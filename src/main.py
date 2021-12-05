import random
import time

import matplotlib.pyplot as plt
import numpy as np

from imports import *

import parameters as parameters
import readCSV as readCSV
import testCumulativeDeaths as testCumulativeDeaths
import testDailyDeaths as testDailyDeaths
import createDataset as createDataset
import printTheta as printTheta


def main():
    startTime = time.time()

    # Read the real cumulative deaths from stats
    realCumulativeDeaths = readCSV.read()

    # Theta
    createDataset.create()
    [theta, predictedDailyDeaths, predictedCumulativeDeaths,
        predictedCumulativeSusceptible, predictedCumulativeExposed, predictedCumulativeInfectious] = createDataset.getThetaAndPredictedDailyDeaths()

    # Convert to numpy arrays
    realCumulativeDeaths = np.array(realCumulativeDeaths)
    predictedCumulativeDeaths = np.array(predictedCumulativeDeaths)

    # Compute the best set of parameters using the least_squares_error
    # This is not the best approach, becasuse I am considering each parameter to have
    # the same importance (same weight) applied to the model of differential equations

    # A better approach is to make a grid_search or a NN model to guess the right parameters
    bestIdx = -1
    smallestLeastSquaresErrors = float('inf')
    for i in range(createDataset.NUMBER_OF_SAMPLES):
        currLeastSquaresError = np.sum(np.square(np.subtract(realCumulativeDeaths, predictedCumulativeDeaths[i])))
        currLeastSquaresError **= 0.5

        if(currLeastSquaresError < smallestLeastSquaresErrors):
            smallestLeastSquaresErrors = currLeastSquaresError
            bestIdx = i


    # Plot the best predicted graph
    day_no = random.randint(1, 30)
    print("------------------------------")
    print("Number of samples (theta): " + str(createDataset.NUMBER_OF_SAMPLES))
    testCumulativeDeaths.plot(realCumulativeDeaths, predictedCumulativeDeaths[bestIdx], day_no)
    print("------------------------------")
    printTheta.printToSTDOUT(theta[bestIdx])
    print("------------------------------")
    endTime = time.time()
    print("Elapsed time: " + str(round(endTime - startTime, 2)) + " seconds")
    print("------------------------------")


if __name__ == "__main__":
    main()
    plt.show()
