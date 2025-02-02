from qat.lang import Program
from matplotlib import pyplot as plt
import sys
sys.path.append('../')
from AutomatskiKomencoQiskit import *


my_program = Program()
qbits_reg = my_program.qalloc(2)  # Allocate 2 qubits

import numpy as np
from qat.lang import CNOT, H, RZ

H(qbits_reg[0])
CNOT(qbits_reg[0], qbits_reg[1])

qlm_circuit = my_program.to_circ()



#from qat.interop.qiskit import qiskit_to_qlm
#qlm_circuit = qiskit_to_qlm(your_qiskit_circuit)

from qat.interop.qiskit import qlm_to_qiskit
qiskit_circuit = qlm_to_qiskit(qlm_circuit)




# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

# Run the circuit and get results
result_sim = backend.run(qiskit_circuit, repetitions=1000, topK=20)


#import pprint
#pprint.pp(result_sim)



counts = result_sim.get_counts(None)
print(counts)

from qiskit.visualization import plot_histogram
plot_histogram(counts)
plt.show()

