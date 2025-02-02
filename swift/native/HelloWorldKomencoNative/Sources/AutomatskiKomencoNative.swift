import Foundation
#if canImport(FoundationNetworking)
import FoundationNetworking
#endif

class AutomatskiKomencoNative {
    private var host: String
    private var port: Int

    init(host: String, port: Int) {
        self.host = host
        self.port = port
    }

    func run(circuit: QuantumCircuit, repetitions: Int, topK: Int) async throws -> [String: Int] {
        let tstart = Date()

        let body = try serializeCircuit(circuit: circuit, topK: topK)
        let struct_ = try await postRequest(body: body)

        let tend = Date()
        let executionTime = tend.timeIntervalSince(tstart) * 1000
        print("Time Taken \(executionTime)ms")

        if let error = struct_["error"] as? String {
            print(error)
            throw NSError(domain: "", code: 0, userInfo: [NSLocalizedDescriptionKey: error])
        }

        return try deserializeResult(responseData: struct_, repetitions: repetitions)
    }

    private func serializeCircuit(circuit: QuantumCircuit, topK: Int) throws -> [String: Any] {
        let numQubits = circuit.getNumQubits()

        var operations: [[String: Any]] = []
        var measurements: [Int] = []

        for operation in circuit.getOperations() {
            let gate = operation.getGate()
            let params = operation.getParams()
            let qubits = operation.getQubits()

            if gate == "measure" {
                measurements.append(contentsOf: qubits)
            } else {
                let op: [String: Any] = [
                    "gate": gate,
                    "params": params,
                    "qubits": qubits
                ]
                operations.append(op)
            }
        }

        print("Executing Quantum Circuit With...")
        print("\(numQubits) Qubits And ...")
        print("\(operations.count) Gates")

        if measurements.isEmpty {
            throw NSError(domain: "", code: 0, userInfo: [NSLocalizedDescriptionKey: "There are no measurements done at the end of the circuit."])
        }

        return [
            "num_qubits": numQubits,
            "operations": operations,
            "measurements": measurements,
            "topK": topK
        ]
    }

    private func postRequest(body: [String: Any]) async throws -> [String: Any] {
        let url = URL(string: "http://\(host):\(port)/api/komenco")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.setValue("application/json", forHTTPHeaderField: "Accept")
        request.httpBody = try JSONSerialization.data(withJSONObject: body, options: [])

        let (data, response) = try await URLSession.shared.data(for: request)

        guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
            throw NSError(domain: "", code: 0, userInfo: [NSLocalizedDescriptionKey: "Error making POST request"])
        }

        guard let jsonResponse = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any] else {
            throw NSError(domain: "", code: 0, userInfo: [NSLocalizedDescriptionKey: "Failed to parse JSON response"])
        }

        return jsonResponse
    }

    private func deserializeResult(responseData: [String: Any], repetitions: Int) throws -> [String: Int] {
        guard let measurementsStrings = responseData["measurements"] as? [String: Double] else {
            throw NSError(domain: "", code: 0, userInfo: [NSLocalizedDescriptionKey: "Invalid response data"])
        }

        var measurements: [String: Int] = [:]
        for (key, value) in measurementsStrings {
            let count = Int(round(value * Double(repetitions)))
            measurements[key] = count
        }

        return measurements
    }
}