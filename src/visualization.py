import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

def save_histogram(counts, filename):
    """
    Saves a histogram figure.
    """

    fig = plot_histogram(counts)

    fig.savefig(filename)

    plt.close()