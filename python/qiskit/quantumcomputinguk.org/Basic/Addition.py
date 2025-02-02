print('\n Quantum Full Adder')
print('---------------------')
from qiskit import QuantumRegister
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit

import sys
sys.path.append('../../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)


######## A ###########################
q = QuantumRegister(5,'q')
c = ClassicalRegister(2,'c')
circuit = QuantumCircuit(q,c)
circuit.x(q[0])
circuit.cx(q[0],q[3])
circuit.cx(q[1],q[3])
circuit.cx(q[2],q[3])
circuit.ccx(q[0],q[1],q[4])
circuit.ccx(q[0],q[2],q[4])
circuit.ccx(q[1],q[2],q[4])
circuit.measure(q[3],c[0])
circuit.measure(q[4],c[1])
########################################

print('\nExecuting...\n')
print('\nA\n')
result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)
print('RESULT: ',counts,'\n')
######## B ###########################
q = QuantumRegister(5,'q')
c = ClassicalRegister(2,'c')
circuit = QuantumCircuit(q,c)
circuit.x(q[1])
circuit.cx(q[0],q[3])
circuit.cx(q[1],q[3])
circuit.cx(q[2],q[3])
circuit.ccx(q[0],q[1],q[4])
circuit.ccx(q[0],q[2],q[4])
circuit.ccx(q[1],q[2],q[4])
circuit.measure(q[3],c[0])
circuit.measure(q[4],c[1])
######################################

print('\nB\n')
result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)
print('RESULT: ',counts,'\n')
######## A + B ###########################
q = QuantumRegister(5,'q')
c = ClassicalRegister(2,'c')
circuit = QuantumCircuit(q,c)
circuit.x(q[0])
circuit.x(q[1])
circuit.cx(q[0],q[3])
circuit.cx(q[1],q[3])
circuit.cx(q[2],q[3])
circuit.ccx(q[0],q[1],q[4])
circuit.ccx(q[0],q[2],q[4])
circuit.ccx(q[1],q[2],q[4])
circuit.measure(q[3],c[0])
circuit.measure(q[4],c[1])
######################################

print('\nA + B\n')
result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)
print('RESULT: ',counts,'\n')
######## Cin ###########################
q = QuantumRegister(5,'q')
c = ClassicalRegister(2,'c')
circuit = QuantumCircuit(q,c)
circuit.x(q[2])
circuit.cx(q[0],q[3])
circuit.cx(q[1],q[3])
circuit.cx(q[2],q[3])
circuit.ccx(q[0],q[1],q[4])
circuit.ccx(q[0],q[2],q[4])
circuit.ccx(q[1],q[2],q[4])
circuit.measure(q[3],c[0])
circuit.measure(q[4],c[1])
######################################

print('\nCin\n')
result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)
print('RESULT: ',counts,'\n')
######## Cin + A ###########################
q = QuantumRegister(5,'q')
c = ClassicalRegister(2,'c')
circuit = QuantumCircuit(q,c)
circuit.x(q[2])
circuit.x(q[0])
circuit.cx(q[0],q[3])
circuit.cx(q[1],q[3])
circuit.cx(q[2],q[3])
circuit.ccx(q[0],q[1],q[4])
circuit.ccx(q[0],q[2],q[4])
circuit.ccx(q[1],q[2],q[4])
circuit.measure(q[3],c[0])
circuit.measure(q[4],c[1])
######################################

print('\nCin + A\n')
result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)
print('RESULT: ',counts,'\n')
######## Cin + B ###########################
q = QuantumRegister(5,'q')
c = ClassicalRegister(2,'c')
circuit = QuantumCircuit(q,c)
circuit.x(q[2])
circuit.x(q[1])
circuit.cx(q[0],q[3])
circuit.cx(q[1],q[3])
circuit.cx(q[2],q[3])
circuit.ccx(q[0],q[1],q[4])
circuit.ccx(q[0],q[2],q[4])
circuit.ccx(q[1],q[2],q[4])
circuit.measure(q[3],c[0])
circuit.measure(q[4],c[1])
######################################

print('\nCin + B\n')
result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)
print('RESULT: ',counts,'\n')
######## Cin + A + B ###########################
q = QuantumRegister(5,'q')
c = ClassicalRegister(2,'c')
circuit = QuantumCircuit(q,c)
circuit.x(q[2])
circuit.x(q[1])
circuit.x(q[0])
circuit.cx(q[0],q[3])
circuit.cx(q[1],q[3])
circuit.cx(q[2],q[3])
circuit.ccx(q[0],q[1],q[4])
circuit.ccx(q[0],q[2],q[4])
circuit.ccx(q[1],q[2],q[4])
circuit.measure(q[3],c[0])
circuit.measure(q[4],c[1])
######################################

print('\nCin + A + B\n')
result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)
print('RESULT: ',counts,'\n')
print('Press any key to close')
input()