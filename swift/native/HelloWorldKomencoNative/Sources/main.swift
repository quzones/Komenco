import Foundation

// Assuming AutomatskiInitiumTabuSolver.swift exists and is in the same directory
// Include the AutomatskiInitiumTabuSolver class
// import AutomatskiInitiumTabuSolver


struct HelloWorldKomencoNative {

    static func main() async {
        // Create a sample quantum circuit to create a 3 Qubit GHZ State
        let circuit = QuantumCircuit(numQubits: 3)
        circuit.h(0)
        circuit.cx(0, qubit2: 1)
        circuit.cx(0, qubit2: 2)
        circuit.measureAll()

        // Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
        let sampler = AutomatskiKomencoNative(host: "103.212.120.18", port: 80)

        // Run the circuit and get results
        var measurements: [String: Int]
        do {
            measurements = try await sampler.run(circuit: circuit, repetitions: 100, topK: 20) // changed 1000 samples to 100 so that its easier to print the text histogram on screen
        } catch {
            print(error.localizedDescription)
            return
        }

        // Extract and count the measurement results
        print(measurements)

        let labels = measurements.keys.sorted()
        let values = labels.map { measurements[$0]! }

        // Plot the results using a simple text-based histogram
        print("Quantum States & Counts Histogram")
        print("---------------------------------")
        for (index, label) in labels.enumerated() {
            print("\(label.padding(toLength: 10, withPad: " ", startingAt: 0)): \(String(repeating: "*", count: values[index])) (\(values[index]))")
        }
    }

}

await HelloWorldKomencoNative.main()