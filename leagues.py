# from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ["MOZ_HEADLESS"] = "1"
browser = webdriver.Firefox()


def find_league_names():
    leftMenu__text = browser.find_elements(By.CSS_SELECTOR, "span.leftMenu__text")
    leagues_names = []
    for league in leftMenu__text:
        leagues_names.append(league.text)
    return leagues_names


def find_league_links():
    leftMenu__href = browser.find_elements(By.CSS_SELECTOR, "a.leftMenu__href")
    links = []
    for link in leftMenu__href:
        links.append(link.get_attribute("href"))
    return links


def find_leagues():
    browser.get("https://www.flashscore.pl/")
    leagues = find_league_names()
    # print(leagues)

    links = find_league_links()
    # print(links)
    leagues_all = {
        "name": leagues,
        "link": links,
    }
    browser.close()
    return leagues_all
