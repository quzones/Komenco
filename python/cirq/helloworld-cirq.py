import cirq
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from AutomatskiKomencoCirq import *

# Create a sample quantum circuit
qubits = cirq.LineQubit.range(2)
circuit = cirq.Circuit(
    cirq.H(qubits[0]),
    cirq.CNOT(qubits[0], qubits[1]),
    cirq.measure(*qubits, key='result')
)

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers 
simulator = AutomatskiKomencoCirq(host="103.212.120.18", port=80)

# Run the circuit and get results
samples = simulator.run(circuit, repetitions=1000, topK=20)


cirq.plot_state_histogram(samples, plt.subplot())
plt.show()

