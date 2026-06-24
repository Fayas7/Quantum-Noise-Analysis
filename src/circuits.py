from qiskit import QuantumCircuit

def bell_state_circuit(measure=True):
    """
    Creates a Bell State circuit.
    """

    qc = QuantumCircuit(2)

    qc.h(0)
    qc.cx(0, 1)

    if measure:
        qc.measure_all()

    return qc
