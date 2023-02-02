# Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Initialize the lists to hold player names and links
player_link_name_2014 = []
player_links_2014 = []
player_names_2014 = []

# Loop through each year and page to get player links
for x in range(1, 25):
    url = f'https://www.nfl.com/draft/tracker/prospects/all-positions/all-colleges/all-statuses/2014?page={x}'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    player_link_name = soup.find_all('a', class_='css-1mchkr3')
    for link in player_link_name:
            player_links_2014.append(link['href'])
    for name in player_link_name:
            player_names_2014.append(name.text)

player_link_name_2015 = []
player_links_2015 = []
player_names_2015 = []

for x in range(1, 22):
    url = f'https://www.nfl.com/draft/tracker/prospects/all-positions/all-colleges/all-statuses/2015?page={x}'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    player_link_name = soup.find_all('a', class_='css-1mchkr3')
    for link in player_link_name:
        player_links_2015.append(link['href'])
    for name in player_link_name:
        player_names_2015.append(name.text)

player_link_name_2016 = []
player_links_2016 = []
player_names_2016 = []

for x in range(1, 22):
    url = f'https://www.nfl.com/draft/tracker/prospects/all-positions/all-colleges/all-statuses/2016?page={x}'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    player_link_name = soup.find_all('a', class_='css-1mchkr3')
    for link in player_link_name:
        player_links_2016.append(link['href'])
    for name in player_link_name:
        player_names_2016.append(name.text)


player_link_name_2017 = []
player_links_2017 = []
player_names_2017 = []


for x in range(1, 23):
    url = f'https://www.nfl.com/draft/tracker/prospects/all-positions/all-colleges/all-statuses/2017?page={x}'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    player_link_name = soup.find_all('a', class_='css-1mchkr3')
    for link in player_link_name:
        player_links_2017.append(link['href'])
    for name in player_link_name:
        player_names_2017.append(name.text)

player_link_name_2018 = []
player_links_2018 = []
player_names_2018 = []

for x in range(1, 34):
    url = f'https://www.nfl.com/draft/tracker/prospects/all-positions/all-colleges/all-statuses/2018?page={x}'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    player_link_name = soup.find_all('a', class_='css-1mchkr3')
    for link in player_link_name:
        player_links_2018.append(link['href'])
    for name in player_link_name:
        player_names_2018.append(name.text)

player_link_name_2019 = []
player_links_2019 = []
player_names_2019 = []


for x in range(1, 27):
    url = f'https://www.nfl.com/draft/tracker/prospects/all-positions/all-colleges/all-statuses/2019?page={x}'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    player_link_name = soup.find_all('a', class_='css-1mchkr3')
    for link in player_link_name:
        player_links_2019.append(link['href'])
    for name in player_link_name:
        player_names_2019.append(name.text)

player_link_name_2020 = []
player_links_2020 = []
player_names_2020 = []

for x in range(1, 27):
    url = f'https://www.nfl.com/draft/tracker/prospects/all-positions/all-colleges/all-statuses/2020?page={x}'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    player_link_name = soup.find_all('a', class_='css-1mchkr3')
    for link in player_link_name:
        player_links_2020.append(link['href'])
    for name in player_link_name:
        player_names_2020.append(name.text)

player_link_name_2021 = []
player_links_2021 = []
player_names_2021 = []

for x in range(1, 25):
    url = f'https://www.nfl.com/draft/tracker/prospects/all-positions/all-colleges/all-statuses/2021?page={x}'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    player_link_name = soup.find_all('a', class_='css-1mchkr3')
    for link in player_link_name:
        player_links_2021.append(link['href'])
    for name in player_link_name:
        player_names_2021.append(name.text)

player_link_name_2022 = []
player_links_2022 = []
player_names_2022 = []

for x in range(1, 25):
    url = f'https://www.nfl.com/draft/tracker/prospects/all-positions/all-colleges/all-statuses/2022?page={x}'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    player_link_name = soup.find_all('a', class_='css-1mchkr3')
    for link in player_link_name:
        player_links_2022.append(link['href'])
    for name in player_link_name:
        player_names_2022.append(name.text)

# Join all the link lists into one list
player_links = player_links_2014 + player_links_2015 + player_links_2016 + player_links_2017 + player_links_2018 + \
    player_links_2019 + player_links_2020 + player_links_2021 + player_links_2022

# Join all the name lists into one list
player_names = player_names_2014 + player_names_2015 + player_names_2016 + player_names_2017 + player_names_2018 + \
    player_names_2019 + player_names_2020 + player_names_2021 + player_names_2022

# Create a dataframe
df = pd.DataFrame({'Player': player_names, 'Link': player_links})

# Remove duplicates
df = df.drop_duplicates(subset=['Player'], keep='first')

# Initialize lists to hold the data
player_bios = []
player_grades = []
draft_projection = []

# Loop through the links and scrape the data, should take about 6 hours to run
for index, row in df.iterrows():
    url = row['Link']
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = bs(html, 'html.parser')
    try:
        # Append the player's bio to the dataframe
        player_bio = soup.find('div', class_='player-bio').text
        
    except AttributeError:
        player_bios.append('NA')
        player_grades.append('NA')
        draft_projection.append('NA')

