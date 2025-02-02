










struct Operation
    gate::String
    qubits::Vector{Int}
    params::Vector{Float64}
end

function get_gate(operation::Operation)
    return operation.gate
end

function get_params(operation::Operation)
    return operation.params
end

function get_qubits(operation::Operation)
    return operation.qubits
end

mutable struct QuantumCircuit
    numQubits::Int
    operations::Vector{Operation}
end

function QuantumCircuit(numQubits::Int)
    return QuantumCircuit(numQubits, Vector{Operation}())
end

function get_num_qubits(circuit::QuantumCircuit)
    return circuit.numQubits
end

function get_operations(circuit::QuantumCircuit)
    return circuit.operations
end

function add_single(circuit::QuantumCircuit, gate::String, paramsList::Vector{Float64}, qubits::Vector{Int})
    if length(qubits) != 1
        throw(ArgumentError("Number of qubits for gate $gate has to be one"))
    end
    for qubit in qubits
        if qubit < 0 || qubit >= circuit.numQubits
            throw(ArgumentError("Invalid qubit: $qubit"))
        end
    end
    push!(circuit.operations, Operation(gate, qubits, paramsList))
end

function add_double(circuit::QuantumCircuit, gate::String, paramsList::Vector{Float64}, qubits::Vector{Int})
    if length(qubits) != 2
        throw(ArgumentError("Number of qubits for gate $gate has to be two"))
    end
    for qubit in qubits
        if qubit < 0 || qubit >= circuit.numQubits
            throw(ArgumentError("Invalid qubit: $qubit"))
        end
    end
    push!(circuit.operations, Operation(gate, qubits, paramsList))
end

function add_triple(circuit::QuantumCircuit, gate::String, paramsList::Vector{Float64}, qubits::Vector{Int})
    if length(qubits) != 3
        throw(ArgumentError("Number of qubits for gate $gate has to be three"))
    end
    for qubit in qubits
        if qubit < 0 || qubit >= circuit.numQubits
            throw(ArgumentError("Invalid qubit: $qubit"))
        end
    end
    push!(circuit.operations, Operation(gate, qubits, paramsList))
end

function add_multiple(circuit::QuantumCircuit, gate::String, paramsList::Vector{Float64}, qubits::Vector{Int})
    requiredQubits = Int(log(length(gate)) / log(2))
    if length(qubits) != requiredQubits
        throw(ArgumentError("Number of qubits for gate $gate has to be $requiredQubits"))
    end
    for qubit in qubits
        if qubit < 0 || qubit >= circuit.numQubits
            throw(ArgumentError("Invalid qubit: $qubit"))
        end
    end
    push!(circuit.operations, Operation(gate, qubits, paramsList))
end

function id(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "id", Float64[], [qubit1])
end

function x(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "x", Float64[], [qubit1])
end

function y(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "y", Float64[], [qubit1])
end

function z(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "z", Float64[], [qubit1])
end

function h(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "h", Float64[], [qubit1])
end

function s(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "s", Float64[], [qubit1])
end

function sdg(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "sdg", Float64[], [qubit1])
end

function t(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "t", Float64[], [qubit1])
end

function tdg(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "tdg", Float64[], [qubit1])
end

function rx(circuit::QuantumCircuit, theta::Float64, qubit1::Int)
    add_single(circuit, "rx", [theta], [qubit1])
end

function ry(circuit::QuantumCircuit, theta::Float64, qubit1::Int)
    add_single(circuit, "ry", [theta], [qubit1])
end

function rz(circuit::QuantumCircuit, theta::Float64, qubit1::Int)
    add_single(circuit, "rz", [theta], [qubit1])
end

function u(circuit::QuantumCircuit, theta::Float64, phi::Float64, lam::Float64, qubit1::Int)
    add_single(circuit, "u", [theta, phi, lam], [qubit1])
end

function u1(circuit::QuantumCircuit, theta::Float64, qubit1::Int)
    add_single(circuit, "u1", [theta], [qubit1])
end

