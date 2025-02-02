from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit


import sys
sys.path.append('../../../')
from AutomatskiKomencoQiskit import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
# No need for transpiling with any transpiler
backend = AutomatskiKomencoQiskit(host="103.212.120.18", port=80)



q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')

def firstBellState():
    circuit = QuantumCircuit(q,c)

    circuit.h(q[0]) # Hadamard gate 
    circuit.cx(q[0],q[1]) # CNOT gate
    circuit.measure(q,c) # Qubit Measurment

    print(circuit)

    result_sim = backend.run(circuit, repetitions=8192, topK=20)
    counts = result_sim.get_counts(None)

    print(counts)

def secondBellState():
    circuit = QuantumCircuit(q,c)

    circuit.x(q[0]) # Pauli-X gate 
    circuit.h(q[0]) # Hadamard gate 
    circuit.cx(q[0],q[1]) # CNOT gate
    circuit.measure(q,c) # Qubit Measurment

    print(circuit)

    result_sim = backend.run(circuit, repetitions=8192, topK=20)
    counts = result_sim.get_counts(None)

    print(counts)

def thirdBellState():
    circuit = QuantumCircuit(q,c)

    circuit.x(q[1]) # Pauli-X gate 
    circuit.h(q[0]) # Hadamard gate 
    circuit.cx(q[0],q[1]) # CNOT gate
    circuit.measure(q,c) # Qubit Measurment

    print(circuit)

    result_sim = backend.run(circuit, repetitions=8192, topK=20)
    counts = result_sim.get_counts(None)

    print(counts)

def fourthBellState():
    circuit = QuantumCircuit(q,c)

    circuit.x(q[1]) # Pauli-X gate 
    circuit.h(q[0]) # Hadamard gate
    circuit.z(q[0]) # Pauli-Z gate
    circuit.z(q[1]) # Pauli-Z  gate 
    circuit.cx(q[0],q[1]) # CNOT gate
    circuit.measure(q,c) # Qubit Measurment

    print(circuit)

    result_sim = backend.run(circuit, repetitions=8192, topK=20)
    counts = result_sim.get_counts(None)

    print(counts)

print("Creating first Bell State:\n")
firstBellState()
print("\nCreating second Bell State:\n")
secondBellState()
print("\nCreating third Bell State:\n")
thirdBellState()
print("\nCreating fourth Bell State:\n")
fourthBellState()
