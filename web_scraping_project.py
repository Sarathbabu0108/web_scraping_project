import requests
from bs4 import BeautifulSoup
import pandas as pd

# copy the forecast url
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.884250000000065&lon=-87.63244999999995#.YPWMqegzbIU")
# creating object out of  that page
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast")
# print(week)
items = week.find_all(class_="tombstone-container")
#print(items[0])
# find will help us to find the given text
# get_text used to separate a text Eg: Today
print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_="temp").get_text())
# we are going to write a for loop to go through all of the item
period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
#print(period_names)
#print(short_descriptions)
#print(temperatures)
# we are using pandas to make so easy to turn this data to a table

weather_stuff = pd.DataFrame(
    {'period': period_names,
     'short desc': short_descriptions,
     'temperatures': temperatures}
    )

print(weather_stuff)
#Awesome feature of panda stuff
weather_stuff.to_csv('weather.csv')
