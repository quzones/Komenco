using HTTP
using JSON
using Dates

include("QuantumCircuitMod.jl")




mutable struct AutomatskiKomencoNative
    host::String
    port::Int
end



function run(sampler::AutomatskiKomencoNative, circuit::QuantumCircuit, repetitions::Int, topK::Int)
    tstart = now()

    body = serialize_circuit(circuit, topK)
    struct_data = post_request(sampler, body)

    tend = now()
    execution_time = (tend - tstart).value
    println("Time Taken $execution_time ms")

    if haskey(struct_data, "error")
        println(struct_data["error"])
        throw(Exception(struct_data["error"]))
    end

    return deserialize_result(struct_data, repetitions)
end

function serialize_circuit(circuit::QuantumCircuit, topK::Int)
    num_qubits = get_num_qubits(circuit)

    operations = []
    measurements = []

    for operation in get_operations(circuit)
        gate = get_gate(operation)
        params_list = get_params(operation)
        qubits = get_qubits(operation)

        if gate == "measure"
            append!(measurements, qubits)
        else
            op = Dict("gate" => gate, "params" => params_list, "qubits" => qubits)
            push!(operations, op)
        end
    end

    println("Executing Quantum Circuit With...")
    println("$num_qubits Qubits And ...")
    println("$(length(operations)) Gates")

    if length(measurements) == 0
        throw(Exception("There are no measurements done at the end of the circuit."))
    end

    json = Dict(
        "num_qubits" => num_qubits,
        "operations" => operations,
        "measurements" => measurements,
        "topK" => topK
    )

    return json
end

function post_request(sampler::AutomatskiKomencoNative, body::Dict)
    url = "http://$(sampler.host):$(sampler.port)/api/komenco"
    headers = ["Content-Type" => "application/json; utf-8", "Accept" => "application/json"]
    response = HTTP.post(url, headers, JSON.json(body))
    response_data = JSON.parse(String(response.body))
    return response_data
end

function deserialize_result(response_data::Dict, repetitions::Int)
    measurements_strings = response_data["measurements"]

    measurements = Dict{String, Int}()
    for (key, value) in measurements_strings
        count = round(Int, value * repetitions)
        measurements[key] = count
    end

    return measurements
end
