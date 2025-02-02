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

# Example 3-5: Custom conditional-phase
# Set up the program
reg = QuantumRegister(2, name='reg')
qc = QuantumCircuit(reg)

theta = math.pi / 2
qc.h(reg)
qc.rz(theta/2, reg[1])
qc.cx(reg[0], reg[1])
qc.rz(-theta/2, reg[1])
qc.cx(reg[0], reg[1])
qc.rz(-theta/2, reg[0])

qc.barrier()

qc.crz(theta, reg[0], reg[1])
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
