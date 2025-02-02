


# general imports
import matplotlib.pyplot as plt
# AWS imports: Import Braket SDK modules
from braket.circuits import Circuit
import sys
sys.path.append('../')
from AutomatskiKomencoBraket import *

# function to build a GHZ state
def ghz_circuit(n_qubits):
    """
    function to return a GHZ circuit ansatz
    input: number of qubits
    """

    # instantiate circuit object
    circuit = Circuit()
    
    # add Hadamard gate on first qubit
    circuit.h(0)

    # apply series of CNOT gates
    for ii in range(0, n_qubits-1):
        circuit.cnot(control=ii, target=ii+1)

    for ii in range(0, n_qubits):
        circuit.measure(ii)
        
    return circuit
    
# define circuit
n_qubits = 10
ghz = ghz_circuit(n_qubits)

# print circuit
print(ghz)    



# set up device
device = AutomatskiKomencoBraket(host="103.212.120.18", port=80)

# run circuit
result = device.run(ghz, repetitions=1000)
# get measurement shots
counts = result.measurement_counts
# print counts
print(counts)


# plot using Counter
plt.bar(counts.keys(), counts.values());
plt.xlabel('Measurement Outcomes')
plt.ylabel('Counts')
plt.title('Quantum States & Counts Histogram')
plt.xticks(rotation='vertical')  # Rotate labels vertically
plt.show()