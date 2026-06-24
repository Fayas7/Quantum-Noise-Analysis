from qiskit_aer.noise import NoiseModel
from qiskit_aer.noise import depolarizing_error
from qiskit_aer.noise import pauli_error
def create_bit_flip_noise(probability):

    noise_model = NoiseModel()

    error = pauli_error([
        ('X', probability),
        ('I', 1 - probability)
    ])

    noise_model.add_all_qubit_quantum_error(
        error,
        ['measure']
    )

    return noise_model


def create_depolarizing_noise(probability):
    """
    Creates a depolarizing noise model.
    """

    noise_model = NoiseModel()

    error_1q = depolarizing_error(probability, 1)
    error_2q = depolarizing_error(probability, 2)

    noise_model.add_all_qubit_quantum_error(
        error_1q,
        ["h"]
    )

    noise_model.add_all_qubit_quantum_error(
        error_2q,
        ["cx"]
    )

    return noise_model
