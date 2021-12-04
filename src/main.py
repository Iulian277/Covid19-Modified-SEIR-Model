import random

import matplotlib.pyplot as plt

from imports import *

import parameters as parameters
import resolveODES as resolveODES
import readCSV as readCSV
import testCumulativeDeaths as testCumulativeDeaths
import testDailyDeaths as testDailyDeaths
import createDataset as createDataset


def main():
    realDeaths = readCSV.read()
    # predictedDeaths = resolveODES.resolve()
    #
    # day_no = random.randint(1, 30)
    # print("Day " + str(day_no))
    # print("------------------------------")
    # testCumulativeDeaths.plot(realDeaths, predictedDeaths, day_no)
    # print("------------------------------")
    # testDailyDeaths.plot(realDeaths, predictedDeaths, day_no)
    # print("------------------------------")
    # print(parameters.theta["R0"])

    # theta =
    createDataset.create()
    [theta, predictedDailyDeaths, predictedCumulativeDeaths] = createDataset.getThetaAndPredictedDailyDeaths()

    realDailyDeaths = []
    for i in range(1, len(realDeaths)):
        realDailyDeaths.append(realDeaths[i] - realDeaths[i - 1])


    # bestIdx = -1
    # smallestLeastSquaresErrors = float('inf')
    # for i in range(createDataset.NUMBER_OF_SAMPLES):
    #     currLeastSquaresError = 0
    #     for j in range(len(realDeaths) - 1):
    #         currLeastSquaresError += (realDailyDeaths[j] - predictedDailyDeaths[i][j]) ** 2
    #     currLeastSquaresError = currLeastSquaresError ** 0.5
    #
    #     if(currLeastSquaresError < smallestLeastSquaresErrors):
    #         smallestLeastSquaresErrors = currLeastSquaresError
    #         bestIdx = i

    # Plot the best graph
    # plt.figure(0)
    # days = np.linspace(1, len(realDeaths) - 1, len(realDeaths) - 1)
    #
    # plt.scatter(days, predictedDailyDeaths[bestIdx])
    # plt.scatter(days, realDailyDeaths)
    #
    # plt.legend(["PREDICTED_DAILY_DEATHS", "REAL_DAILY_DEATHS"], loc="upper right")
    # plt.show(block=False)
    #
    # print(bestIdx)




if __name__ == "__main__":
    main()
    plt.show()
