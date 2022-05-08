import dataRetriever
import dataPrinters
import matplotlib.pyplot as plt

def main():

    forecastItems = dataRetriever.getForecastItems()
    # dataPrinters.printNumPeriodsPerWeather(forecastItems)
    dataPrinters.plotPeriodTemp(forecastItems)

if __name__ == "__main__":
    main()