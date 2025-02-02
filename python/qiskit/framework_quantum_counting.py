from framework.Search import *

n = 4
print_oracle = True

quantum_counting_qc = quantum_counting(n, [print_oracle])

decomposed_circuit = decomposer(quantum_counting_qc, 1)
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
calculate_M(raw_counts, n)
# display(sorted_counts['0010'])