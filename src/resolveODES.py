from imports import *
import defineODES as defineODES
import parameters as parameters

from scipy.integrate import odeint

def resolve():
    # Initial conditions
    S0 = parameters.N - parameters.I0
    E0 = 0
    I0 = parameters.I0

    M0 = 0
    R_M0 = 845351

    V0 = 0
    R_V0 = 100000

    H0 = 0
    R_H0 = 100000

    F0 = 0
    R_F0 = 33785

    days = np.linspace(1, 30, 30)
    x = odeint(defineODES.odes, [S0, E0, I0, M0, R_M0, V0, R_V0, H0, R_H0, F0, R_F0], days)


    S   = x[:,0]
    E   = x[:,1]
    I   = x[:,2]

    M   = x[:,3]
    R_M = x[:,4]

    V   = x[:,5]
    R_V = x[:,6]

    H   = x[:,7]
    R_H = x[:,8]

    F   = x[:,9]
    R_F = x[:,10]

    # Plot the results
    # plt.figure(0)
    # plt.plot(days, S)
    # plt.plot(days, E)
    # plt.plot(days, I)
    # plt.legend(["S", "E", "I"])
    #
    #
    # plt.figure(1)
    # plt.plot(days, M)
    # plt.plot(days, R_M)
    # plt.legend(["M", "R_M"])
    #
    # plt.figure(2)
    # plt.plot(days, V)
    # plt.plot(days, R_V)
    # plt.legend(["V", "R_V"])
    #
    # plt.figure(3)
    # plt.plot(days, H)
    # plt.plot(days, R_H)
    # plt.legend(["H", "R_H"])

    return R_F
