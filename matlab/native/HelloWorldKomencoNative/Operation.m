classdef Operation
    properties (Access = private)
        gate
        qubits
        params
    end
    
    methods
        function obj = Operation(gate, qubits, params)
            obj.gate = gate;
            obj.qubits = qubits;
            obj.params = params;
        end
        
        function gate = getGate(obj)
            gate = obj.gate;
        end
        
        function qubits = getQubits(obj)
            qubits = obj.qubits;
        end
        
        function params = getParams(obj)
            params = obj.params;
        end
    end
end