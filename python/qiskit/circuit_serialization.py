from qiskit.circuit import QuantumCircuit
from qiskit import qpy
 
qc = QuantumCircuit(2, name='Bell', metadata={'test': True})
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
 
with open('bell.qpy', 'wb') as fd:
    qpy.dump(qc, fd)
 
with open('bell.qpy', 'rb') as fd:
    new_qc = qpy.load(fd)[0]
    
# The qiskit.qpy.dump() function also lets you include multiple circuits in a single QPY file:

with open('twenty_bells.qpy', 'wb') as fd:
    qpy.dump([qc] * 20, fd) # storing 20 copies of the Bell circuit into one file

with open('twenty_bells.qpy', 'rb') as fd:
    new_qc = qpy.load(fd)[0]    