function u2(circuit::QuantumCircuit, phi::Float64, lam::Float64, qubit1::Int)
    add_single(circuit, "u2", [phi, lam], [qubit1])
end

function u3(circuit::QuantumCircuit, theta::Float64, phi::Float64, lam::Float64, qubit1::Int)
    add_single(circuit, "u3", [theta, phi, lam], [qubit1])
end

function sx(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "sx", Float64[], [qubit1])
end

function sxdg(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "sxdg", Float64[], [qubit1])
end

function r(circuit::QuantumCircuit, theta::Float64, phi::Float64, qubit1::Int)
    add_single(circuit, "r", [theta, phi], [qubit1])
end

function cx(circuit::QuantumCircuit, qubit1::Int, qubit2::Int)
    add_double(circuit, "cx", Float64[], [qubit1, qubit2])
end

function cy(circuit::QuantumCircuit, qubit1::Int, qubit2::Int)
    add_double(circuit, "cy", Float64[], [qubit1, qubit2])
end

function cz(circuit::QuantumCircuit, qubit1::Int, qubit2::Int)
    add_double(circuit, "cz", Float64[], [qubit1, qubit2])
end

function ch(circuit::QuantumCircuit, qubit1::Int, qubit2::Int)
    add_double(circuit, "ch", Float64[], [qubit1, qubit2])
end

function ucrx(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "ucrx", [theta], [qubit1, qubit2])
end

function ucry(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "ucry", [theta], [qubit1, qubit2])
end

function ucrz(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "ucrz", [theta], [qubit1, qubit2])
end

function crx(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "crx", [theta], [qubit1, qubit2])
end

function cry(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "cry", [theta], [qubit1, qubit2])
end

function crz(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "crz", [theta], [qubit1, qubit2])
end

function cr(circuit::QuantumCircuit, theta::Float64, phi::Float64, lam::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "cr", [theta, phi, lam], [qubit1, qubit2])
end

function cu(circuit::QuantumCircuit, theta::Float64, phi::Float64, lam::Float64, gamma::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "cu1", [theta, phi, lam, gamma], [qubit1, qubit2])
end

function cu1(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "cu1", [theta], [qubit1, qubit2])
end

function cu2(circuit::QuantumCircuit, phi::Float64, lam::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "cu2", [phi, lam], [qubit1, qubit2])
end

function cu3(circuit::QuantumCircuit, theta::Float64, phi::Float64, lam::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "cu3", [theta, phi, lam], [qubit1, qubit2])
end

function dcx(circuit::QuantumCircuit, qubit1::Int, qubit2::Int)
    add_double(circuit, "dcx", Float64[], [qubit1, qubit2])
end

function ecr(circuit::QuantumCircuit, qubit1::Int, qubit2::Int)
    add_double(circuit, "ecr", Float64[], [qubit1, qubit2])
end

function iswap(circuit::QuantumCircuit, qubit1::Int, qubit2::Int)
    add_double(circuit, "iswap", Float64[], [qubit1, qubit2])
end

function rxx(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "rxx", [theta], [qubit1, qubit2])
end

function ryy(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "ryy", [theta], [qubit1, qubit2])
end

function rzz(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "rzz", [theta], [qubit1, qubit2])
end

function rzx(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "rzx", [theta], [qubit1, qubit2])
end

function cswap(circuit::QuantumCircuit, qubit1::Int, qubit2::Int, qubit3::Int)
    add_triple(circuit, "cswap", Float64[], [qubit1, qubit2, qubit3])
end

function ccx(circuit::QuantumCircuit, qubit1::Int, qubit2::Int, qubit3::Int)
    add_triple(circuit, "ccx", Float64[], [qubit1, qubit2, qubit3])
end

function ccy(circuit::QuantumCircuit, qubit1::Int, qubit2::Int, qubit3::Int)
    add_triple(circuit, "ccy", Float64[], [qubit1, qubit2, qubit3])
end

function ccz(circuit::QuantumCircuit, qubit1::Int, qubit2::Int, qubit3::Int)
    add_triple(circuit, "ccz", Float64[], [qubit1, qubit2, qubit3])
end

