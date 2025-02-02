import Foundation

class Operation {
    private var gate: String
    private var qubits: [Int]
    private var params: [Double]

    init(gate: String, qubits: [Int], params: [Double]) {
        self.gate = gate
        self.qubits = qubits
        self.params = params
    }

    func getGate() -> String {
        return gate
    }

    func getQubits() -> [Int] {
        return qubits
    }

    func getParams() -> [Double] {
        return params
    }
}