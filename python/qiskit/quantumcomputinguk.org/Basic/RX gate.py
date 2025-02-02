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

q = QuantumRegister(1,'q')
c = ClassicalRegister(1,'c')

circuit = QuantumCircuit(q,c)

circuit.rx(pi,q[0])
circuit.measure(q,c)

print(circuit)

result_sim = backend.run(circuit, repetitions=8192, topK=20)
counts = result_sim.get_counts(None)

print(counts)
