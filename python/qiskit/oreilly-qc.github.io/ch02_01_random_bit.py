## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

## This sample generates a single random bit.

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import math

import sys
sys.path.append('../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

## Uncomment the next line to see diagrams when running in a notebook
#%matplotlib inline

## Example 2-1: Random bit
# Set up the program
reg = QuantumRegister(1, name='reg')
reg_c = ClassicalRegister(1, name='regc')
qc = QuantumCircuit(reg, reg_c)

#qc.reset(reg)          # write the value 0
qc.h(reg)              # put it into a superposition of 0 and 1
qc.measure(reg, reg_c) # read the result as a digital bit

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

# Run the circuit and get results
result = backend.run(qc, repetitions=1000, topK=20)

counts = result.get_counts(None)
print('counts:',counts)

#outputstate = result.get_statevector(qc, decimals=3)
#print(outputstate)
#qc.draw()        # draw the circuit
