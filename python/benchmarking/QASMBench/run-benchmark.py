import qiskit.qasm2
import numpy as np
from qiskit import QuantumCircuit
from matplotlib import pyplot as plt
import sys
sys.path.append('../../')
from AutomatskiKomencoQiskit import *

filename = "./small/grover_n2/grover_n2.qasm"

circuit = qiskit.qasm2.load(filename)
circuit.draw("mpl")
plt.savefig('benchmark-circuit.png', bbox_inches='tight')
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
plt.savefig('benchmark-output.png', bbox_inches='tight')
plt.show()