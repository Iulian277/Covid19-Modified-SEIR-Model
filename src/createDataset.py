import random
from scipy.integrate import odeint

from imports import *
import parameters as parameters

NUMBER_OF_SAMPLES = 1000

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

#
theta = []  # Tuple of variable parameters (11)
predicted_daily_deaths = []

predicted_cumulative_deaths = []
predicted_cumulative_susceptible = []
predicted_cumulative_exposed = []
predicted_cumulative_infectious = []

# Last randomly generated theta
lastTheta = {
    "R0": 0,

    "T_vac": 0,
    "T_inc": 0,
    "T_inf": 0,

    "P_m": 0,
    "P_v": 0,
    "P_h": 0,
    "P_f": 0,

    "T_m": 0,
    "T_v": 0,
    "T_h": 0,
    "T_f": 0,
    }


def odes(x, t):
    #
    S   = x[0]
    E   = x[1]
    I   = x[2]

    M   = x[3]
    R_m = x[4]

    V   = x[5]
    R_v = x[6]

    H   = x[7]
    R_h = x[8]

    F   = x[9]
    R_f = x[10]

    #
    BETA  = (float) ((1 - parameters.N_vac) * (1 - parameters.P_vac) * lastTheta["R0"] / lastTheta["T_inf"])  # Transmission rate
    SIGMA = (float) (1.0 / lastTheta["T_inc"])  # Rate of getting infectious from being expose
    GAMMA = (float) (1.0 / lastTheta["T_inf"])  # Recovery rate (from M, V, H)

    #
    dSdt  = -BETA * I * S
    dEdt  =  BETA * I * S - SIGMA * E
    dIdt  =  SIGMA * E - GAMMA * I

    #
    dMdt  = parameters.P_vac * parameters.N_vac * lastTheta["P_m"] * GAMMA * I - M / lastTheta["T_m"]
    dRmdt = M / lastTheta["T_m"]

    dVdt  = (1 - parameters.P_vac) * (1 - parameters.N_vac) * lastTheta["P_v"] * GAMMA * I - V / lastTheta["T_v"]
    dRvdt = V / lastTheta["T_v"]

    dHdt  = (1 - parameters.P_vac) * (1 - parameters.N_vac) * lastTheta["P_h"] * GAMMA * I - H / lastTheta["T_h"]
    dRhdt = H / lastTheta["T_h"]

    dFdt  = (1 - parameters.P_vac) * (1 - parameters.N_vac) * lastTheta["P_f"] * GAMMA * I - F / lastTheta["T_f"]
    dRfdt = F / lastTheta["T_f"]


    return [dSdt, dEdt, dIdt, dMdt, dRmdt, dVdt, dRvdt, dHdt, dRhdt, dFdt, dRfdt]


def randomTheta():
    R0 = random.choice(parameters.R0_range)

    T_vac = random.choice(parameters.T_vac_range)
    T_inc = random.choice(parameters.T_inc_range)
    T_inf = random.choice(parameters.T_inf_range)

    T_m = random.choice(parameters.T_m_range)
    T_v = random.choice(parameters.T_v_range)
    T_h = random.choice(parameters.T_h_range)
    T_f = random.choice(parameters.T_f_range)

    P_v = random.choice(parameters.P_v_range)
    P_h = random.choice(parameters.P_h_range)
    P_f = random.choice(parameters.P_f_range)

    return [R0, T_vac, T_inc, T_inf, T_m, T_v, T_h, T_f, P_v, P_h, P_f]


def create():
    for i in range(NUMBER_OF_SAMPLES):
        [R0, T_vac, T_inc, T_inf, T_m, T_v, T_h, T_f, P_v, P_h, P_f] = randomTheta()
        theta.append([R0, T_vac, T_inc, T_inf, T_m, T_v, T_h, T_f, P_v, P_h, P_f])

        lastTheta["R0"] = R0

        lastTheta["T_vac"] = T_vac
        lastTheta["T_inc"] = T_inc
        lastTheta["T_inf"] = T_inf

        lastTheta["T_m"] = T_m
        lastTheta["T_v"] = T_v
        lastTheta["T_h"] = T_h
        lastTheta["T_f"] = T_f

        lastTheta["P_m"] = 1 - P_v - P_h - P_f
        lastTheta["P_v"] = P_v
        lastTheta["P_h"] = P_h
        lastTheta["P_f"] = P_f

        days = np.linspace(1, 30, 30)
        x = odeint(odes, [S0, E0, I0, M0, R_M0, V0, R_V0, H0, R_H0, F0, R_F0], days)

        S = x[:,0]
        predicted_cumulative_susceptible.append(S)

        E = x[:,1]
        predicted_cumulative_exposed.append(E)

        I = x[:,2]
        predicted_cumulative_infectious.append(I)

        R_F = x[:,10]
        predicted_cumulative_deaths.append(R_F)

        # Until now, we have generated cumulative deaths
        # Create daily deaths
        curr_daily_vector = []
        for j in range(1, len(predicted_cumulative_deaths[i])):
            curr_daily_vector.append(predicted_cumulative_deaths[i][j] - predicted_cumulative_deaths[i][j-1])
        predicted_daily_deaths.append(curr_daily_vector)


def getThetaAndPredictedDailyDeaths():
    return [theta, predicted_daily_deaths, predicted_cumulative_deaths,
            predicted_cumulative_susceptible, predicted_cumulative_exposed, predicted_cumulative_infectious]