function c3x(circuit::QuantumCircuit, qubits::Vector{Int})
    add_multiple(circuit, "c3x", Float64[], qubits)
end

function c4x(circuit::QuantumCircuit, qubits::Vector{Int})
    add_multiple(circuit, "c4x", Float64[], qubits)
end

function mcx(circuit::QuantumCircuit, qubits::Vector{Int})
    add_multiple(circuit, "mcx", Float64[], qubits)
end

function mcu1(circuit::QuantumCircuit, theta::Float64, qubits::Vector{Int})
    add_multiple(circuit, "mcu1", [theta], qubits)
end

function mcu2(circuit::QuantumCircuit, phi::Float64, lam::Float64, qubits::Vector{Int})
    add_multiple(circuit, "mcu2", [phi, lam], qubits)
end

function mcu3(circuit::QuantumCircuit, theta::Float64, phi::Float64, lam::Float64, qubits::Vector{Int})
    add_multiple(circuit, "mcu3", [theta, phi, lam], qubits)
end

function mcz(circuit::QuantumCircuit, qubits::Vector{Int})
    add_multiple(circuit, "mcz", Float64[], qubits)
end

function mcp(circuit::QuantumCircuit, qubits::Vector{Int})
    add_multiple(circuit, "mcp", Float64[], qubits)
end

function mcrx(circuit::QuantumCircuit, qubits::Vector{Int})
    add_multiple(circuit, "mcrx", Float64[], qubits)
end

function mcry(circuit::QuantumCircuit, qubits::Vector{Int})
    add_multiple(circuit, "mcry", Float64[], qubits)
end

function mcrz(circuit::QuantumCircuit, qubits::Vector{Int})
    add_multiple(circuit, "mcrz", Float64[], qubits)
end

function qft(circuit::QuantumCircuit, qubits::Vector{Int})
    add_multiple(circuit, "qft", Float64[], qubits)
end

function inverse_qft(circuit::QuantumCircuit, qubits::Vector{Int})
    add_multiple(circuit, "iqft", Float64[], qubits)
end

function swap(circuit::QuantumCircuit, qubit1::Int, qubit2::Int)
    add_double(circuit, "swap", Float64[], [qubit1, qubit2])
end

function csx(circuit::QuantumCircuit, qubit1::Int, qubit2::Int)
    add_double(circuit, "csx", Float64[], [qubit1, qubit2])
end

function p(circuit::QuantumCircuit, theta::Float64, qubit1::Int)
    add_single(circuit, "p", [theta], [qubit1])
end

function cp(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "cp", [theta], [qubit1, qubit2])
end

function ccp(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int, qubit3::Int)
    add_triple(circuit, "ccp", [theta], [qubit1, qubit2, qubit3])
end

function sqrt_x(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "sqrt_x", Float64[], [qubit1])
end

function sqrt_y(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "sqrt_y", Float64[], [qubit1])
end

function sqrt_z(circuit::QuantumCircuit, qubit1::Int)
    add_single(circuit, "sqrt_z", Float64[], [qubit1])
end

function gpi(circuit::QuantumCircuit, phi::Float64, qubit1::Int)
    add_single(circuit, "gpi", [phi], [qubit1])
end

function gpi2(circuit::QuantumCircuit, phi::Float64, qubit1::Int)
    add_single(circuit, "gpi2", [phi], [qubit1])
end

function xp(circuit::QuantumCircuit, theta::Float64, qubit1::Int)
    add_single(circuit, "xp", [theta], [qubit1])
end

function yp(circuit::QuantumCircuit, theta::Float64, qubit1::Int)
    add_single(circuit, "yp", [theta], [qubit1])
end

function zp(circuit::QuantumCircuit, theta::Float64, qubit1::Int)
    add_single(circuit, "zp", [theta], [qubit1])
end

function xxp(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "xxp", [theta], [qubit1, qubit2])
end

function yyp(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "yyp", [theta], [qubit1, qubit2])
end

function zzp(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "zzp", [theta], [qubit1, qubit2])
end

