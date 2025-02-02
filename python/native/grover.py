import matplotlib.pyplot as plt 
import sys
sys.path.append('../')
from AutomatskiKomencoNative import *






# helper function for initialization
def initialize(n_qubits=3):
    """
    function to apply hadamard to all qubits
    """
    # Initialize with superposition
    circuit = QuantumCircuit(3)
    for ii in range(n_qubits):
        circuit.h(ii)

    return circuit 

# helper function for phase oracle
def oracle(circuit, item):
    """
    function to apply oracle for given target item
    """
    # All possible items and their corresponding oracles
    # define oracle dictionary using this CCZ gate
    if item == "000": 
        circuit.x(0)
        circuit.x(1)
        circuit.x(2)
        circuit.ccz(0, 1, 2)
        circuit.x(0)
        circuit.x(1)
        circuit.x(2)
    elif item == "001": 
        circuit.x(0)
        circuit.x(1)
        circuit.ccz(0, 1, 2)
        circuit.x(0)
        circuit.x(1)
    elif item == "010": 
        circuit.x(0)
        circuit.x(2)
        circuit.ccz(0, 1, 2)
        circuit.x(0)
        circuit.x(2)
    elif item == "011": 
        circuit.x(0)
        circuit.ccz(0, 1, 2)
        circuit.x(0)
    elif item == "100": 
        circuit.x(1)
        circuit.x(2)
        circuit.ccz(0, 1, 2)
        circuit.x(1)
        circuit.x(2)
    elif item == "101": 
        circuit.x(1)
        circuit.ccz(0, 1, 2)
        circuit.x(1)
    elif item == "110": 
        circuit.x(2)
        circuit.ccz(0, 1, 2)
        circuit.x(2)
    elif item == "111": 
        circuit.ccz(0, 1, 2)
    else:
        raise(Exception("invalid input"))
        


# helper function for amplification
def amplify(circuit, n_qubits=3):
    """
    function for amplitude amplification
    """
    
    # Amplification
    for ii in range(n_qubits):
        circuit.h(ii)
    oracle(circuit, '000')
    for ii in range(n_qubits):
        circuit.h(ii)



# helper function for grover algorithm
def grover(item, n_qubits=3, n_reps=1):
    """
    function to put together individual modules of Grover algorithm
    """
    # initialize
    grover_circ = initialize()
    # oracle and amplify
    for ii in range(n_reps):
        # oracle
        oracle(grover_circ, item)
        # amplify
        amplify(grover_circ)

    
    grover_circ.measure_all()
    
    return grover_circ

# set up sampler
sampler = AutomatskiKomencoNative(host="103.212.120.18", port=80)
        
# Function to run quantum task, check the status thereof, and collect results
def get_result(circ):
    
    # run circuit
    results = sampler.run(circ, repetitions=1000)

    # get measurement results
    # Extract and count the measurement results
    measurement_counts = results['result']

    # print measurement results
    print('measurement_counts:', measurement_counts)

    labels = sorted(measurement_counts.keys())
    values = [measurement_counts[label] for label in labels]

    plt.bar(labels, values)
    plt.xlabel('Measurement Outcomes')
    plt.ylabel('Counts')
    plt.title('Quantum States & Counts Histogram')
    plt.xticks(rotation='vertical')  # Rotate labels vertically
    plt.show()



# Select item to find. Let's start with '111' for now
item = "101"

# get Grover circuit
circ = grover(item)

# print circuit
print(circ)

# Measurement
get_result(circ)



