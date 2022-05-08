import bs4
import requests
from dotenv import load_dotenv
import os
load_dotenv()

def getForecastItems():
    page = requests.get(os.environ.get("REQUEST_LINK"))
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    forecasts = soup.find(id="seven-day-forecast")
    forecastItems = forecasts.find_all(class_="tombstone-container")
    return forecastItems