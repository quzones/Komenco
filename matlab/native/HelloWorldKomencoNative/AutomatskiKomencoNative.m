classdef AutomatskiKomencoNative
    properties (Access = private)
        host
        port
    end
    
    methods
        function obj = AutomatskiKomencoNative(host, port)
            obj.host = host;
            obj.port = port;
        end
        
        function measurements = run(obj, circuit, repetitions, topK)
            tstart = tic;

            body = obj.serializeCircuit(circuit, topK);
            disp(body);

            struct2 = obj.postRequest(body);

            executionTime = toc(tstart) * 1000;
            fprintf('Time Taken %.2fms\n', executionTime);

            if isfield(struct2, 'error')
                fprintf('%s\n', struct2.error);
                error(struct2.error);
            end

            measurements = obj.deserializeResult(struct2, repetitions);
        end
    end
    
    methods (Access = private)
        function body = serializeCircuit(obj, circuit, topK)
            numQubits = circuit.getNumQubits();

            operations = [];
            measurements = [];

            inops = circuit.getOperations();
            for i = 1:length(inops)
                operation = inops(i);
                gate = operation.getGate();
                params = operation.getParams();
                qubits = operation.getQubits();

                if strcmp(gate, 'measure')
                    measurements = [measurements; qubits];
                else
                    op.gate = gate;
                    if isscalar(params)
                        params = {params};
                    end  
                    op.params = params;
                    if isscalar(qubits)
                        qubits = {qubits};
                    end                    
                    op.qubits = qubits;
                    %operations{end+1} = op;
                    operations = [operations; op];
                end
            end

            fprintf('Executing Quantum Circuit With...\n');
            fprintf('%d Qubits And ...\n', numQubits);
            fprintf('%d Gates\n', length(operations));

            if isempty(measurements)
                error('There are no measurements done at the end of the circuit.');
            end

            body.num_qubits = numQubits;
            body.operations = operations;
            body.measurements = measurements;
            body.topK = topK;
        end
        
        function struct2 = postRequest(obj, body)
            url = sprintf('http://%s:%d/api/komenco', obj.host, obj.port);
            options = weboptions('MediaType', 'application/json', 'Timeout', 60);
            response = webwrite(url, body, options);

            if isempty(response)
                error('Error making POST request');
            end

            struct2 = response;
        end
        
        function measurements = deserializeResult(obj, responseData, repetitions)
            measurementsStrings = responseData.measurements;

            measurements = containers.Map;
            keys = fieldnames(measurementsStrings);
            for i = 1:length(keys)
                key = keys{i};
                value = measurementsStrings.(key);
                count = round(value * repetitions);
                measurements(key) = count;
            end
        end
    end
end