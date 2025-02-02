import requests
import cirq
import numpy as np
import uuid
import datetime

    
class AutomatskiKomencoCirq:
    
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
        
        
    def run(self, circuit, repetitions=1000, topK=20):
        tstart = datetime.datetime.now()
        
        body = self.serialize_circuit(circuit, topK)
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
        
        
        
        return self.deserialize_result(struct, repetitions, execution_time)

    def serialize_circuit(self, circuit, topK):
        # Get all qubits in the circuit and assign a custom index to each
        all_qubits = sorted(circuit.all_qubits())  # This gives a sorted list of qubits
        qubit_index_map = {qubit: idx for idx, qubit in enumerate(all_qubits)}

        # Extract the number of qubits
        num_qubits = len(qubit_index_map)
        

        # Initialize lists to store operations and measurements
        operations = []
        measurements = []

        # Iterate through the circuit to extract information
        for moment in circuit:
            for op in moment.operations:
                gate = str(op.gate).split('(')[0].lower()
                
                #we need to map some gate naming conventions to make sure there are no errors
                if gate in self.gateMap:
                    gate = self.gateMap[gate]
                
                qubits = []
                params = []

                # Get the custom index for each qubit
                for q in op.qubits:
                    qubits.append(qubit_index_map[q])

                # Check if the gate has parameters
                if isinstance(op.gate, cirq.EigenGate):
                    params = [op.gate.exponent]

                # Check for measurement gate
                if isinstance(op.gate, cirq.MeasurementGate):
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
    def deserialize_result(response_data, repetitions, execution_time):
        measurementsStrings = response_data['measurements']
        # Initialize an empty list to collect measurement outcomes
        measurement_results = []

        # For each measurement string and its probability
        for bitstring, prob in measurementsStrings.items():
            # Calculate how many times this bitstring should appear
            num_occurrences = int(prob * repetitions)
            
            # Convert the bitstring (e.g., '00', '11') into an array of 0s and 1s
            bit_array = np.array([int(bit) for bit in bitstring[::-1]], dtype=np.int32)
            
            # Append the bitstring multiple times based on its probability
            measurement_results.extend([bit_array] * num_occurrences)
        
        # Convert the list of measurement results into a numpy array
        measurement_results = np.array(measurement_results)

        # Create the result dictionary expected by cirq.ResultDict
        result_dict = {'result': measurement_results}

        # Create a cirq.ResultDict from the result_dict
        return cirq.ResultDict(params=cirq.ParamResolver({}), measurements=result_dict)
 