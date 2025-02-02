import classiq 
from classiq import *
classiq.authenticate()

from qiskit import QuantumCircuit
from matplotlib import pyplot as plt
import sys
sys.path.append('../')
from AutomatskiKomencoQiskit import *
from AutomatskiClassiq import *

@qfunc
def main(reg: Output[QArray]):
    allocate(6, reg)
    H(reg[0])
    repeat(
        count=reg.len - 1,
        iteration=lambda index: CX(ctrl=reg[index], target=reg[index + 1]),
    )


quantum_program = synthesize(create_model(main))
show(quantum_program)

circuit = generateQiskitCircuit(quantum_program)

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

# Run the circuit and get results
result_sim = backend.run(circuit, repetitions=1000, topK=20)

counts = result_sim.get_counts(None)
print(counts)

from qiskit.visualization import plot_histogram
plot_histogram(counts)
plt.show()