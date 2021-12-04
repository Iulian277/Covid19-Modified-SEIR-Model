from imports import *
import parameters as parameters

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
    dSdt  = -parameters.BETA * I * S
    dEdt  =  parameters.BETA * I * S - parameters.SIGMA * E
    dIdt  =  parameters.SIGMA * E - parameters.GAMMA * I

    #
    dMdt  = parameters.P_vac * parameters.N_vac * parameters.P_m * parameters.GAMMA * I - M / parameters.T_m
    dRmdt = M / parameters.T_m

    dVdt  = (1 - parameters.P_vac) * (1 - parameters.N_vac) * parameters.P_v * parameters.GAMMA * I - V / parameters.T_v
    dRvdt = V / parameters.T_v

    dHdt  = (1 - parameters.P_vac) * (1 - parameters.N_vac) * parameters.P_h * parameters.GAMMA * I - H / parameters.T_h
    dRhdt = H / parameters.T_h

    dFdt  = (1 - parameters.P_vac) * (1 - parameters.N_vac) * parameters.P_f * parameters.GAMMA * I - F / parameters.T_f
    dRfdt = F / parameters.T_f


    return [dSdt, dEdt, dIdt, dMdt, dRmdt, dVdt, dRvdt, dHdt, dRhdt, dFdt, dRfdt]