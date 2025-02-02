print('\n Superdense Coding')
print('--------------------------\n')

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

import sys
sys.path.append('../../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')


#################### 00 ###########################
circuit = QuantumCircuit(q,c) 

circuit.h(q[0]) # Hadamard gate applied to q0
circuit.cx(q[0],q[1]) # CNOT gate applied
circuit.cx(q[0],q[1]) 
circuit.h(q[0])  

circuit.measure(q,c) # Qubits measured    
                               
print('Executing Job...\n')               
result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)

print('RESULT: ',counts,'\n')

#################### 10 ###########################
circuit = QuantumCircuit(q,c) 

circuit.h(q[0])
circuit.cx(q[0],q[1])
circuit.x(q[0]) # X-gate applied
circuit.cx(q[0],q[1])
circuit.h(q[0])

circuit.measure(q,c)
                               
print('Executing Job...\n')                  
result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)

print('RESULT: ',counts,'\n')

#################### 01 ###########################
circuit = QuantumCircuit(q,c) 

circuit.h(q[0])
circuit.cx(q[0],q[1])
circuit.z(q[0]) # Z-gate applied to q0 
circuit.cx(q[0],q[1])
circuit.h(q[0])

circuit.measure(q,c)
                               
print('Executing Job...\n')               
result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)

print('RESULT: ',counts,'\n')

#################### 11 ###########################
circuit = QuantumCircuit(q,c) 

circuit.h(q[0])
circuit.cx(q[0],q[1])
circuit.z(q[0]) # Z-gate applied 
circuit.x(q[0]) # X-gate applied 
circuit.cx(q[0],q[1])
circuit.h(q[0])

circuit.measure(q,c)
                               
print('Executing Job...\n')               
result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)

print('RESULT: ',counts,'\n')
print('Press any key to close')
input()