# general imports
import matplotlib.pyplot as plt
# AWS imports: Import Braket SDK modules
from braket.circuits import Circuit
import sys
sys.path.append('../')
from AutomatskiKomencoBraket import *



bell = Circuit().rx(0, 0.789).measure(0)

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