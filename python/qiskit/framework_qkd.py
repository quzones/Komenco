from framework.Communication import *

import sys
sys.path.append('../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

n = 10
interception = True
play = True

quantum_key_distribution_circuit = quantum_key_distribution(backend, n, [interception, play])

decomposed_circuit = decomposer(quantum_key_distribution_circuit, 1)# Note the 1. We are decomposing sub-circuits
decomposed_circuit.draw("mpl")
plt.show()



qc = decomposed_circuit # Automatski Backends can only run fully decomposed circuits. They cannot execute circuits with sub-circuits 
shots = 1024
optimization_level = 0
seed = None
show_plot = True
show_counts = False

sorted_counts, raw_counts = run_ideal_simulation(backend, qc, shots, optimization_level, seed, show_plot, show_counts)