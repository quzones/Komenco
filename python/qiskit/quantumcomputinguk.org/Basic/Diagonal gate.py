from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit
from qiskit.circuit.library import Diagonal
import numpy as np

pi = np.pi

def decomposer(circ, level=1):
    # decompose the circuit to see the basis gates
    # level = how many times to decompose
    
    decomposed_circ = circ
    
    for i in range(level):
        decomposed_circ = decomposed_circ.decompose()
        
    return decomposed_circ

import sys
sys.path.append('../../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

diagonals = [-1,-1,-1,-1]

q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')

circuit = QuantumCircuit(q,c)

circuit.h(q[0])
circuit.h(q[1])
circuit &= Diagonal(diagonals)
circuit.h(q[0])
circuit.h(q[1])


circuit.measure(q,c) # Qubit Measurment

print(circuit)

decomposed_circuit = decomposer(circuit, 1)


result_sim = backend.run(decomposed_circuit, repetitions=8192, topK=20)
counts = result_sim.get_counts(None)

print(counts)
    
