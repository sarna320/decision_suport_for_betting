import os
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By


def find_league_names():
    leftMenu__text = browser.find_elements(By.CSS_SELECTOR, "span.leftMenu__text")
    leagues_names = []
    for league in leftMenu__text:
        leagues_names.append(league.text)
    return leagues_names


def find_links():
    leftMenu__href = browser.find_elements(By.CSS_SELECTOR, "a.leftMenu__href")
    links = []
    for link in leftMenu__href:
        links.append(link.get_attribute("href"))
    return links


# To not show mozzila
os.environ["MOZ_HEADLESS"] = "1"

browser = webdriver.Firefox()
browser.get("https://www.flashscore.pl/")

leagues = find_league_names()
# print(leagues)

links = find_links()
# print(links)

browser.get(links[0])  # showing first league
events_nr = browser.find_elements(
    By.CSS_SELECTOR, "div.event__round.event__round--static"
)
next_event_nr = events_nr[1].text
print(next_event_nr)

browser.close()
