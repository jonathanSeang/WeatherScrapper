import bs4
import requests

#Link to National Weather Service forecast location
REQUEST_LINK = "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"

def printNumPeriodsPerWeather(forecast_items):
    map = {}
    for item in forecast_items:
        currDesc = item.find(class_="short-desc").get_text()
        map[currDesc] = map.get(currDesc, 0) + 1

    itemsSorted = dict(sorted(map.items()))
    print("{:<50} {:<10}".format("Weather", "# periods"))
    print("{:<50} {:<10}".format("--------------------------------", "--------"))
    for item in itemsSorted: 
        print("{:<50} {:<10}".format(item, map[item]))
    print("{:<50} {:<10}".format("--------------------------------", "--------"))

def main():
    page = requests.get(REQUEST_LINK)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    forecasts = soup.find(id="seven-day-forecast")
    forecast_items = forecasts.find_all(class_="tombstone-container")

    printNumPeriodsPerWeather(forecast_items)

if __name__ == "__main__":
    main()

