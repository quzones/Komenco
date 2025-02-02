from framework.Variational import *

n = 4
repeat_f = 1
repeat_v = 1
parameters = 'random'

vqc_qc = vqc(n, [repeat_f, repeat_v, parameters])

decomposed_circuit = decomposer(vqc_qc, 2)
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