print('\n Quantum Toffoli Program')
print('--------------------------')
print('Programmed by Macauley Coggins for Quantum Computing UK\n')

from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit

import sys
sys.path.append('../../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

q = QuantumRegister(3,'q')
c = ClassicalRegister(3,'c')

circuit = QuantumCircuit(q,c)
circuit.x(q[0])
circuit.x(q[1])
circuit.ccx(q[0],q[1],q[2])
circuit.measure(q,c)

                             
print('Executing Job...\n')                  
result_sim = backend.run(circuit, repetitions=8192, topK=20)
counts = result_sim.get_counts(None)

print('RESULT: ',counts,'\n')
print('Press any key to close')
input()