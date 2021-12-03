import matplotlib.pyplot as plt

from imports import *

def plot(realDeaths, predictedDeaths, day_no):
    predictedDailyDeaths = []
    for i in range(1, len(predictedDeaths)):
        predictedDailyDeaths.append(predictedDeaths[i] - predictedDeaths[i-1])

    realDailyDeaths = []
    for i in range(1, len(realDeaths)):
        realDailyDeaths.append(realDeaths[i] - realDeaths[i - 1])


    print("Predicted Daily Deaths: " + str(math.floor(predictedDailyDeaths[day_no - 1])))
    print("Real Daily Deaths: " + str(math.floor(realDailyDeaths[day_no - 1])))
    print("Percentage: " +
        str(min([math.floor(predictedDailyDeaths[day_no - 1]), math.floor(realDailyDeaths[day_no - 1])]) /
            max([math.floor(predictedDailyDeaths[day_no - 1]), math.floor(realDailyDeaths[day_no - 1])])))


    # Plots
    plt.figure(1)
    days = np.linspace(1, len(realDeaths) - 1, len(realDeaths) - 1)

    plt.scatter(days, predictedDailyDeaths)
    plt.scatter(days, realDailyDeaths)

    plt.legend(["PREDICTED_DAILY_DEATHS", "REAL_DAILY_DEATHS"], loc="upper right")
    plt.show(block=False)