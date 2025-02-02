import qiskit.qasm2
from qiskit import QuantumCircuit
import json

def generateQiskitCircuit(quantum_program):
    json_data = json.loads(quantum_program)    
    qasm_string = json_data["transpiled_circuit"]["outputs"]["qasm"]
    circuit = qiskit.qasm2.loads(qasm_string)
    circuit.measure_all()
    
    return circuit 