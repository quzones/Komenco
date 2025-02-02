from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

import sys
sys.path.append('../../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)


q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')

circuit = QuantumCircuit(q,c)
circuit.x(q[0]) # Pauli x gate applied to first qubit 
circuit.cx(q[0],q[1]) # CNOT applied to both qubits 
circuit.measure(q,c) # Qubits states are measured 


                               
print('Executing Job...')
print('')                   
result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)

print('RESULT: ',counts)
print('')
print('Press any key to close')
input()