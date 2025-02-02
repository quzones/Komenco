from framework.Communication import *

n = 4
state = 'random'

quantum_teleportation_qc = quantum_teleportation(n, [state])

decomposed_circuit = decomposer(quantum_teleportation_qc, 1)# Note the 1. We are decomposing sub-circuits
decomposed_circuit.draw("mpl")
plt.show()


import sys
sys.path.append('../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

qc = decomposed_circuit # Automatski Backends can only run fully decomposed circuits. They cannot execute circuits with sub-circuits 
shots = 1024
optimization_level = 0
seed = None
show_plot = True
show_counts = False

sorted_counts, raw_counts = run_ideal_simulation(backend, qc, shots, optimization_level, seed, show_plot, show_counts)