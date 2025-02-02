import numpy as np
from qiskit import QuantumCircuit
from matplotlib import pyplot as plt
import sys
sys.path.append('../')
from AutomatskiKomencoQiskit import *
from math import pi

def qft_circuit(n):
    qc = QuantumCircuit(n,n)
    
    # Apply the QFT
    for qubit in range(n):
        # Apply the Hadamard gate
        qc.h(qubit)
        
        # Apply the controlled phase shift gates
        for other_qubit in range(qubit + 1, n):
            angle = pi / (2 ** (other_qubit - qubit))
            qc.cp(angle, other_qubit, qubit)
    
    # Swap the qubits to reverse the order
    for i in range(n // 2):
        qc.swap(i, n - i - 1)
    
    return qc

# Example usage: create a QFT circuit for n=3 qubits
n = 3
qc = qft_circuit(n)
qc.draw('mpl')
plt.show()

qc.barrier(range(n))
# map the quantum measurement to the classical bits
qc.measure(range(n), range(n))



# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

# Run the circuit and get results
result_sim = backend.run(qc, repetitions=1000, topK=20)


#import pprint
#pprint.pp(result_sim)



counts = result_sim.get_counts(None)
print(counts)

from qiskit.visualization import plot_histogram
plot_histogram(counts)
plt.show()