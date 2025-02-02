import qiskit.qasm2
import numpy as np
from qiskit import QuantumCircuit
from matplotlib import pyplot as plt
import sys
sys.path.append('../')
from AutomatskiKomencoQiskit import *

'''
//https://docs.quantum.ibm.com/guides/interoperate-qiskit-qasm2
import qiskit.qasm2
 
qiskit.qasm2.load(filename, include_path=('.',), include_input_directory='append', custom_instructions=(), custom_classical=(), strict=False)
qiskit.qasm2.loads(program, include_path=('.',), custom_instructions=(), custom_classical=(), strict=False)
'''
 
program = '''
    OPENQASM 2.0;
    include "qelib1.inc";
    qreg q[2];
    creg c[2];
 
    h q[0];
    cx q[0], q[1];
 
    measure q -> c;
'''
circuit = qiskit.qasm2.loads(program)
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