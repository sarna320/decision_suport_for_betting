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


def find_next_event_numer():
    events_nr = browser.find_elements(
        By.CSS_SELECTOR, "div.event__round.event__round--static"
    )
    next_event_nr = events_nr[1].text
    return next_event_nr

def find_home_participant():
    table_event = browser.find_elements(
    By.CSS_SELECTOR, "div.leagues--static.event--leagues.summary-fixtures"
    )
    next_table_event = table_event[0]
    # print(table_event)
    # print(next_table_event)
    home_participant = []
    home_participant_css = next_table_event.find_elements(
        By.CSS_SELECTOR, "div.event__participant.event__participant--home"
    )
    for item in home_participant_css:
        home_participant.append(item.text)
    return home_participant

def find_away_participant():
    table_event = browser.find_elements(
    By.CSS_SELECTOR, "div.leagues--static.event--leagues.summary-fixtures"
    )
    next_table_event = table_event[0]
    # print(table_event)
    # print(next_table_event)
    away_participant = []
    away_participant_css = next_table_event.find_elements(
        By.CSS_SELECTOR, "div.event__participant.event__participant--away"
    )
    for item in away_participant_css:
        away_participant.append(item.text)
    return away_participant

# To not show mozzila
os.environ["MOZ_HEADLESS"] = "1"

browser = webdriver.Firefox()
browser.get("https://www.flashscore.pl/")

leagues = find_league_names()
# print(leagues)

links = find_links()
# print(links)

browser.get(links[0])  # showing first league

next_event_nr=find_next_event_numer()
#print(next_event_nr)

home_participant=find_home_participant()
#print(home_participant)

away_participant=find_away_participant()
#print(away_participant)

browser.close()
