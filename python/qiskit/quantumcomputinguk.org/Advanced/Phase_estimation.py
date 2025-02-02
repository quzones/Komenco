from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT
import numpy as np

import sys
sys.path.append('../../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

q = QuantumRegister(4,'q')
c = ClassicalRegister(3,'c')

circuit = QuantumCircuit(q,c)

pi = np.pi

angle = 2*(pi/3)

actual_phase = angle/(2*pi)

#### Controlled unitary operations ####

circuit.h(q[0])
circuit.h(q[1])
circuit.h(q[2])
circuit.x(q[3])

circuit.cp(angle, q[0], q[3]);

circuit.cp(angle, q[1], q[3]);
circuit.cp(angle, q[1], q[3]);

circuit.cp(angle, q[2], q[3]);
circuit.cp(angle, q[2], q[3]);
circuit.cp(angle, q[2], q[3]);
circuit.cp(angle, q[2], q[3]);

circuit.barrier()

#### Inverse QFT ####

circuit.swap(q[0],q[2])
circuit.h(q[0])
circuit.cp(-pi/2, q[0], q[1]);
circuit.h(q[1])
circuit.cp(-pi/4, q[0], q[2]);
circuit.cp(-pi/2, q[1], q[2]);
circuit.h(q[2])
circuit.barrier()

#### Measuring counting qubits ####
circuit.measure(q[0],0)
circuit.measure(q[1],1)
circuit.measure(q[2],2)

result_sim = backend.run(circuit, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)

print('\n')
print("Phase estimation output")
print("-----------------------\n")

a = counts.most_frequent()

print('Most frequent measurement: ',a,'\n')

bin_a = int(a,2) # Converts the binary value to an integer

phase = bin_a/(2**3)# The calculation used to estimate the phase

print('Actual phase is: ',actual_phase)
print('Estimated phase is: ',phase)
input()
