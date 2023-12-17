import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

os.environ["MOZ_HEADLESS"] = "1"
browser = webdriver.Firefox()


def find_events_live_and_today(url):
    browser.get(url)
    table_event = browser.find_elements(
        By.CSS_SELECTOR, "div.leagues--static.event--leagues.summary-fixtures"
    )
    time.sleep(1)
    # print(table_event)
    events_list = []
    try:
        table_event = table_event[0]
    except:
        return events_list
    events = table_event.find_elements(By.XPATH, '//*[starts-with(@id, "g_1")]')
    for item in events:
        if (
            item.get_attribute("class")
            == "event__match event__match--scheduled event__match--twoLine"
            or item.get_attribute("class")
            == "event__match event__match--scheduled event__match--last event__match--twoLine"
            or item.get_attribute("class")
            == "event__match event__match--live event__match--twoLine"
            or item.get_attribute("class")
            == "event__match event__match--live event__match--last event__match--twoLine"
        ):
            temp = item.get_attribute("id")
            temp = temp.split("_")
            temp = temp[-1]
            temp = "https://www.flashscore.pl/mecz/" + temp + "/#/szczegoly-meczu"
            # print(temp)
            events_list.append(temp)
    return events_list


def find_events_next(url):
    browser.get(url)
    table_event = browser.find_elements(
        By.CSS_SELECTOR, "div.leagues--static.event--leagues.summary-fixtures"
    )
    time.sleep(1)
    # print(table_event)
    events_list = []
    try:
        table_event = table_event[0]
    except:
        return events_list
    events = table_event.find_elements(By.XPATH, '//*[starts-with(@id, "g_1")]')
    for item in events:
        if (
            item.get_attribute("class")
            == "event__match event__match--static event__match--scheduled event__match--twoLine"
            or item.get_attribute("class")
            == "event__match event__match--static event__match--scheduled event__match--last event__match--twoLine"
        ):
            temp = item.get_attribute("id")
            temp = temp.split("_")
            temp = temp[-1]
            temp = "https://www.flashscore.pl/mecz/" + temp + "/#/szczegoly-meczu"
            # print(temp)
            events_list.append(temp)
    return events_list
