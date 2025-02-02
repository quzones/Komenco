import matplotlib.pyplot as plt 
import sys
sys.path.append('../')
from AutomatskiKomencoNative import *

repetitions = 1000

# Create a sample quantum circuit to create a 3 Qubit GHZ State 
circuit = QuantumCircuit(3)
circuit.h(0)
circuit.cx(0, 1)
circuit.cx(0, 2)
circuit.measure_all()

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers 
sampler = AutomatskiKomencoNative(host="103.212.120.18", port=80)

# Run the circuit and get results
results = sampler.run(circuit, repetitions=repetitions, topK=20)
# Extract and count the measurement results
measurements = results['result']
print(measurements)

labels = [int(label, 2) for label in measurements.keys()]
counts = np.array(list(measurements.values()))
states = np.array(labels).astype(float)
probs = counts / repetitions 
#expectation = np.array([np.sum(np.multiply(probs, states))])
expectation = np.sum(np.multiply(probs, states))

print("Expectation")
print(expectation)
