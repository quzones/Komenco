from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit
import numpy as np

pi = np.pi

import sys
sys.path.append('../../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

def rz(rotation):
    circuit = QuantumCircuit(q,c)

    circuit.h(q[0]) # Hadamard gate 
    circuit.rz(rotation,q[0]) # RZ gate
    circuit.h(q[0]) # Hadamard gate 
    circuit.measure(q,c) # Qubit Measurment

    print(circuit)

    result_sim = backend.run(circuit, repetitions=8192, topK=20)
    counts = result_sim.get_counts(None)

    print(counts)
    
q = QuantumRegister(1,'q')
c = ClassicalRegister(1,'c')

rotation = 0
rz(rotation)

rotation = pi/2
rz(rotation)

rotation = pi
rz(rotation)
