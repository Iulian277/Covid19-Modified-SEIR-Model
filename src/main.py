import matplotlib.pyplot as plt

from imports import *

import parameters as parameters
import resolveODES as resolveODES
import readCSV as readCSV
import testCumulativeDeaths as testCumulativeDeaths
import testDailyDeaths as testDailyDeaths


def main():
    realDeaths = readCSV.read()
    predictedDeaths = resolveODES.resolve()

    day_no = 25
    print("Day " + str(day_no))
    print("------------------------------")
    testCumulativeDeaths.plot(realDeaths, predictedDeaths, day_no)
    print("------------------------------")
    testDailyDeaths.plot(realDeaths, predictedDeaths, day_no)
    print("------------------------------")
    print(parameters.theta["R0"])

if __name__ == "__main__":
    main()
    plt.show()
