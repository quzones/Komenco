import qiskit.qasm3
import numpy as np
from qiskit import QuantumCircuit
from matplotlib import pyplot as plt
import sys
sys.path.append('../')
from AutomatskiKomencoQiskit import *


 
program = """
    // quantum Fourier transform
    include "stdgates.inc";
    qubit[4] q;
    bit[4] c;
    // reset q;
    x q[0];
    x q[2];
    barrier q;
    h q[0];
    cphase(pi / 2) q[1], q[0];
    h q[1];
    cphase(pi / 4) q[2], q[0];
    cphase(pi / 2) q[2], q[1];
    h q[2];
    cphase(pi / 8) q[3], q[0];
    cphase(pi / 4) q[3], q[1];
    cphase(pi / 2) q[3], q[2];
    h q[3];
    c = measure q;
"""
circuit = qiskit.qasm3.loads(program)
circuit.draw("mpl")
plt.show()

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

# Run the circuit and get results
result_sim = backend.run(circuit, repetitions=1000, topK=20)


#import pprint
#pprint.pp(result_sim)



counts = result_sim.get_counts(None)
print(counts)

from qiskit.visualization import plot_histogram
plot_histogram(counts)
plt.show()