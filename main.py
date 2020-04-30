import matplotlib.pyplot as plt

from core.plot import *

if __name__ == '__main__':
    fig = plt.figure(dpi=300)
    plot = fig.add_subplot('111', projection='3d')

    plot_bloch_sphere(plot)

    # basis
    plot_qubit(plot, zero_qubit, color='xkcd:red', label='|0⟩')
    plot_qubit(plot, plus_qubit, color='xkcd:green', label='|+⟩')
    plot_qubit(plot, cw_qubit, color='xkcd:blue', label='|↻⟩')

    qubit = T @ H @ zero_qubit
    plot_qubit(plot, qubit, color='xkcd:teal', label='|v⟩')

    plot.legend(loc="upper left")
    fig.show()