function phased_xp(circuit::QuantumCircuit, theta::Float64, phi::Float64, qubit1::Int)
    add_single(circuit, "phased_xp", [theta, phi], [qubit1])
end

function phased_yp(circuit::QuantumCircuit, theta::Float64, phi::Float64, qubit1::Int)
    add_single(circuit, "phased_yp", [theta, phi], [qubit1])
end

function phased_zp(circuit::QuantumCircuit, theta::Float64, phi::Float64, qubit1::Int)
    add_single(circuit, "phased_zp", [theta, phi], [qubit1])
end

function cnotp(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "cnotp", [theta], [qubit1, qubit2])
end

function ccnotp(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int, qubit3::Int)
    add_triple(circuit, "ccnotp", [theta], [qubit1, qubit2, qubit3])
end

function cyp(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "cyp", [theta], [qubit1, qubit2])
end

function ccyp(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int, qubit3::Int)
    add_triple(circuit, "ccyp", [theta], [qubit1, qubit2, qubit3])
end

function czp(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int)
    add_double(circuit, "czp", [theta], [qubit1, qubit2])
end

function cczp(circuit::QuantumCircuit, theta::Float64, qubit1::Int, qubit2::Int, qubit3::Int)
    add_triple(circuit, "cczp", [theta], [qubit1, qubit2, qubit3])
end

function measure(circuit::QuantumCircuit, qubits::Vector{Int})
    cparams = Float64[]
    cqubits = Int[]
    cgate = "measure"
    if length(qubits) == 0
        throw(ArgumentError("number of qubits to measure cannot be zero"))
    else
        for qubit in qubits
            if qubit < 0 || qubit >= circuit.numQubits
                throw(ArgumentError("invalid qubit: $qubit"))
            else
                push!(cqubits, qubit)
            end
        end
    end
    push!(circuit.operations, Operation(cgate, cqubits, cparams))
end

function measure_all(circuit::QuantumCircuit)
    cparams = Float64[]
    cqubits = Int[]
    cgate = "measure"
    for qubit in 0:(circuit.numQubits - 1)
        push!(cqubits, qubit)
    end
    push!(circuit.operations, Operation(cgate, cqubits, cparams))
end

function random_circuit(circuit::QuantumCircuit, numberOfOperations::Int, qubitsToUseForRandomCircuit::Vector{Int})
    qubitsCount = length(qubitsToUseForRandomCircuit)
    if qubitsCount < 3
        throw(ArgumentError("The number of qubits needed to generate random circuits is >= 3"))
    end

    gatesAndQubitsMap = Dict(
        # 1 qubit gates
        "x" => 1,
        "y" => 1,
        "z" => 1,
        "rx" => 1,
        "ry" => 1,
        "rz" => 1,
        "h" => 1,
        "s" => 1,
        "sdg" => 1,
        "t" => 1,
        "tdg" => 1,
        "sx" => 1,
        "sxdg" => 1,
        # 2 qubit gates
        "cx" => 2,
        "cy" => 2,
        "cz" => 2,
        "crx" => 2,
        "cry" => 2,
        "crz" => 2,
        "ch" => 2,
        "dcx" => 2,
        "ecr" => 2,
        "iswap" => 2,
        "swap" => 2,
        "csx" => 2,
        # 3 qubit gates
        "cswap" => 3,
        "ccx" => 3
    )

    allPossibleGates = collect(keys(gatesAndQubitsMap))
    allPossibleGatesCount = length(allPossibleGates)

    for i in 1:numberOfOperations
        index = rand(1:allPossibleGatesCount)
        cgate = allPossibleGates[index]

        numberOfQubits = gatesAndQubitsMap[cgate]

        qubitsToUseForRandomCircuit = shuffle(qubitsToUseForRandomCircuit)
        cqubits = qubitsToUseForRandomCircuit[1:numberOfQubits]

        cparams = Float64[]
        if cgate in ["rx", "ry", "rz", "crx", "cry", "crz"]
            theta = rand() * 2 * π
            push!(cparams, theta)
        end

        push!(circuit.operations, Operation(cgate, cqubits, cparams))
    end
end


