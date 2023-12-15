# from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ["MOZ_HEADLESS"] = "1"
browser = webdriver.Firefox()


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


def find_links_to_events():
    table_event = browser.find_elements(
        By.CSS_SELECTOR, "div.leagues--static.event--leagues.summary-fixtures"
    )
    next_table_event = table_event[0]

    id_event = next_table_event.find_elements(By.XPATH, '//*[starts-with(@id, "g_1")]')
    # print(id_event)

    link_to_events = []
    for item in id_event:
        if "event__match event__match--static event__match--scheduled event__match--twoLine" == item.get_attribute(
            "class"
        ) or "event__match event__match--static event__match--scheduled event__match--last event__match--twoLine" == item.get_attribute(
            "class"
        ):
            temp = item.get_attribute("id")
            temp = temp.split("_")
            temp = temp[-1]
            temp = "https://www.flashscore.pl/mecz/" + temp + "/#/szczegoly-meczu"
            # print(temp)
            link_to_events.append(temp)
    return link_to_events


def find_all_events(url):
    browser.get(url)

    # next_event_nr = find_next_event_numer()
    # print(next_event_nr)

    home_participant = find_home_participant()
    # print(home_participant)

    away_participant = find_away_participant()
    # print(away_participant)

    link_to_events = find_links_to_events()
    next_events = {
        "home": home_participant,
        "away": away_participant,
        "link": link_to_events,
    }
    browser.close()
    return next_events
