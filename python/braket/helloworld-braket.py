# general imports
import matplotlib.pyplot as plt
# AWS imports: Import Braket SDK modules
from braket.circuits import Circuit
import sys
sys.path.append('../')
from AutomatskiKomencoBraket import *



# build a Bell state with two qubits. Here 'cnot(control=0, target=1)' can be simplified as 'cnot(0,1)'
bell = Circuit().h(0).cnot(control=0, target=1).measure(0).measure(1)

# set up device
device = AutomatskiKomencoBraket(host="103.212.120.18", port=80)

# run circuit
result = device.run(bell, repetitions=1000)
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