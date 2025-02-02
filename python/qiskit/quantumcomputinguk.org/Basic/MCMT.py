from qiskit import QuantumRegister, ClassicalRegister
from qiskit.circuit.library import MCMT
from qiskit import QuantumCircuit
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

q = QuantumRegister(6,'q')
c = ClassicalRegister(2,'c')

circuit = QuantumCircuit(q,c)

#### This circuit shows how to implement a controlled hadamard gate ####
#### consisting of 4 control qubits and 2 target qubits ####

circuit.x(q[0])
circuit.x(q[1])
circuit.x(q[2])
circuit.x(q[3])

circuit &= MCMT('h',4,2)

circuit.measure(q[4],c[0])
circuit.measure(q[5],c[1])

print(circuit)

decomposed_circuit = decomposer(circuit, 1)


result_sim = backend.run(decomposed_circuit, repetitions=8192, topK=20)
counts = result_sim.get_counts(None)

print(counts)
