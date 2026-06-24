# Experiment 03: Bit-Flip Noise Analysis

## Objective

The objective of this experiment is to investigate the effect of bit-flip noise on an entangled Bell State and analyze how increasing error probability influences measurement statistics and quantum state reliability.

This experiment extends the previous depolarizing noise study by examining a structured quantum error channel rather than a fully random noise process. Understanding the behavior of specific error mechanisms is essential for the development of quantum error correction and fault-tolerant quantum computing systems.

---

## Theoretical Background

Quantum computers are highly susceptible to errors caused by imperfect gate operations, environmental interactions, and hardware limitations. One of the simplest and most fundamental quantum error models is the bit-flip error.

A bit-flip error is represented by the Pauli-X operator:

```text
X|0⟩ = |1⟩
X|1⟩ = |0⟩
```

which is analogous to a classical binary error where a bit changes from 0 to 1 or from 1 to 0.

Unlike depolarizing noise, which introduces random errors that affect the quantum state in multiple ways, bit-flip noise produces a specific and predictable transformation of the qubit state. Because of this structured behavior, bit-flip errors are commonly used as introductory examples in quantum error correction theory.

The Bell State used in this experiment is:

```text
(|00⟩ + |11⟩)/√2
```

This state is maximally entangled and exhibits perfect correlations between the two qubits. Any deviation from the expected measurement outcomes can therefore be attributed to the presence of noise.

---

## Experimental Methodology

### Bell State Preparation

The Bell State was generated using the following quantum circuit:

1. Apply a Hadamard gate to qubit 0.
2. Apply a Controlled-NOT (CNOT) gate with qubit 0 as the control and qubit 1 as the target.
3. Measure both qubits in the computational basis.

In the absence of noise, the expected measurement outcomes are:

```text
00 ≈ 50%
11 ≈ 50%
```

with negligible probabilities for the states:

```text
01
10
```

### Bit-Flip Noise Model

A bit-flip noise model was implemented using Qiskit Aer. The probability of a bit-flip error occurring was varied between:

```text
p = 0.00 to p = 0.30
```

For each value of p:

1. The Bell State circuit was simulated.
2. The noise model was applied.
3. Measurement outcomes were collected.
4. Outcome probabilities were calculated and analyzed.

Each simulation was executed using a finite number of measurement shots to estimate the probability distribution of the resulting quantum states.

---

## Results

### Histogram Analysis

The histogram comparison between the ideal and noisy Bell States revealed the appearance of additional measurement outcomes as the bit-flip probability increased.

While the ideal Bell State produced only the expected states:

```text
00
11
```

the noisy simulations generated:

```text
01
10
```

indicating the presence of bit-flip errors.

### Probability Distribution Analysis

The probability distribution plot demonstrated a systematic redistribution of probability mass as the error probability increased.

The probabilities associated with the ideal Bell State outcomes decreased steadily with increasing noise strength, while the probabilities of the error states increased correspondingly.

This behavior reflects the structured nature of bit-flip noise and is consistent with theoretical expectations.

---

## Discussion

The results illustrate a key distinction between depolarizing noise and bit-flip noise.

In the depolarizing noise experiment, quantum information was gradually randomized, leading to a general degradation of state quality. In contrast, bit-flip noise produced identifiable and predictable error patterns.

The emergence of the states 01 and 10 demonstrates that bit-flip errors introduce specific transitions between computational basis states rather than randomly perturbing the entire quantum state.

This distinction is particularly important in the context of quantum error correction. Because bit-flip errors possess a well-defined structure, they can be detected and corrected using appropriate encoding and syndrome measurement techniques.

The experiment therefore provides an important conceptual bridge between noise characterization and fault-tolerant quantum computation.

---

## Observations

* The ideal Bell State produced only the outcomes 00 and 11.
* Increasing bit-flip probability reduced the likelihood of observing the correct Bell State outcomes.
* Error states 01 and 10 emerged and became increasingly probable as noise strength increased.
* The observed behavior matched the theoretical predictions of the bit-flip noise model.
* The resulting error patterns were structured and predictable rather than random.
* The experiment demonstrated how specific quantum error channels affect entangled quantum states.

---

## Conclusion

This experiment successfully investigated the impact of bit-flip noise on an entangled Bell State.

The results showed that increasing bit-flip probability causes a gradual transfer of probability from the correct Bell State outcomes to erroneous measurement states. Unlike depolarizing noise, which introduces largely random disturbances, bit-flip noise generates structured error patterns that can be directly observed in measurement statistics.

These findings highlight the importance of understanding individual quantum error mechanisms and provide motivation for the development of quantum error correction techniques capable of identifying and correcting such errors.

This experiment represents an important step in the broader Quantum Noise Analysis and Error Mitigation project and establishes a foundation for future investigations involving phase-flip noise, amplitude damping, quantum state fidelity, and error mitigation strategies.
