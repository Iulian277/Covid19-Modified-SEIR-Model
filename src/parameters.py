import numpy as np
import random

### Starting time: July 1 2021 ###

# Fixed
N = 19084460 # Total number of population
I0 = 1080792 # Initial number of infections

N_vac = 0.4 # Vaccinated population rate
P_vac = 0.9 # Decrease transmition by after vaccinating population rate


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
