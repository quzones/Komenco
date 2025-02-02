using Plots
using JSON

include("AutomatskiKomencoNativeMod.jl")
include("QuantumCircuitMod.jl")


function main()
    # Create a sample quantum circuit to create a 3 Qubit GHZ State
    circuit = QuantumCircuit(3)
    h(circuit, 0)
    cx(circuit, 0, 1)
    cx(circuit, 0, 2)
    measure_all(circuit)

    # Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
    sampler = AutomatskiKomencoNative("103.212.120.18", 80)

    # Run the circuit and get results
    results = Dict{String, Int}()
    try
        results = run(sampler, circuit, 1000, 20)
    catch e
        println(e)
        return
    end

    # Extract and count the measurement results
    measurements = results
    println(measurements)

    labels = sort(collect(keys(measurements)))
    values = [measurements[label] for label in labels]

    # Plot the results
    bar(labels, values, legend=false, title="Quantum States & Counts Histogram", xlabel="Measurement Outcomes", ylabel="Counts")

    # Save the plot to an HTML file
    savefig("chart.html")
    println("Chart saved to chart.html")
end

main()