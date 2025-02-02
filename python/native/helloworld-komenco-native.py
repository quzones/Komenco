import matplotlib.pyplot as plt 
import sys
sys.path.append('../')
from AutomatskiKomencoNative import *

# Create a sample quantum circuit to create a N Qubit GHZ State

numOfQubits = 7
 
circuit = QuantumCircuit(numOfQubits)
circuit.h(0)

for i in range (numOfQubits - 1):
    circuit.cx(i, i + 1);

circuit.measure_all()

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers 
sampler = AutomatskiKomencoNative(host="103.212.120.18", port=80)

# Run the circuit and get results
results = sampler.run(circuit, repetitions=1000, topK=20)
# Extract and count the measurement results
measurements = results['result']
print(measurements)

labels = sorted(measurements.keys())
values = [measurements[label] for label in labels]

plt.bar(labels, values)
plt.xlabel('Measurement Outcomes')
plt.ylabel('Counts')
plt.title('Quantum States & Counts Histogram')
plt.xticks(rotation='vertical')  # Rotate labels vertically
plt.show()
