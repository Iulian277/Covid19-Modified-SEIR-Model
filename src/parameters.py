import numpy as np
import random

### Starting time: July 1 2021 ###

# Fixed
N = 19084460 # Total number of population
I0 = 1080792 # Initial number of infections

N_vac = 0.4 # Vaccinated population rate
P_vac = 0.9 # Decrease transmition by after vaccinating population rate

# Variables
R0 = random.choice(np.linspace(1.5, 2.5)) # Basic reproduction number

T_vac = random.choice(np.linspace(7, 14)) # Length of vaccine until immunity (days)
T_inc = random.choice(np.linspace(2, 14)) # Length of incubation period (days)
T_inf = random.choice(np.linspace(3, 14)) # Length of infectiousness to death (days)

T_m = random.choice(np.linspace(5, 14))  # Recovery time from mild symptoms (days)
T_v = random.choice(np.linspace(7, 40))  # Recovery time from sever symptoms at home (days)
T_h = random.choice(np.linspace(7, 40))  # Recovery time from sever symptoms at hospital (days)
T_f = random.choice(np.linspace(15, 35)) # Time from end of infectiousness to death (days)

P_v = random.choice(np.linspace(0.05, 0.15))    # Sever home symptoms rate
P_h = random.choice(np.linspace(0.05, 0.15))    # Sever hospital symptoms rate
P_f = random.choice(np.linspace(0.001, 0.01))   # Case fatility rate
P_m = 1 - P_v - P_h - P_f                       # Mild symptoms rate


BETA  = (float) ((1 - N_vac) * (1 - P_vac) * R0 / T_inf) # Transmission rate
SIGMA = (float) (1.0 / T_inc)                            # Rate of getting infectious from being expose
GAMMA = (float) (1.0 / T_inf)                            # Recovery rate (from M, V, H)

# All variable parameters (11)
theta = {
    "R0": R0,

    "T_vac": T_vac,
    "T_inc": T_inc,
    "T_inf": T_inf,

    "P_v": P_v,
    "P_h": P_h,
    "P_f": P_f,

    "T_m": T_m,
    "T_v": T_v,
    "T_h": T_h,
    "T_f": T_f,
    }


# Ranges of variable parameters for dataset
R0_range = np.linspace(1.5, 2.5) # Basic reproduction number

T_vac_range = np.linspace(7, 14) # Length of vaccine until immunity (days)
T_inc_range = np.linspace(2, 14) # Length of incubation period (days)
T_inf_range = np.linspace(3, 14) # Length of infectiousness to death (days)

T_m_range = np.linspace(5, 14)  # Recovery time from mild symptoms (days)
T_v_range = np.linspace(7, 40)  # Recovery time from sever symptoms at home (days)
T_h_range = np.linspace(7, 40)  # Recovery time from sever symptoms at hospital (days)
T_f_range = np.linspace(15, 35) # Time from end of infectiousness to death (days)

P_v_range = np.linspace(0.05, 0.15)    # Sever home symptoms rate
P_h_range = np.linspace(0.05, 0.15)    # Sever hospital symptoms rate
P_f_range = np.linspace(0.001, 0.01)   # Case fatility rate

