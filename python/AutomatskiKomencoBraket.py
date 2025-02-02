from braket.tasks.gate_model_quantum_task_result import GateModelQuantumTaskResult
from braket.circuits import Circuit
from braket.task_result import (
    AdditionalMetadata,
    GateModelTaskResult,
    ResultTypeValue,
    TaskMetadata,
)
from collections import Counter
import requests
import numpy as np
import uuid
import datetime

    
class AutomatskiKomencoBraket:
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.gateMap = {}
        
        self.gateMap["cu1"]="cp"
        self.gateMap["cnot"]="cx"
        self.gateMap["phase"] = "p"
        self.gateMap["cphase"] = "cp"
        self.gateMap["ccphase"] = "ccp"
        self.gateMap["mcphase"] = "mcp"
        self.gateMap["toffoli"] = "ccx"
        self.gateMap["fredkin"] = "cswap"
        self.gateMap["cxp"] = "cnotp"
        self.gateMap["ccxp"] = "ccnotp"


        self.qubitsToIndex = {}
        self.indexToQubits = {}
        self.count = 0
        
    def run(self, circuit, repetitions=1000, topK=20):
        tstart = datetime.datetime.now()
        
        body = self.serialize_circuit(circuit, topK)
        measured_qubits = body['measurements']
        response = requests.post(f'http://{self.host}:{self.port}/api/komenco', json=body)
        response.close() #bug fix - too many connections open
        struct = response.json()
        
        tend = datetime.datetime.now()
        execution_time = (tend - tstart).microseconds
        print(f"Time Taken {(tend - tstart)}")
        
        cannotProceed = None
        try:
            if struct["error"] :
                print(struct["error"])
                cannotProceed = True
                raise Exception(struct["error"])
        except Exception as e:
            if cannotProceed:
                raise e            
            pass 
        
        
        
        return self.deserialize_result(struct, measured_qubits, repetitions, execution_time)

    def serialize_circuit(self, circuit, topK):
        # Extract the number of qubits
        num_qubits = circuit.qubit_count
        
        operations = []
        measurements = []

        for instruction in circuit.instructions:
            gate = instruction.operator.name.lower() #the server uses lowercase gate names 

            print(gate) 
            #we need to map some gate naming conventions to make sure there are no errors
            if gate in self.gateMap:
                gate = self.gateMap[gate]

            params = instruction.operator.parameters if hasattr(instruction.operator, 'parameters') else []    
            qubits = []
            for target in instruction.target:
                qubits.append(
                    self.index(target))
                    
            if gate == 'measure':
                for q in qubits:
                    measurements.append(q)
            elif gate in ['barrier']:
                continue 
            elif gate in ['delay','initialize','reset','store']:
                raise(Exception(f"gate or operation: '{gate}' is not supported by Komenco yet"))                
            else:
                operations.append({"gate": gate, "params": params, "qubits": qubits})
        
        print("Executing Quantum Circuit With...")
        print(f"{num_qubits} Qubits And ...")
        print(f"{len(operations)} Gates")
        
        if len(measurements) == 0:
            raise(Exception("There are no measurements done at the end of the circuit."))        
                
        return { "num_qubits": num_qubits, "operations": operations, "measurements": measurements, "topK": topK}    

    @staticmethod
    def deserialize_result(response_data, measured_qubits, repetitions, execution_time):
        measurements_strings = response_data['measurements']
        
        # Build counts and probabilities
        counts = Counter()
        probabilities = {}
        measurements = []

        for key_original, value in measurements_strings.items():
            count = round(value * repetitions)
            counts[key_original] = count
            probabilities[key_original] = value

        # Convert measurements to numpy array
        for key, count in counts.items():
            bitstring = [int(bit) for bit in key]
            measurements.extend([bitstring] * count)
        
        measurements_array = np.array(measurements)

        # Create TaskMetadata
        task_metadata = TaskMetadata(
            braketSchemaHeader={"name": "braket.task_result.task_metadata", "version": "1"},
            id=str(uuid.uuid4()),
            shots=repetitions,
            deviceId='komenco',
            createdAt=None,
            endedAt=None,
            status=None,
            failureReason=None
        )

        # Create GateModelQuantumTaskResult
        result = GateModelQuantumTaskResult(
            task_metadata=task_metadata,
            additional_metadata=None,
            result_types=[],
            values=[],
            measurements=measurements_array,
            measured_qubits=measured_qubits,
            measurement_counts=counts,
            measurement_probabilities=probabilities,
            measurements_copied_from_device=True,
            measurement_counts_copied_from_device=False,
            measurement_probabilities_copied_from_device=False,
            _result_types_indices={}
        )

        return result

    def index(self, qubit):
        if qubit in self.qubitsToIndex:
            return self.qubitsToIndex[qubit]
        else:
            self.qubitsToIndex[qubit] = self.count
            self.indexToQubits[self.count] = qubit
            self.count = self.count + 1
            return self.count - 1    