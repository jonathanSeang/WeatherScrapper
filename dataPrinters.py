import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

def printNumPeriodsPerWeather(forecastItems):
    map = {}
    for item in forecastItems:
        currDesc = item.find(class_="short-desc").get_text()
        map[currDesc] = map.get(currDesc, 0) + 1

    itemsSorted = dict(sorted(map.items()))
    print("{:<50} {:<10}".format("Weather", "# periods"))
    print("{:<50} {:<10}".format("--------------------------------", "--------"))
    for item in itemsSorted: 
        print("{:<50} {:<10}".format(item, map[item]))
    print("{:<50} {:<10}".format("--------------------------------", "--------"))

def plotPeriodTemp(forecastItems):
    allPeriods = []
    allTemps = []
    for item in forecastItems:
        period = item.find(class_="period-name").get_text()
        temp = int(item.find(class_="temp").get_text()[-6:-3])
        allPeriods.append(period)
        allTemps.append(temp)

    # make smooth
    idx = range(len(allPeriods))
    xnew = np.linspace(min(idx), max(idx), 300)

    spl = make_interp_spline(idx, allTemps, k=3)
    smooth = spl(xnew)

    plt.rc('font', size=5)
    plt.title("Period to temperature")
    plt.xlabel("Period")
    plt.ylabel("Temperature °F")

    plt.plot(xnew, smooth)
    plt.xticks(idx, allPeriods)
    plt.savefig('periodTemp.png', bbox_inches='tight')
    plt.show()
    

