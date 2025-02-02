from framework.QFT import *

N = 6 #[6, 15, 21, 35, 39, 51, 55, 57, 65, 69, 77, 85, 87, 91, 93, 95, 105, 111, 115, 119, 123]
random = True

shor_qc = shor(N, [random])

decomposed_circuit = decomposer(shor_qc, 1) # Note the 1. We are decomposing sub-circuits
#decomposed_circuit.draw("mpl")
#plt.show()


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