## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

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

## Example 3-3: Phase Kickback
# Set up the program
reg1 = QuantumRegister(2, name='reg1')
reg2 = QuantumRegister(1, name='reg2')
qc = QuantumCircuit(reg1, reg2)

qc.h(reg1)         # put a into reg1 superposition of 0,1,2,3
qc.cp(math.pi/4, reg1[0], reg2)
qc.cp(math.pi/2, reg1[1], reg2)
qc.measure_all()

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

# Run the circuit and get results
result = backend.run(qc, repetitions=1000, topK=20)

counts = result.get_counts(None)
print(counts)

#outputstate = result.get_statevector(qc, decimals=3)
#print(outputstate)
#qc.draw()        # draw the circuit
