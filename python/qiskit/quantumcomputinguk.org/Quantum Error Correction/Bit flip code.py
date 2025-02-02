
print('\nPhase Flip Code')
print('----------------')

from qiskit import QuantumRegister
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit

import sys
sys.path.append('../../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

q = QuantumRegister(3,'q')
c = ClassicalRegister(1,'c')

circuit = QuantumCircuit(q,c)

circuit.cx(q[0],q[1])
circuit.cx(q[0],q[2])
circuit.h(q[0])
circuit.h(q[1])
circuit.h(q[2]) 
circuit.z(q[0]) #Add this to simulate a phase flip error
circuit.h(q[0])
circuit.h(q[1])
circuit.h(q[2])
circuit.cx(q[0],q[1])
circuit.cx(q[0],q[2])
circuit.ccx(q[2],q[1],q[0])
circuit.measure(q[0],c[0])

result_sim = backend.run(circuit, repetitions=8192, topK=20)
counts = result_sim.get_counts(None)

print("\nPhase flip code with error")
print("----------------------")
print(counts)
input()




