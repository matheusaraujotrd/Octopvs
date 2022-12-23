from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import html_parser
import pandas as pd

s = Service("/usr/lib/chromium-browser/chromedriver")
option = webdriver.ChromeOptions()
option.add_argument("headless")
option.add_argument("--log-level=3")
driver = webdriver.Chrome(options=option, service=s)
driver.get("https://www.nhl.com/redwings/roster")
urls = len(driver.find_elements(By.CSS_SELECTOR, "div.name-col__list"))
for x in range(urls):
    player=[]
    elements = driver.find_elements(By.CSS_SELECTOR, "div.name-col__list")
    driver.execute_script("arguments[0].click();", elements[x])
    player.append(html_parser.parser(driver.page_source))
    driver.back()
    print(player)