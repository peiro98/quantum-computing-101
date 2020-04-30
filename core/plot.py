from .gates import *
from .qc import *


def get_bloch_coords(qubit):
    def get_x():
        """
        Write the qubit as a linear combination in the basis |+⟩, |-⟩:
        |v⟩ = a|+⟩ + b|-⟩ = a(H|0⟩) + b(H|1⟩)
        Project |v⟩ on |+⟩ and |-⟩:
        a = <+|v⟩ = <0|H'|v⟩ = a<0|H'H|0⟩ = a
        b = <-|v⟩ = <1|H'|v⟩ = a<1|H'H|1⟩ = b
        """
        qubit_x_basis = H @ qubit
        probs = qubit_x_basis.conj() * qubit_x_basis
        return (probs[0] - probs[1]).real

    def get_y():
        """
        Write the qubit as a linear combination in the basis |↺⟩, |↻⟩:
        |v⟩ = a|↻⟩ + b|↺⟩ = a(SH|0⟩) + b(SH|1⟩)
        Project |v⟩ on |↺⟩ and |↻⟩:
        a = <↻|v⟩ = <0|H'S'|v⟩ = a<0|H'S'SH|0⟩ = a
        b = <↺|v⟩ = <1|H'S'|v⟩ = a<1|H'S'SH|1⟩ = b
        """
        qubit_y_basis = H @ Sdg @ qubit
        probs = qubit_y_basis.conj() * qubit_y_basis
        return (probs[0] - probs[1]).real

    def get_z():
        qubit_z_basis = qubit
        probs = qubit_z_basis.conj() * qubit_z_basis
        return (probs[0] - probs[1]).real

    return get_x(), get_y(), get_z()


def draw_sphere(ax, n=250):
    u, v = np.mgrid[0:2 * np.pi:n * 1.0j, 0:np.pi:(n / 2) * 1.0j]
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)
    ax.plot_wireframe(x, y, z, color="k", alpha=.01, rcount=100, ccount=100)
    ax.grid(False)


def plot_qubit(plot, qubit, color, label=None):
    x, y, z = get_bloch_coords(qubit)
    plot.quiver(0, 0, 0, x, y, z, length=1, color=color,
                arrow_length_ratio=0.1, label=label)


def plot_bloch_sphere(plot):
    draw_sphere(plot)

    plot.set_xlim([-1, 1])
    plot.set_ylim([-1, 1])
    plot.set_zlim([-1, 1])

    plot.view_init(azim=20)
    return plot
