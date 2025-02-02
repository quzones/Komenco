import matplotlib.pyplot as plt 
import sys
sys.path.append('../')
from AutomatskiKomencoNative import *
import numpy as np
import random 

seed = 12345
random.seed(seed)
np.random.seed(seed)
#torch.manual_seed(seed) #to be used in pytorch quantum 


totalQubits = 10
qubitsToUseForRandomCircuit = [ q for q in range(totalQubits) ]
numberOfOperations = 100

# Create a sample quantum circuit
circuit = QuantumCircuit(totalQubits)
circuit.randomCircuit( numberOfOperations, qubitsToUseForRandomCircuit )
circuit.measure_all()

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
sampler = AutomatskiKomencoNative(host="103.212.120.18", port=80)

# Run the circuit and get results
results = sampler.run(circuit, repetitions=10000, topK=20)
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