# EXPERIMENT 01

Bell State Generation

Observation:  

The Bell state is created by applying a Hadamard gate to the first qubit followed by a CNOT gate. This produces the entangled state:


$$|\Phi^+\rangle = \frac{1}{\sqrt{2}} \big(|00\rangle + |11\rangle\big) $$

Since the state contains only the basis states ∣00⟩ and ∣11⟩, measurement outcomes are restricted to these two possibilities. The states ∣01⟩ and ∣10⟩ have zero probability amplitude and therefore do not appear in an ideal simulation.

The Bell state is an equal superposition of ∣00⟩ and ∣11⟩. Both states have the same probability amplitude magnitude, resulting in equal measurement probabilities of 50%.

P(00)=P(11)= 0.5

In practice, finite-shot simulations may produce slight deviations from exactly 50% due to statistical fluctuations, but the probabilities approach 50% as the number of shots increases.

What this tells us about Entanglement?:  

The measurement results demonstartes strong correlations between the two qubits. Whenever the first qubit is measured as 0, the second qubit is also measured as 0; similarly, when the first qubit is measured as 1, the second qubit is measured as 1.  
These correlations cannot be explained by treating the qubits as independent systems. Instead, the qubits share a single quantum state, indicating that they are entangled. Entanglement is a fundamental quantum phenomenon in which the state of one qubit is intrinsically related to the state of another, regardless of physical separation.

Interpretation:

This behavior confirms the successfull creation of an entangled bell state. The equal probabilities arise from quantum superposition, while the perfect correlation between qubit measurements is evidemce of entanglement. This experiment serves as the baseline for subsequent noise and error-mitigation analysis.
