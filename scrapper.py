from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import html_parser
import exporter

urls_teams_enum={}
player_data_df=[]

def running_scrapper(team="all"):
    s = Service("/usr/lib/chromium-browser/chromedriver")
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    option.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=option, service=s)
    driver.get("https://www.nhl.com/redwings/roster")
    urls = len(driver.find_elements(By.CSS_SELECTOR, "div.name-col__list"))
    for url in range(urls):
        player=[]
        elements = driver.find_elements(By.CSS_SELECTOR, "div.name-col__list")
        driver.execute_script("arguments[0].click();", elements[url])
        player.append(html_parser.parser(driver.page_source))
        driver.back()
        player_data_df.append(exporter.write_player_data_to_df(player))
        print(player_data_df)
    for player_dataframe in player_data_df:
        complete_dataframe = pd.merge(complete_dataframe, player_data_df[player_dataframe])
    
