from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit

import sys
sys.path.append('../../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

q = QuantumRegister(8, 'q')
c = ClassicalRegister(1, 'c')

circuit = QuantumCircuit(q, c)

circuit.x(q[0])
circuit.x(q[1])
circuit.x(q[2])
circuit.x(q[3])

circuit.ccx(q[0], q[1], q[4])
circuit.ccx(q[2], q[4], q[5])
circuit.ccx(q[3], q[5], q[6])

circuit.cx(q[6], q[7]) 

circuit.ccx(q[3], q[5], q[6])
circuit.ccx(q[2], q[4], q[5])
circuit.ccx(q[0], q[1], q[4])

circuit.measure(q[7], c[0])

result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)

print(circuit)
print(counts)
