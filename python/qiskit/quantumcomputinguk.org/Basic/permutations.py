from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit
from qiskit.circuit.library import Permutation

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


q = QuantumRegister(8, 'q')
c = ClassicalRegister(8, 'c')

########### PERMUTATION WITH PATTERN 7,0,6,1,5,2,4,3 
circuit = QuantumCircuit(q, c)

circuit.x(q[0])
circuit.x(q[1])
circuit.x(q[2])
circuit.x(q[3])

circuit &= Permutation(num_qubits = 8, pattern = [7,0,6,1,5,2,4,3])

circuit.measure(q, c)

decomposed_circuit = decomposer(circuit, 1)


result_sim = backend.run(decomposed_circuit, repetitions=8192, topK=20)
counts = result_sim.get_counts(None)

print(circuit)
print(counts)

####### RANDOM PERMUTATION CIRCUIT 
circuit = QuantumCircuit(q, c)

circuit.x(q[0])
circuit.x(q[1])
circuit.x(q[2])
circuit.x(q[3])

circuit &= Permutation(num_qubits = 8)

circuit.measure(q, c)

decomposed_circuit = decomposer(circuit, 1)


result_sim = backend.run(decomposed_circuit, repetitions=8192, topK=20)
counts = result_sim.get_counts(None)

print(circuit)
print(counts)
