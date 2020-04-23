import math

import numpy as np

# |0⟩ and |1⟩ basis (z-axis)
zero_qubit = np.array([1, 0]).T
one_qubit = np.array([0, 1]).T

# |+⟩ and |-⟩ basis (x-axis)
plus_qubit = 1 / np.sqrt(2) * np.array([1, 1]).T
minus_qubit = 1 / np.sqrt(2) * np.array([1, -1]).T

# |↺⟩ and |↻⟩ basis (y-axis)
cw_qubit = 1 / np.sqrt(2) * np.array([1, 1.0j]).T
ccw_qubit = 1 / np.sqrt(2) * np.array([1, -1.0j]).T


def prob_to_qubit(zero, one):
    if not math.isclose(zero + one, 1.0, abs_tol=1e-4) or zero < 0.0 or one < 0.0:
        raise Exception("zero and one must represent valid probability values")

    return np.array([np.sqrt(zero), np.sqrt(one)]).T
