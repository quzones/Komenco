## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io
##
## A complete notebook of all Chapter 6 samples (including this one) can be found at
##  https://github.com/oreilly-qc/oreilly-qc.github.io/tree/master/samples/Qiskit

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

## Example 7-8: QFT rotating phases

# Set up the program
signal = QuantumRegister(4, name='signal')
qc = QuantumCircuit(signal)

def main():

    ## Rotate kth state in register by k times 20 degrees
    phi = 20;

    ## First HAD so that we can see the result for all k values at once
    qc.h(signal);

    ## Apply 2^k phase operations to kth qubit
    for i in range(4):
        val = 1 << i
        for j in range(val):
            qc.rz(math.radians(phi), signal[i]);

def QFT(qreg):
    ## This QFT implementation is adapted from IBM's sample:
    ##   https://github.com/Qiskit/qiskit-terra/blob/master/examples/python/qft.py
    ## ...with a few adjustments to match the book QFT implementation exactly
    n = len(qreg)
    for j in range(n):
        for k in range(j):
            qc.cp(-math.pi/float(2**(j-k)), qreg[n-j-1], qreg[n-k-1])
        qc.h(qreg[n-j-1])
    # Now finish the QFT by reversing the order of the qubits
    for j in range(n//2):
        qc.swap(qreg[j], qreg[n-j-1])

main()

qc.measure_all()

## That's the program. Everything below runs and draws it.

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

# Run the circuit and get results
result = backend.run(qc, repetitions=1000, topK=20)

counts = result.get_counts(None)
print(counts)

#outputstate = result.get_statevector(qc, decimals=3)
#for i,amp in enumerate(outputstate):
#    if abs(amp) > 0.000001:
#        prob = abs(amp) * abs(amp)
#        print('|{}> {} probability = {}%'.format(i, amp, round(prob * 100, 5)))
#qc.draw()        # draw the circuit
