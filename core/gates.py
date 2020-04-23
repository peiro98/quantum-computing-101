import numpy as np

H = 1 / np.sqrt(2) * np.array([[1, 1],
                               [1, -1]])

# Pauli X
X = np.array([[0, 1],
              [1, 0]])

# Pauli Y
Y = np.array([[0, -1j],
              [1j, 0]])

# Pauli Z
Z = np.array([[1, 0],
              [0, -1]])


def phase_shift(phi: np.real):
    return np.array([[1, 0],
                     [0, np.e ** (1.0j * phi)]])


# S is a pi/2 rotation about the z-axis
S = phase_shift(np.pi / 2)
Sdg = phase_shift(-np.pi / 2)

# T is a pi/4 rotation about the z-axis
T = phase_shift(np.pi / 4)
Tdg = phase_shift(-np.pi / 4)

# Cx is a controlled NOT gate.
# When applied to two qubits a rotation of pi/2 radians
# is applied to the target qubit if the control qubit is |1⟩
# |a, b⟩ --> |a, a ⊗ b⟩
# |00⟩ --> |00⟩, |01⟩ --> |01⟩, |10⟩ --> |11⟩, |11⟩ --> |10⟩
Cx = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 1],
               [0, 0, 1, 0]])
