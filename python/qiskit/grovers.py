import numpy as np
from qiskit import QuantumCircuit,QuantumRegister, ClassicalRegister
from matplotlib import pyplot as plt
import sys
sys.path.append('../')
from AutomatskiKomencoQiskit import *

#SECRET is 11

# https://github.com/Qiskit/textbook/blob/main/notebooks/ch-algorithms/grover.ipynb
n = 2
grover_circuit = QuantumCircuit(n,n)

for q in range(n):
    grover_circuit.h(q)

grover_circuit.cz(0,1) # Oracle

# Diffusion operator (U_s)
grover_circuit.h([0,1])
grover_circuit.z([0,1])
grover_circuit.cz(0,1)
grover_circuit.h([0,1])

grover_circuit.draw('mpl')
plt.show()    

grover_circuit.barrier(range(n))
# map the quantum measurement to the classical bits
grover_circuit.measure(range(n), range(n))

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

# Run the circuit and get results
result = backend.run(grover_circuit, repetitions=1000, topK=20)

# Get the counts (how many times each state was measured)
counts = result.get_counts()

# Print the result and plot the histogram
print("Recovered Secret:", max(counts, key=counts.get))
from qiskit.visualization import plot_histogram
plot_histogram(counts)
plt.show()

