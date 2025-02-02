print('\nGrovers Algorithm')
print('------------------\n')

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import math

import sys
sys.path.append('../../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)
        
pi = math.pi
q = QuantumRegister(4,'q')
c = ClassicalRegister(4,'c')
qc = QuantumCircuit(q,c)

print('\nInitialising Circuit...\n')

### Initialisation ###

qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.h(q[3])

print('\nPreparing Oracle circuit....\n')

### 0000 Oracle ###

qc.x(q[0])
qc.x(q[1])
qc.x(q[2])
qc.x(q[3])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[0])
qc.x(q[1])
qc.x(q[2])
qc.x(q[3])

'''
### 0001 Oracle ###

qc.x(q[1])
qc.x(q[2])
qc.x(q[3])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[1])
qc.x(q[2])
qc.x(q[3])
'''

'''
### 0010 Oracle ###

qc.x(q[0])
qc.x(q[2])
qc.x(q[3])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[0])
qc.x(q[2])
qc.x(q[3])
'''

'''
### 0011 Oracle ###

qc.x(q[2])
qc.x(q[3])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[2])
qc.x(q[3])
'''

'''
### 0100 Oracle ###

qc.x(q[0])
qc.x(q[1])
qc.x(q[3])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[0])
qc.x(q[1])
qc.x(q[3])
'''

'''
### 0101 Oracle ###

qc.x(q[1])
qc.x(q[3])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[1])
qc.x(q[3])
'''

'''
### 0110 Oracle ###

qc.x(q[0])
qc.x(q[3])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[0])
qc.x(q[3])
'''

'''
### 0111 Oracle ###

qc.x(q[3])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[3])
'''

'''
### 1000 Oracle ###

qc.x(q[0])
qc.x(q[1])
qc.x(q[2])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[0])
qc.x(q[1])
qc.x(q[2])
'''

'''
### 1001 Oracle ###

qc.x(q[1])
qc.x(q[2])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[1])
qc.x(q[2])
'''

'''
### 1010 Oracle ###

qc.x(q[0])
qc.x(q[2])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[0])
qc.x(q[2])
'''

'''
### 1011 Oracle ###

qc.x(q[3])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[3])
'''

'''
### 1100 Oracle ###

qc.x(q[0])
qc.x(q[1])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[0])
qc.x(q[1])
'''

'''
### 1101 Oracle ###

qc.x(q[1])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[1])
'''

'''
### 1110 Oracle ###

qc.x(q[0])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[0])
'''

'''
###1111 Oracle###

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
'''

print('\nPreparing Amplification circuit....\n')
#### Amplification ####

qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.h(q[3])
qc.x(q[0])
qc.x(q[1])
qc.x(q[2])
qc.x(q[3])

qc.cp(pi/4, q[0], q[3])
qc.cx(q[0], q[1])
qc.cp(-pi/4, q[1], q[3])
qc.cx(q[0], q[1])
qc.cp(pi/4, q[1], q[3])
qc.cx(q[1], q[2])
qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])
qc.cx(q[1], q[2])

qc.cp(-pi/4, q[2], q[3])
qc.cx(q[0], q[2])
qc.cp(pi/4, q[2], q[3])

qc.x(q[0])
qc.x(q[1])
qc.x(q[2])
qc.x(q[3])
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.h(q[3])

### Measurment ###
qc.barrier(q)
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])
qc.measure(q[3], c[3])


print('\nExecuting job....\n')
result_sim = backend.run(qc, repetitions=1000, topK=20)
counts = result_sim.get_counts(None)

print('RESULT: ',counts,'\n')
print('Press any key to close')
input()