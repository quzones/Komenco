from framework.Variational import *

n = 4
repeat = 1
gates = ['ry', 'rz']
entanglement = 'full' # full, linear, reverse_linear, circular, sca
params = 'random'

vqe_qc = vqe(n, [repeat, gates, entanglement, params])

decomposed_circuit = decomposer(vqe_qc, 1)
decomposed_circuit.draw("mpl")
plt.show()


import sys
sys.path.append('../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

qc = decomposed_circuit
shots = 1024
optimization_level = 0
seed = None
show_plot = True
show_counts = False

sorted_counts, raw_counts = run_ideal_simulation(backend, qc, shots, optimization_level, seed, show_plot, show_counts)