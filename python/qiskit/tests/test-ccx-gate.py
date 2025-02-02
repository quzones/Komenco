import numpy as np
from qiskit import QuantumCircuit
from matplotlib import pyplot as plt
import sys
sys.path.append('../../')
from AutomatskiKomencoQiskit import *


# Create a Quantum Circuit acting on a quantum register of three qubits
qc = QuantumCircuit(3,3)

qc.x(0)
qc.x(1)
qc.ccx(0,1,2)

# map the quantum measurement to the classical bits
qc.measure(range(3), range(3))



# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

# Run the circuit and get results
result_sim = backend.run(qc, repetitions=1000, topK=20)


#import pprint
#pprint.pp(result_sim)



counts = result_sim.get_counts(None)
print(counts)

from qiskit.visualization import plot_histogram
plot_histogram(counts)
plt.show()