classdef QuantumCircuit
    properties (Access = private)
        numQubits
        operations
    end
    
    methods
        function obj = QuantumCircuit(numQubits)
            obj.numQubits = numQubits;
            obj.operations = [];
        end
        
        function numQubits = getNumQubits(obj)
            numQubits = obj.numQubits;
        end
        
        function operations = getOperations(obj)
            operations = obj.operations;
        end
        
        function obj = addSingle(obj, gate, params, qubits)
            if length(qubits) ~= 1
                error('Number of qubits for gate %s has to be one', gate);
            end
            for qubit = qubits
                if qubit < 0 || qubit >= obj.numQubits
                    error('Invalid qubit: %d', qubit);
                end
            end
            % obj.operations{end+1} = Operation(gate, qubits, params);
            obj.operations = [obj.operations; Operation(gate, qubits, params)];
        end
        
        function obj = addDouble(obj, gate, params, qubits)
            if length(qubits) ~= 2
                error('Number of qubits for gate %s has to be two', gate);
            end
            for qubit = qubits
                if qubit < 0 || qubit >= obj.numQubits
                    error('Invalid qubit: %d', qubit);
                end
            end
            % obj.operations{end+1} = Operation(gate, qubits, params);
            obj.operations = [obj.operations; Operation(gate, qubits, params)];
        end
        
        function obj = addTriple(obj, gate, params, qubits)
            if length(qubits) ~= 3
                error('Number of qubits for gate %s has to be three', gate);
            end
            for qubit = qubits
                if qubit < 0 || qubit >= obj.numQubits
                    error('Invalid qubit: %d', qubit);
                end
            end
            % obj.operations{end+1} = Operation(gate, qubits, params);
            obj.operations = [obj.operations; Operation(gate, qubits, params)];
        end
        
        function obj = addMultiple(obj, gate, params, qubits)
            requiredQubits = floor(log(length(gate)) / log(2));
            if length(qubits) ~= requiredQubits
                error('Number of qubits for gate %s has to be %d', gate, requiredQubits);
            end
            for qubit = qubits
                if qubit < 0 || qubit >= obj.numQubits
                    error('Invalid qubit: %d', qubit);
                end
            end
            % obj.operations{end+1} = Operation(gate, qubits, params);
            obj.operations = [obj.operations; Operation(gate, qubits, params)];
        end
        
        function obj = id(obj, qubit1)
            obj = obj.addSingle('id', [], [qubit1]);
        end
        
        function obj = x(obj, qubit1)
            obj = obj.addSingle('x', [], [qubit1]);
        end
        
        function obj = y(obj, qubit1)
            obj = obj.addSingle('y', [], [qubit1]);
        end
        
        function obj = z(obj, qubit1)
            obj = obj.addSingle('z', [], [qubit1]);
        end
        
        function obj = h(obj, qubit1)
            obj = obj.addSingle('h', [], [qubit1]);
        end
        
        function obj = s(obj, qubit1)
            obj = obj.addSingle('s', [], [qubit1]);
        end
        
        function obj = sdg(obj, qubit1)
            obj = obj.addSingle('sdg', [], [qubit1]);
        end
        
        function obj = t(obj, qubit1)
            obj = obj.addSingle('t', [], [qubit1]);
        end
        
        function obj = tdg(obj, qubit1)
            obj = obj.addSingle('tdg', [], [qubit1]);
        end
        
        function obj = rx(obj, theta, qubit1)
            obj = obj.addSingle('rx', [theta], [qubit1]);
        end
        
        function obj = ry(obj, theta, qubit1)
            obj = obj.addSingle('ry', [theta], [qubit1]);
        end
        
        function obj = rz(obj, theta, qubit1)
            obj = obj.addSingle('rz', [theta], [qubit1]);
        end
        
        function obj = u(obj, theta, phi, lam, qubit1)
            obj = obj.addSingle('u', [theta, phi, lam], [qubit1]);
        end
        
        function obj = u1(obj, theta, qubit1)
            obj = obj.addSingle('u1', [theta], [qubit1]);
        end
        
        function obj = u2(obj, phi, lam, qubit1)
            obj = obj.addSingle('u2', [phi, lam], [qubit1]);
        end
        
        function obj = u3(obj, theta, phi, lam, qubit1)
            obj = obj.addSingle('u3', [theta, phi, lam], [qubit1]);
        end
        
        function obj = sx(obj, qubit1)
            obj = obj.addSingle('sx', [], [qubit1]);
        end
        
        function obj = sxdg(obj, qubit1)
            obj = obj.addSingle('sxdg', [], [qubit1]);
        end
        
        function obj = r(obj, theta, phi, qubit1)
            obj = obj.addSingle('r', [theta, phi], [qubit1]);
        end
        
        function obj = cx(obj, qubit1, qubit2)
            obj = obj.addDouble('cx', [], [qubit1, qubit2]);
        end
        
        function obj = cy(obj, qubit1, qubit2)
            obj = obj.addDouble('cy', [], [qubit1, qubit2]);
        end
        
        function obj = cz(obj, qubit1, qubit2)
            obj = obj.addDouble('cz', [], [qubit1, qubit2]);
        end
        
        function obj = ch(obj, qubit1, qubit2)
            obj = obj.addDouble('ch', [], [qubit1, qubit2]);
        end
        
        function obj = ucrx(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('ucrx', [theta], [qubit1, qubit2]);
        end
        
        function obj = ucry(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('ucry', [theta], [qubit1, qubit2]);
        end
        
        function obj = ucrz(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('ucrz', [theta], [qubit1, qubit2]);
        end
        
        function obj = crx(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('crx', [theta], [qubit1, qubit2]);
        end
        
        function obj = cry(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('cry', [theta], [qubit1, qubit2]);
        end
        
        function obj = crz(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('crz', [theta], [qubit1, qubit2]);
        end
        
        function obj = cr(obj, theta, phi, lam, qubit1, qubit2)
            obj = obj.addDouble('cr', [theta, phi, lam], [qubit1, qubit2]);
        end
        
        function obj = cu(obj, theta, phi, lam, gamma, qubit1, qubit2)
            obj = obj.addDouble('cu', [theta, phi, lam, gamma], [qubit1, qubit2]);
        end
        
        function obj = cu1(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('cu1', [theta], [qubit1, qubit2]);
        end
        
        function obj = cu2(obj, phi, lam, qubit1, qubit2)
            obj = obj.addDouble('cu2', [phi, lam], [qubit1, qubit2]);
        end
        
        function obj = cu3(obj, theta, phi, lam, qubit1, qubit2)
            obj = obj.addDouble('cu3', [theta, phi, lam], [qubit1, qubit2]);
        end
        
        function obj = dcx(obj, qubit1, qubit2)
            obj = obj.addDouble('dcx', [], [qubit1, qubit2]);
        end
        
        function obj = ecr(obj, qubit1, qubit2)
            obj = obj.addDouble('ecr', [], [qubit1, qubit2]);
        end
        
        function obj = iswap(obj, qubit1, qubit2)
            obj = obj.addDouble('iswap', [], [qubit1, qubit2]);
        end
        
        function obj = rxx(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('rxx', [theta], [qubit1, qubit2]);
        end
        
        function obj = ryy(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('ryy', [theta], [qubit1, qubit2]);
        end
        
        function obj = rzz(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('rzz', [theta], [qubit1, qubit2]);
        end
        
        function obj = rzx(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('rzx', [theta], [qubit1, qubit2]);
        end
        
        function obj = cswap(obj, qubit1, qubit2, qubit3)
            obj = obj.addTriple('cswap', [], [qubit1, qubit2, qubit3]);
        end
        
        function obj = ccx(obj, qubit1, qubit2, qubit3)
            obj = obj.addTriple('ccx', [], [qubit1, qubit2, qubit3]);
        end
        
        function obj = ccy(obj, qubit1, qubit2, qubit3)
            obj = obj.addTriple('ccy', [], [qubit1, qubit2, qubit3]);
        end
        
        function obj = ccz(obj, qubit1, qubit2, qubit3)
            obj = obj.addTriple('ccz', [], [qubit1, qubit2, qubit3]);
        end
        
        function obj = c3x(obj, qubits)
            obj = obj.addMultiple('c3x', [], qubits);
        end
        
        function obj = c4x(obj, qubits)
            obj = obj.addMultiple('c4x', [], qubits);
        end
        
        function obj = mcx(obj, qubits)
            obj = obj.addMultiple('mcx', [], qubits);
        end
        
        function obj = mcu1(obj, theta, qubits)
            obj = obj.addMultiple('mcu1', theta, qubits);
        end
        
        function obj = mcu2(obj, phi, lam, qubits)
            obj = obj.addMultiple('mcu2', [phi, lam], qubits);
        end
        
        function obj = mcu3(obj, theta, phi, lam, qubits)
            obj = obj.addMultiple('mcu3', [theta, phi, lam], qubits);
        end
        
        function obj = mcz(obj, qubits)
            obj = obj.addMultiple('mcz', [], qubits);
        end
        
        function obj = mcp(obj, qubits)
            obj = obj.addMultiple('mcp', [], qubits);
        end
        
        function obj = mcrx(obj, qubits)
            obj = obj.addMultiple('mcrx', [], qubits);
        end
        
        function obj = mcry(obj, qubits)
            obj = obj.addMultiple('mcry', [], qubits);
        end
        
        function obj = mcrz(obj, qubits)
            obj = obj.addMultiple('mcrz', [], qubits);
        end
        
        function obj = qft(obj, qubits)
            obj = obj.addMultiple('qft', [], qubits);
        end
        
        function obj = inverse_qft(obj, qubits)
            obj = obj.addMultiple('iqft', [], qubits);
        end
        
        function obj = swap(obj, qubit1, qubit2)
            obj = obj.addDouble('swap', [], [qubit1, qubit2]);
        end
        
        function obj = csx(obj, qubit1, qubit2)
            obj = obj.addDouble('csx', [], [qubit1, qubit2]);
        end
        
        function obj = p(obj, theta, qubit1)
            obj = obj.addSingle('p', [theta], [qubit1]);
        end
        
        function obj = cp(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('cp', [theta], [qubit1, qubit2]);
        end
        
        function obj = ccp(obj, theta, qubit1, qubit2, qubit3)
            obj = obj.addTriple('ccp', [theta], [qubit1, qubit2, qubit3]);
        end
        
        function obj = sqrt_x(obj, qubit1)
            obj = obj.addSingle('sqrt_x', [], [qubit1]);
        end
        
        function obj = sqrt_y(obj, qubit1)
            obj = obj.addSingle('sqrt_y', [], [qubit1]);
        end
        
        function obj = sqrt_z(obj, qubit1)
            obj = obj.addSingle('sqrt_z', [], [qubit1]);
        end
        
        function obj = gpi(obj, phi, qubit1)
            obj = obj.addSingle('gpi', [phi], [qubit1]);
        end
        
        function obj = gpi2(obj, phi, qubit1)
            obj = obj.addSingle('gpi2', [phi], [qubit1]);
        end
        
        function obj = xp(obj, theta, qubit1)
            obj = obj.addSingle('xp', [theta], [qubit1]);
        end
        
        function obj = yp(obj, theta, qubit1)
            obj = obj.addSingle('yp', [theta], [qubit1]);
        end
        
        function obj = zp(obj, theta, qubit1)
            obj = obj.addSingle('zp', [theta], [qubit1]);
        end
        
        function obj = xxp(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('xxp', [theta], [qubit1, qubit2]);
        end
        
        function obj = yyp(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('yyp', [theta], [qubit1, qubit2]);
        end
        
        function obj = zzp(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('zzp', [theta], [qubit1, qubit2]);
        end
        
        function obj = phased_xp(obj, theta, phi, qubit1)
            obj = obj.addSingle('phased_xp', [theta, phi], [qubit1]);
        end
        
        function obj = phased_yp(obj, theta, phi, qubit1)
            obj = obj.addSingle('phased_yp', [theta, phi], [qubit1]);
        end
        
        function obj = phased_zp(obj, theta, phi, qubit1)
            obj = obj.addSingle('phased_zp', [theta, phi], [qubit1]);
        end
        
        function obj = cnotp(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('cnotp', [theta], [qubit1, qubit2]);
        end
        
        function obj = ccnotp(obj, theta, qubit1, qubit2, qubit3)
            obj = obj.addTriple('ccnotp', [theta], [qubit1, qubit2, qubit3]);
        end
        
        function obj = cyp(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('cyp', [theta], [qubit1, qubit2]);
        end
        
        function obj = ccyp(obj, theta, qubit1, qubit2, qubit3)
            obj = obj.addTriple('ccyp', [theta], [qubit1, qubit2, qubit3]);
        end
        
        function obj = czp(obj, theta, qubit1, qubit2)
            obj = obj.addDouble('czp', [theta], [qubit1, qubit2]);
        end
        
        function obj = cczp(obj, theta, qubit1, qubit2, qubit3)
            obj = obj.addTriple('cczp', [theta], [qubit1, qubit2, qubit3]);
        end
        
        function obj = measure(obj, qubits)
            if isempty(qubits)
                error('Number of qubits to measure cannot be zero');
            end
            for qubit = qubits
                if qubit < 0 || qubit >= obj.numQubits
                    error('Invalid qubit: %d', qubit);
                end
            end
            % obj.operations{end+1} = Operation('measure', qubits, []);
            obj.operations = [obj.operations; Operation('measure', qubits, [])];
        end
        
        function obj = measureAll(obj)
            qubits = 0:(obj.numQubits - 1);
            % obj.operations{end+1} = Operation('measure', qubits, []);
            obj.operations = [obj.operations; Operation('measure', qubits, [])];
        end
    

        function obj = randomCircuit(obj, numberOfOperations, qubitsToUseForRandomCircuit)
            qubitsCount = length(qubitsToUseForRandomCircuit);
            if qubitsCount < 3
                error('The number of qubits needed to generate random circuits is >= 3');
            end
        
            gatesAndQubitsMap = containers.Map(...
                {'x', 'y', 'z', 'rx', 'ry', 'rz', 'h', 's', 'sdg', 't', 'tdg', 'sx', 'sxdg', ...
                'cx', 'cy', 'cz', 'crx', 'cry', 'crz', 'ch', 'dcx', 'ecr', 'iswap', 'swap', 'csx', ...
                'cswap', 'ccx'}, ...
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ...
                3, 3]);
        
            allPossibleGates = keys(gatesAndQubitsMap);
            allPossibleGatesCount = length(allPossibleGates);
        
            for i = 1:numberOfOperations
                index = randi(allPossibleGatesCount);
                cgate = allPossibleGates{index};
        
                numberOfQubits = gatesAndQubitsMap(cgate);
        
                qubitsToUseForRandomCircuit = qubitsToUseForRandomCircuit(randperm(length(qubitsToUseForRandomCircuit)));
                cqubits = qubitsToUseForRandomCircuit(1:numberOfQubits);
        
                cparams = [];
                if ismember(cgate, {'rx', 'ry', 'rz', 'crx', 'cry', 'crz'})
                    theta = rand() * 2 * pi;
                    cparams = [cparams; theta];
                end
        
                %obj.operations{end+1} = Operation(cgate, cqubits, cparams);
                obj.operations = [obj.operations; Operation(cgate, cqubits, cparams)];
            end
        end
    end
end