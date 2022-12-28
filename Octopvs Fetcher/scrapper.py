from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import html_parser
import exporter

teams=(
    ("Anaheim Ducks","https://www.nhl.com/ducks/roster"),("Arizona Coyotes","https://www.nhl.com/coyotes/roster/"),("Boston Bruins","https://www.nhl.com/bruins/roster/"),\
    ("Buffalo Sabres","https://www.nhl.com/sabres/roster/"),("Calgary Flames","https://www.nhl.com/flames/roster/"),("Carolina Hurricanes","https://www.nhl.com/hurricanes/roster/"),\
    ("Chicago Blackhawks","https://www.nhl.com/blackhawks/roster/"),("Colorado Avalanche","https://www.nhl.com/avalanche/roster/"),("Columbus Blue Jackets","https://www.nhl.com/bluejackets/roster/"),\
    ("Dallas Stars","https://www.nhl.com/stars/roster/"),("Detroit Red Wings","https://www.nhl.com/redwings/roster/"),("Edmonton Oilers","https://www.nhl.com/oilers/roster/"),\
    ("Florida Panthers","https://www.nhl.com/panthers/roster/"),("Los Angeles Kings","https://www.nhl.com/kings/roster/"),("Minnesota Wild","https://www.nhl.com/wild/roster/"),\
    ("Montréal Canadiens","https://www.nhl.com/canadiens/roster/"),("Nashville Predators","https://www.nhl.com/predators/roster/"),("New Jersey Devils","https://www.nhl.com/devils/roster/"),\
    ("New York Islanders","https://www.nhl.com/islanders/roster/"),("New York Rangers","https://www.nhl.com/rangers/roster/"),("Ottawa Senators","https://www.nhl.com/senators/roster/"),
    ("Philadelphia Flyers","https://www.nhl.com/flyers/roster/"),("Pittsburgh Penguins","https://www.nhl.com/penguins/roster/"),("San Jose Sharks","https://www.nhl.com/sharks/roster/"),\
    ("Seattle Kraken","https://www.nhl.com/kraken/roster/"),("Tampa Bay Lightning","https://www.nhl.com/lightning/roster/"),("Toronto Maple Leafs","https://www.nhl.com/mapleleafs/roster/"),\
    ("St. Louis Blues","https://www.nhl.com/blues/roster/"),("Vancouver Canucks","https://www.nhl.com/canucks/roster/"),("Vegas Golden Knights","https://www.nhl.com/goldenknights/roster/"),\
    ("Washington Capitals","https://www.nhl.com/capitals/roster/"),("Winnipeg Jets","https://www.nhl.com/jets/roster/")
)

def scrappy_execute():
    s = Service("/usr/lib/chromium-browser/chromedriver")
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    option.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=option, service=s)
    delay = 3
    for team in teams:
        driver.get(team[1])
        driver_wait = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.name-col__list")))
        print(f"Fetching data from {team[0]}")
        player_data_df=[]
        urls = len(driver.find_elements(By.CSS_SELECTOR, "div.name-col__list"))
        for url in range(urls):
            player=[]
            try:
                execute_page(driver, url, player)
            except TimeoutException:
                time.sleep(delay)
                execute_page(driver, url, player)
            player_data_df.append(exporter.write_player_data_to_df(player))
            exporter.export_data_to_csv(player_data_df[url])
    
def execute_page(driver, url, player):
    elements = driver.find_elements(By.CSS_SELECTOR, "div.name-col__list")
    driver.execute_script("arguments[0].click();", elements[url])
    player.append(html_parser.player_parser(driver.page_source))
    print(f"Getting data from {player[0][0]} ({player[0][3][-1]})")
    driver.back()