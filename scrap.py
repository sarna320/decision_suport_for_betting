import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

os.environ["MOZ_HEADLESS"] = "1"
browser = webdriver.Firefox()

browser.get("https://www.flashscore.pl/mecz/4AtrLXsT/#/szczegoly-meczu")
time.sleep(1)

home_table = browser.find_element(
    By.CSS_SELECTOR, "div.detailTeamForm__team.detailTeamForm__team--home"
)
home_name = home_table.find_element(By.CSS_SELECTOR, "a.detailTeamForm__teamName").text
print("Home:"+home_name)

away_table = browser.find_element(
    By.CSS_SELECTOR, "div.detailTeamForm__team.detailTeamForm__team--away"
)
away_name = away_table.find_element(By.CSS_SELECTOR, "a.detailTeamForm__teamName").text
print("Away:"+away_name)

home_draw = 0
try:
    home_draw_temp = home_table.find_elements(
        By.CSS_SELECTOR, "div.formIcon.formIcon--d"
    )
    for i in home_draw_temp:
        home_draw += 1
except:
    print("no draws")
print(f"Home team draws:{home_draw}")

home_win = 0
try:
    home_draw_temp = home_table.find_elements(
        By.CSS_SELECTOR, "div.formIcon.formIcon--w"
    )
    for i in home_draw_temp:
        home_win += 1
except:
    print("no wins")
print(f"Home team wins:{home_win}")

home_lose = 0
try:
    home_draw_temp = home_table.find_elements(
        By.CSS_SELECTOR, "div.formIcon.formIcon--l"
    )
    for i in home_draw_temp:
        home_lose += 1
except:
    print("no loses")
print(f"Home team loses:{home_lose}")

home_last_5_games = {
    "win": home_win,
    "lose": home_lose,
    "draw": home_draw,
}

away_draw = 0
try:
    home_draw_temp = away_table.find_elements(
        By.CSS_SELECTOR, "div.formIcon.formIcon--d"
    )
    for i in home_draw_temp:
        away_draw += 1
except:
    print("no draws")
print(f"Away team draws:{away_draw}")

away_win = 0
try:
    home_draw_temp = away_table.find_elements(
        By.CSS_SELECTOR, "div.formIcon.formIcon--w"
    )
    for i in home_draw_temp:
        away_win += 1
except:
    print("no wins")
print(f"Away team wins:{away_win}")

away_lose = 0
try:
    home_draw_temp = away_table.find_elements(
        By.CSS_SELECTOR, "div.formIcon.formIcon--l"
    )
    for i in home_draw_temp:
        away_lose += 1
except:
    print("no loses")
print(f"Away team loses:{away_lose}")

away_last_5_games = {
    "win": away_win,
    "lose": away_lose,
    "draw": away_draw,
}
