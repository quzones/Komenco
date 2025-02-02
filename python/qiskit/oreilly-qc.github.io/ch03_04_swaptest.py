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

## Example 3-4: Swap Test
# Set up the program
input1 = QuantumRegister(1, name='input1')
input2 = QuantumRegister(1, name='input2')
output = QuantumRegister(1, name='output')
output_c = ClassicalRegister(1, name='outputc')
qc = QuantumCircuit(input1, input2, output, output_c)

qc.h(output)
qc.cswap(output, input1, input2)
qc.h(output)
qc.x(output)
qc.measure(output, output_c)

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
