import matplotlib.pyplot as plt
import numpy as np

from imports import *

def plot(realDeaths, predictedDeaths, day_no):
    print("Day: " + str(day_no))
    print("Predicted Cumulative Deaths: " + str(math.floor(predictedDeaths[day_no - 1])))
    print("Real Cumulative Deaths: " + str(math.floor(realDeaths[day_no - 1])))
    print("Percentage: " +
        str(round(
                min([math.floor(predictedDeaths[day_no - 1]), math.floor(realDeaths[day_no - 1])]) /
                max([math.floor(predictedDeaths[day_no - 1]), math.floor(realDeaths[day_no - 1])])
            , 5)))

    plt.figure(0)
    days = np.linspace(1, len(realDeaths), len(realDeaths))
    plt.plot(days, predictedDeaths)
    interp = scipy.interpolate.interp1d(days, realDeaths)
    plt.plot(days, interp(days))
    plt.legend(["PREDICTED_CUMULATIVE_DEATHS", "REAL_CUMULATIVE_DEATHS"], loc="upper left")
    plt.show(block=False)