import dataRetriever
import dataPrinters

def main():

    forecastItems = dataRetriever.getForecastItems()
    print(forecastItems)
    #dataPrinters.printNumPeriodsPerWeather(forecastItems)

if __name__ == "__main__":
    main()

