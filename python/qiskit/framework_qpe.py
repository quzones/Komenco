from framework.QFT import *

n = 4
phase_theta = 1/8

qpe_qc = qpe(n, [phase_theta])

decomposed_circuit = decomposer(qpe_qc, 0)
decomposed_circuit.draw("mpl")
plt.show()


import sys
sys.path.append('../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

qc = qpe_qc
shots = 1024
optimization_level = 0
seed = None
show_plot = True
show_counts = False

sorted_counts, raw_counts = run_ideal_simulation(backend, qc, shots, optimization_level, seed, show_plot, show_counts)