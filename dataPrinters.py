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
