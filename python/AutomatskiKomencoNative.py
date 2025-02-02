import requests
import numpy as np
import random
import datetime 

class QuantumCircuit:
    
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.measurements = []
        self.operations = []

    def single(self, cgate, cparams, cqubits):
        if len(cqubits) != 1:
            raise(Exception(f"number of qubits for gate: {cgate} has to be one"))
        for qubit in cqubits:
            if qubit < 0 or qubit >= self.num_qubits:
                raise(Exception(f"invalid qubit: {qubit}"))       
        self.operations.append([cgate, cparams, cqubits])
        
    def double(self, cgate, cparams, cqubits):
        if len(cqubits) != 2:
            raise(Exception(f"number of qubits for gate: {cgate} has to be two"))
        for qubit in cqubits:
            if qubit < 0 or qubit >= self.num_qubits:
                raise(Exception(f"invalid qubit: {qubit}"))       
        self.operations.append([cgate, cparams, cqubits])

    def triple(self, cgate, cparams, cqubits):
        if len(cqubits) != 3:
            raise(Exception(f"number of qubits for gate: {cgate} has to be three"))
        for qubit in cqubits:
            if qubit < 0 or qubit >= self.num_qubits:
                raise(Exception(f"invalid qubit: {qubit}"))       
        self.operations.append([cgate, cparams, cqubits])       

    def multiple(self, cgate, cparams, cqubits):
        for qubit in cqubits:
            if qubit < 0 or qubit >= self.num_qubits:
                raise(Exception(f"invalid qubit: {qubit}"))       
        self.operations.append([cgate, cparams, cqubits])  

        
    def id(self, qubit1):
        self.single("id",[],[qubit1])

    def x(self, qubit1):
        self.single("x",[],[qubit1])

    def y(self, qubit1):
        self.single("y",[],[qubit1])

    def z(self, qubit1):
        self.single("z",[],[qubit1])

    def h(self, qubit1):
        self.single("h",[],[qubit1])

    def s(self, qubit1):
        self.single("s",[],[qubit1])

    def sdg(self, qubit1):
        self.single("sdg",[],[qubit1])

    def t(self, qubit1):
        self.single("t",[],[qubit1])

    def tdg(self, qubit1):
        self.single("tdg",[],[qubit1])

    def rx(self, theta, qubit1):
        self.single("rx",[theta],[qubit1])

    def ry(self, theta, qubit1):
        self.single("ry",[theta],[qubit1])

    def rz(self, theta, qubit1):
        self.single("rz",[theta],[qubit1])

    def u(self, theta, phi, lam, qubit1):
        self.single("u",[theta,phi,lam],[qubit1])

    def u1(self, theta, qubit1):
        self.single("u1",[theta],[qubit1])

    def u2(self, phi, lam, qubit1):
        self.single("u2",[phi,lam],[qubit1])

    def u3(self, theta, phi, lam, qubit1):
        self.single("u3",[theta,phi,lam],[qubit1])

    def sx(self, qubit1):
        self.single("sx",[],[qubit1])

    def sxdg(self, qubit1):
        self.single("sxdg",[],[qubit1])

    def r(self, theta, phi, qubit1):
        self.single("r",[theta, phi],[qubit1])
        
    def cx(self, qubit1, qubit2):
        self.double("cx",[],[qubit1,qubit2])

    def cy(self, qubit1, qubit2):
        self.double("cy",[],[qubit1,qubit2])
        
    def cz(self, qubit1, qubit2):
        self.double("cz",[],[qubit1,qubit2])

    def ch(self, qubit1, qubit2):
        self.double("ch",[],[qubit1,qubit2])

    def ucrx(self, theta, qubit1, qubit2):
        self.double("ucrx",[theta],[qubit1,qubit2])       
        
    def ucry(self, theta, qubit1, qubit2):
        self.double("ucry",[theta],[qubit1,qubit2])  

    def ucrz(self, theta, qubit1, qubit2):
        self.double("ucrz",[theta],[qubit1,qubit2])  

    def crx(self, theta, qubit1, qubit2):
        self.double("crx",[theta],[qubit1,qubit2])       
        
    def cry(self, theta, qubit1, qubit2):
        self.double("cry",[theta],[qubit1,qubit2])  

    def crz(self, theta, qubit1, qubit2):
        self.double("crz",[theta],[qubit1,qubit2])         
        
    def cr(self, theta, phi, lam, qubit1, qubit2):
        self.double("cr",[theta,phi,lam],[qubit1,qubit2]) 

    def cu(self, theta, phi, lam, gamma, qubit1, qubit2):
        self.double("cu1",[theta, phi, lam, gamma],[qubit1,qubit2]) 
        
    def cu1(self, theta, qubit1, qubit2):
        self.double("cu1",[theta],[qubit1,qubit2]) 

    def cu2(self, phi, lam, qubit1, qubit2):
        self.double("cu2",[phi,lam],[qubit1,qubit2]) 

    def cu3(self, theta, phi, lam, qubit1, qubit2):
        self.double("cu3",[theta,phi,lam],[qubit1,qubit2])  

    def dcx(self, qubit1, qubit2):
        self.double("dcx",[],[qubit1,qubit2]) 

    def ecr(self, qubit1, qubit2):
        self.double("ecr",[],[qubit1,qubit2]) 

    def iswap(self, qubit1, qubit2):
        self.double("iswap",[],[qubit1,qubit2])        
        
    def rxx(self, theta, qubit1, qubit2):
        self.double("rxx",[theta],[qubit1,qubit2]) 

    def ryy(self, theta, qubit1, qubit2):
        self.double("ryy",[theta],[qubit1,qubit2]) 

    def rzz(self, theta, qubit1, qubit2):
        self.double("rzz",[theta],[qubit1,qubit2]) 

    def rzx(self, theta, qubit1, qubit2):
        self.double("rzx",[theta],[qubit1,qubit2])        
        
   

   
    def cswap(self, qubit1, qubit2, qubit3):
        self.triple("cswap",[],[qubit1,qubit2,qubit3])
        
    def ccx(self, qubit1, qubit2, qubit3):
        self.triple("ccx",[],[qubit1,qubit2,qubit3])  
        
    def ccy(self, qubit1, qubit2, qubit3):
        self.triple("ccy",[],[qubit1,qubit2,qubit3])  

    def ccz(self, qubit1, qubit2, qubit3):
        self.triple("ccz",[],[qubit1,qubit2,qubit3])          

    def c3x(self, qubits):
        self.multiple("c3x",[],qubits)  

    def c4x(self, qubits):
        self.multiple("c4x",[],qubits)

    def mcx(self, qubits):
        self.multiple("mcx",[],qubits)

    def mcu1(self, theta, qubits):
        self.multiple("mcu1",[theta],qubits)

    def mcu2(self, phi, lam, qubits):
        self.multiple("mcu2",[phi, lam],qubits)

    def mcu3(self, theta, phi, lam, qubits):
        self.multiple("mcu3",[theta, phi, lam],qubits)

    def mcz(self, qubits):
        self.multiple("mcz",[],qubits)
        
    def mcp(self, qubits):
        self.multiple("mcp",[],qubits)

    def mcrx(self, qubits):
        self.multiple("mcrx",[],qubits)

    def mcry(self, qubits):
        self.multiple("mcry",[],qubits)

    def mcrz(self, qubits):
        self.multiple("mcrz",[],qubits)        

    def mct(self, qubits):
        self.multiple("mct",[],qubits) 

    def qft(self, qubits):
        self.multiple("qft",[],qubits)

    def inverse_qft(self, qubits):
        self.multiple("iqft",[],qubits)        

    def swap(self, qubit1, qubit2):
        self.double("swap",[],[qubit1,qubit2])    
    
    def csx(self, qubit1, qubit2):
        self.double("csx",[],[qubit1,qubit2])
        
    def p(self, theta, qubit1):
        self.single("p",[theta],[qubit1])

    def cp(self, theta, qubit1, qubit2):
        self.double("cp",[theta],[qubit1, qubit2])
        
    def ccp(self, theta, qubit1, qubit2, qubit3):
        self.triple("ccp",[theta],[qubit1, qubit2, qubit3])

    def sqrt_x(self, qubit1):
        self.single("sqrt_x",[],[qubit1])
    
    def sqrt_y(self, qubit1):
        self.single("sqrt_y",[],[qubit1])
        
    def sqrt_z(self, qubit1):
        self.single("sqrt_z",[],[qubit1])    
    
    def gpi(self, phi, qubit1):
        self.single("gpi",[phi],[qubit1])

    def gpi2(self, phi, qubit1):
        self.single("gpi2",[phi],[qubit1])

    def xp(self, theta, qubit1):
        self.single("xp",[theta],[qubit1])

    def yp(self, theta, qubit1):
        self.single("yp",[theta],[qubit1])

    def zp(self, theta, qubit1):
        self.single("zp",[theta],[qubit1])

    def xxp(self, theta, qubit1, qubit2):
        self.double("xxp",[theta],[qubit1, qubit2])

    def yyp(self, theta, qubit1, qubit2):
        self.double("yyp",[theta],[qubit1, qubit2])

    def zzp(self, theta, qubit1, qubit2):
        self.double("zzp",[theta],[qubit1, qubit2])       
    
    def phased_xp(self, theta, phi, qubit1):
        self.single("phased_xp",[theta, phi],[qubit1])

    def phased_yp(self, theta, phi, qubit1):
        self.single("phased_yp",[theta, phi],[qubit1])

    def phased_zp(self, theta, phi, qubit1):
        self.single("phased_zp",[theta, phi],[qubit1])        
    
    def cnotp(self, theta, qubit1, qubit2):
        self.double("cnotp",[theta],[qubit1, qubit2])

    def ccnotp(self, theta, qubit1, qubit2, qubit3):
        self.triple("ccnotp",[theta],[qubit1, qubit2, qubit3])  

    def cyp(self, theta, qubit1, qubit2):
        self.double("cyp",[theta],[qubit1, qubit2])

    def ccyp(self, theta, qubit1, qubit2, qubit3):
        self.triple("ccyp",[theta],[qubit1, qubit2, qubit3])  

    def czp(self, theta, qubit1, qubit2):
        self.double("czp",[theta],[qubit1, qubit2])

    def cczp(self, theta, qubit1, qubit2, qubit3):
        self.triple("cczp",[theta],[qubit1, qubit2, qubit3])          
    
    def measure(self, qubits):
        cparams=[]
        cqubits=[]
        cgate="measure"
        if len(qubits) == 0:
            raise(Exception("number of qubits to measure cannot be zero"))
        else:
            for qubit in qubits:
                if qubit < 0 or qubit >= self.num_qubits:
                    raise(Exception(f"invalid qubit: {qubit}"))
                else:    
                    cqubits.append(qubit)                
        self.operations.append([cgate, cparams, cqubits])

    def measure_all(self):
        cparams=[]
        cqubits=[]
        cgate="measure"
        for qubit in range(self.num_qubits):
            cqubits.append(qubit)                
        self.operations.append([cgate, cparams, cqubits])        
        
    
    def randomCircuit(self, numberOfOperations, qubitsToUseForRandomCircuit ):
        
        qubitsCount = len(qubitsToUseForRandomCircuit)
        if qubitsCount < 3:
            raise(Exception("The number of qubits needed to generate random circuits is >= 3"))
        
        
        gatesAndQubitsMap = {}
        # 1 qubit gates 
        gatesAndQubitsMap["x"] = 1
        gatesAndQubitsMap["y"] = 1
        gatesAndQubitsMap["z"] = 1
        gatesAndQubitsMap["rx"] = 1
        gatesAndQubitsMap["ry"] = 1
        gatesAndQubitsMap["rz"] = 1
        gatesAndQubitsMap["h"] = 1
        gatesAndQubitsMap["s"] = 1
        gatesAndQubitsMap["sdg"] = 1
        gatesAndQubitsMap["t"] = 1
        gatesAndQubitsMap["tdg"] = 1
        gatesAndQubitsMap["sx"] = 1
        gatesAndQubitsMap["sxdg"] = 1        
        # 2 qubit gates 
        gatesAndQubitsMap["cx"] = 2
        gatesAndQubitsMap["cy"] = 2
        gatesAndQubitsMap["cz"] = 2
        gatesAndQubitsMap["crx"] = 2
        gatesAndQubitsMap["cry"] = 2
        gatesAndQubitsMap["crz"] = 2
        gatesAndQubitsMap["ch"] = 2
        gatesAndQubitsMap["dcx"] = 2
        gatesAndQubitsMap["ecr"] = 2
        gatesAndQubitsMap["iswap"] = 2
        gatesAndQubitsMap["swap"] = 2 
        gatesAndQubitsMap["csx"] = 2         
        # 3 qubit gates
        gatesAndQubitsMap["cswap"] = 3 
        gatesAndQubitsMap["ccx"] = 3 

        
        allPossibleGates = list(gatesAndQubitsMap.keys())
        allPossibleGatesCount = len(allPossibleGates)
        
        for i in range(numberOfOperations):
            index = random.randrange(allPossibleGatesCount)
            cgate = allPossibleGates[index]
            
            numberOfQubits = gatesAndQubitsMap[cgate]

            np.random.shuffle(qubitsToUseForRandomCircuit)
            cqubits=[]
            for j in range(numberOfQubits):
                cqubits.append( qubitsToUseForRandomCircuit[j] )
            
            cparams=[]
            if cgate in ["rx","ry","rz","crx","cry","crz"]:
                theta = random.uniform(0.0, 2*np.pi)
                cparams.append(theta)
                
            self.operations.append([cgate, cparams, cqubits])   
        
        
        
class AutomatskiKomencoNative:
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
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
            
        return self.deserialize_result(struct, repetitions)

    def serialize_circuit(self, circuit, topK):
        # Extract the number of qubits
        num_qubits = circuit.num_qubits

        operations = []
        measurements = []

        for cgate, cparams, cqubits in circuit.operations:
            gate = cgate
            params = [param for param in cparams]
            qubits = [q for q in cqubits]
            if gate == 'measure':
                for q in qubits:
                    measurements.append(q)
            else:
                operations.append({"gate": gate, "params": params, "qubits": qubits})
        
        print("Executing Quantum Circuit With...")
        print(f"{num_qubits} Qubits And ...")
        print(f"{len(operations)} Gates")
        
        if len(measurements) == 0:
            raise(Exception("There are no measurements done at the end of the circuit."))
        
        return { "num_qubits": num_qubits, "operations": operations, "measurements": measurements, "topK": topK}    

    @staticmethod
    def deserialize_result(response_data, repetitions):
        measurementsStrings = response_data['measurements']
        
        measurements = {}
        for key, value in measurementsStrings.items():
            #combo = np.array( [int(char) for char in key] , dtype=np.int32)
            count = round(value*repetitions)
            measurements[key] = count

        return { "result": measurements }     





            