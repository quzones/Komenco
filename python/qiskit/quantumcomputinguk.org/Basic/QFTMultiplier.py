from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit
from qiskit.circuit.library import RGQFTMultiplier

def decomposer(circ, level=1):
    # decompose the circuit to see the basis gates
    # level = how many times to decompose
    
    decomposed_circ = circ
    
    for i in range(level):
        decomposed_circ = decomposed_circ.decompose()
        
    return decomposed_circ

import sys
sys.path.append('../../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)

q = QuantumRegister(8,'q')
c = ClassicalRegister(4,'c')

circuit = QuantumCircuit(q,c)

# Operand A = 10 (2)

circuit.x(q[1])

# Operand B = 11 (3)
circuit.x(q[2])
circuit.x(q[3])

circuit1 = RGQFTMultiplier(num_state_qubits=2, num_result_qubits=4)
circuit = circuit.compose(circuit1)

circuit.measure(q[4],c[0])
circuit.measure(q[5],c[1])
circuit.measure(q[6],c[2])
circuit.measure(q[7],c[3])

print(circuit)

decomposed_circuit = decomposer(circuit, 1)


result_sim = backend.run(decomposed_circuit, repetitions=8192, topK=20)
counts = result_sim.get_counts(None)
print('2*3')
print('---')
print(counts)



