


from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import MCXGate


def toffoli_general(qr, control, target):
    qr.append(MCXGate(num_ctrl_qubits=len(control)), control + [target])


qr = QuantumCircuit(5)
toffoli_general(qr, [0, 1, 2, 3], 4)
qr.draw('mpl')
