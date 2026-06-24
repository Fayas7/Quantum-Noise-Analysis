# Experiment 02: Depolarizing Noise Analysis

## Objective

The objective of this experiment is to investigate the impact of depolarizing noise on an entangled Bell State and evaluate how increasing noise strength affects quantum state reliability.

---

## Background

Quantum computers are highly susceptible to noise arising from imperfect gate operations and interactions with the environment.

Depolarizing noise is a widely used noise model in quantum computing. With a given probability, the quantum state is replaced by a random mixed state, causing loss of information and degradation of quantum correlations.

Because Bell States are maximally entangled, they provide an excellent benchmark for studying the effects of noise on quantum information.

---

## Methodology

### Bell State Preparation

A Bell State was generated using:

1. Hadamard gate on qubit 0
2. CNOT gate between qubits 0 and 1

Resulting state:

(|00⟩ + |11⟩)/√2

### Noise Model

A depolarizing noise model was implemented using Qiskit Aer.

Noise was applied to:

* Single-qubit gates
* Two-qubit gates

### Noise Sweep

The depolarizing probability was varied between:

0.00 and 0.30

For each probability value:

1. The noisy circuit was simulated.
2. Measurement counts were collected.
3. Bell State survival probability was calculated.

---

## Results

### Histogram Comparison

The noisy Bell State produced additional measurement outcomes:

* 01
* 10

which are absent in the ideal Bell State.

This indicates that depolarizing noise introduces errors into the entangled state.

### Survival Probability Analysis

The Bell State survival probability decreased as depolarizing probability increased.

The relationship demonstrated a clear degradation of quantum information under increasing noise strength.

---

## Observations

* Bell State performance was highest in the absence of noise.
* Increasing depolarizing probability reduced measurement reliability.
* Noise generated incorrect basis states.
* Entanglement quality degraded as noise strength increased.
* The overall trend confirmed the destructive effect of depolarizing noise on quantum states.

---

## Conclusion

This experiment successfully demonstrated the impact of depolarizing noise on an entangled Bell State.

The results showed a clear reduction in Bell State survival probability as noise strength increased, highlighting the importance of noise mitigation and quantum error correction techniques for practical quantum computing systems.

The experiment serves as the first quantitative noise characterization study within the Quantum Noise Analysis and Error Mitigation project.
