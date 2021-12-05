from imports import *

def printToSTDOUT(theta):

    theta_dict = {
        "R0": theta[0],

        "T_vac": theta[1],
        "T_inc": theta[2],
        "T_inf": theta[3],

        "T_m": theta[4],
        "T_v": theta[5],
        "T_h": theta[6],
        "T_f": theta[7],

        "P_m": 1 - theta[8] - theta[9] - theta[10],
        "P_v": theta[8],
        "P_h": theta[9],
        "P_f": theta[10],
    }

    theta_dict_rounded = {k: round(v, 3) for k,v in theta_dict.items()}

    print("Best theta parameters: " + str(theta_dict_rounded))
