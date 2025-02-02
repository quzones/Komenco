"""Creates and simulates a simple circuit.

=== EXAMPLE OUTPUT ===
Circuit:
(0, 0): ───X**0.5───M('m')───
Results:
m=11000111111011001000
"""

import cirq
import sys
sys.path.append('../')
from AutomatskiKomencoCirq import *

def main():
    # Pick a qubit.
    qubit = cirq.GridQubit(0, 0)

    # Create a circuit
    circuit = cirq.Circuit(
        cirq.H(qubit), cirq.measure(qubit, key='m')  # hadamard.  # Measurement.
    )
    print("Circuit:")
    print(circuit)

    # Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
    simulator = AutomatskiKomencoCirq(host="103.212.120.18", port=80)

    # Run the circuit and get results
    samples = simulator.run(circuit, repetitions=20, topK=20)
    print("Results:")
    print(samples)


if __name__ == '__main__':
    main()
