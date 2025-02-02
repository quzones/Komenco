import Foundation

class QuantumCircuit {
    private var numQubits: Int
    private var operations: [Operation]

    init(numQubits: Int) {
        self.numQubits = numQubits
        self.operations = []
    }

    func getNumQubits() -> Int {
        return numQubits
    }

    func getOperations() -> [Operation] {
        return operations
    }

    private func addSingle(gate: String, params: [Double], qubits: [Int]) {
        guard qubits.count == 1 else {
            fatalError("Number of qubits for gate \(gate) has to be one")
        }
        for qubit in qubits {
            guard qubit >= 0 && qubit < numQubits else {
                fatalError("Invalid qubit: \(qubit)")
            }
        }
        operations.append(Operation(gate: gate, qubits: qubits, params: params))
    }

    private func addDouble(gate: String, params: [Double], qubits: [Int]) {
        guard qubits.count == 2 else {
            fatalError("Number of qubits for gate \(gate) has to be two")
        }
        for qubit in qubits {
            guard qubit >= 0 && qubit < numQubits else {
                fatalError("Invalid qubit: \(qubit)")
            }
        }
        operations.append(Operation(gate: gate, qubits: qubits, params: params))
    }

    private func addTriple(gate: String, params: [Double], qubits: [Int]) {
        guard qubits.count == 3 else {
            fatalError("Number of qubits for gate \(gate) has to be three")
        }
        for qubit in qubits {
            guard qubit >= 0 && qubit < numQubits else {
                fatalError("Invalid qubit: \(qubit)")
            }
        }
        operations.append(Operation(gate: gate, qubits: qubits, params: params))
    }

    private func addMultiple(gate: String, params: [Double], qubits: [Int]) {
        let requiredQubits = Int(log(Double(gate.count)) / log(2.0))
        guard qubits.count == requiredQubits else {
            fatalError("Number of qubits for gate \(gate) has to be \(requiredQubits)")
        }
        for qubit in qubits {
            guard qubit >= 0 && qubit < numQubits else {
                fatalError("Invalid qubit: \(qubit)")
            }
        }
        operations.append(Operation(gate: gate, qubits: qubits, params: params))
    }

    func id(_ qubit1: Int) {
        addSingle(gate: "id", params: [], qubits: [qubit1])
    }

    func x(_ qubit1: Int) {
        addSingle(gate: "x", params: [], qubits: [qubit1])
    }

    func y(_ qubit1: Int) {
        addSingle(gate: "y", params: [], qubits: [qubit1])
    }

    func z(_ qubit1: Int) {
        addSingle(gate: "z", params: [], qubits: [qubit1])
    }

    func h(_ qubit1: Int) {
        addSingle(gate: "h", params: [], qubits: [qubit1])
    }

    func s(_ qubit1: Int) {
        addSingle(gate: "s", params: [], qubits: [qubit1])
    }

    func sdg(_ qubit1: Int) {
        addSingle(gate: "sdg", params: [], qubits: [qubit1])
    }

    func t(_ qubit1: Int) {
        addSingle(gate: "t", params: [], qubits: [qubit1])
    }

    func tdg(_ qubit1: Int) {
        addSingle(gate: "tdg", params: [], qubits: [qubit1])
    }

    func rx(_ theta: Double, qubit1: Int) {
        addSingle(gate: "rx", params: [theta], qubits: [qubit1])
    }

    func ry(_ theta: Double, qubit1: Int) {
        addSingle(gate: "ry", params: [theta], qubits: [qubit1])
    }

    func rz(_ theta: Double, qubit1: Int) {
        addSingle(gate: "rz", params: [theta], qubits: [qubit1])
    }

    func u(_ theta: Double, phi: Double, lam: Double, qubit1: Int) {
        addSingle(gate: "u", params: [theta, phi, lam], qubits: [qubit1])
    }

    func u1(_ theta: Double, qubit1: Int) {
        addSingle(gate: "u1", params: [theta], qubits: [qubit1])
    }

    func u2(_ phi: Double, lam: Double, qubit1: Int) {
        addSingle(gate: "u2", params: [phi, lam], qubits: [qubit1])
    }

    func u3(_ theta: Double, phi: Double, lam: Double, qubit1: Int) {
        addSingle(gate: "u3", params: [theta, phi, lam], qubits: [qubit1])
    }

    func sx(_ qubit1: Int) {
        addSingle(gate: "sx", params: [], qubits: [qubit1])
    }

    func sxdg(_ qubit1: Int) {
        addSingle(gate: "sxdg", params: [], qubits: [qubit1])
    }

    func r(_ theta: Double, phi: Double, qubit1: Int) {
        addSingle(gate: "r", params: [theta, phi], qubits: [qubit1])
    }

    func cx(_ qubit1: Int, qubit2: Int) {
        addDouble(gate: "cx", params: [], qubits: [qubit1, qubit2])
    }

    func cy(_ qubit1: Int, qubit2: Int) {
        addDouble(gate: "cy", params: [], qubits: [qubit1, qubit2])
    }

    func cz(_ qubit1: Int, qubit2: Int) {
        addDouble(gate: "cz", params: [], qubits: [qubit1, qubit2])
    }

    func ch(_ qubit1: Int, qubit2: Int) {
        addDouble(gate: "ch", params: [], qubits: [qubit1, qubit2])
    }

    func ucrx(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "ucrx", params: [theta], qubits: [qubit1, qubit2])
    }

    func ucry(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "ucry", params: [theta], qubits: [qubit1, qubit2])
    }

    func ucrz(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "ucrz", params: [theta], qubits: [qubit1, qubit2])
    }

    func crx(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "crx", params: [theta], qubits: [qubit1, qubit2])
    }

    func cry(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "cry", params: [theta], qubits: [qubit1, qubit2])
    }

    func crz(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "crz", params: [theta], qubits: [qubit1, qubit2])
    }

    func cr(_ theta: Double, phi: Double, lam: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "cr", params: [theta, phi, lam], qubits: [qubit1, qubit2])
    }

    func cu(_ theta: Double, phi: Double, lam: Double, gamma: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "cu1", params: [theta, phi, lam, gamma], qubits: [qubit1, qubit2])
    }

    func cu1(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "cu1", params: [theta], qubits: [qubit1, qubit2])
    }

    func cu2(_ phi: Double, lam: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "cu2", params: [phi, lam], qubits: [qubit1, qubit2])
    }

    func cu3(_ theta: Double, phi: Double, lam: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "cu3", params: [theta, phi, lam], qubits: [qubit1, qubit2])
    }

    func dcx(_ qubit1: Int, qubit2: Int) {
        addDouble(gate: "dcx", params: [], qubits: [qubit1, qubit2])
    }

    func ecr(_ qubit1: Int, qubit2: Int) {
        addDouble(gate: "ecr", params: [], qubits: [qubit1, qubit2])
    }

    func iswap(_ qubit1: Int, qubit2: Int) {
        addDouble(gate: "iswap", params: [], qubits: [qubit1, qubit2])
    }

    func rxx(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "rxx", params: [theta], qubits: [qubit1, qubit2])
    }

    func ryy(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "ryy", params: [theta], qubits: [qubit1, qubit2])
    }

    func rzz(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "rzz", params: [theta], qubits: [qubit1, qubit2])
    }

    func rzx(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "rzx", params: [theta], qubits: [qubit1, qubit2])
    }

    func cswap(_ qubit1: Int, qubit2: Int, qubit3: Int) {
        addTriple(gate: "cswap", params: [], qubits: [qubit1, qubit2, qubit3])
    }

    func ccx(_ qubit1: Int, qubit2: Int, qubit3: Int) {
        addTriple(gate: "ccx", params: [], qubits: [qubit1, qubit2, qubit3])
    }

    func ccy(_ qubit1: Int, qubit2: Int, qubit3: Int) {
        addTriple(gate: "ccy", params: [], qubits: [qubit1, qubit2, qubit3])
    }

    func ccz(_ qubit1: Int, qubit2: Int, qubit3: Int) {
        addTriple(gate: "ccz", params: [], qubits: [qubit1, qubit2, qubit3])
    }

    func c3x(_ qubits: [Int]) {
        addMultiple(gate: "c3x", params: [], qubits: qubits)
    }

    func c4x(_ qubits: [Int]) {
        addMultiple(gate: "c4x", params: [], qubits: qubits)
    }

    func mcx(_ qubits: [Int]) {
        addMultiple(gate: "mcx", params: [], qubits: qubits)
    }

    func mcu1(_ theta: Double, qubits: [Int]) {
        addMultiple(gate: "mcu1", params: [theta], qubits: qubits)
    }

    func mcu2(_ phi: Double, lam: Double, qubits: [Int]) {
        addMultiple(gate: "mcu2", params: [phi, lam], qubits: qubits)
    }

    func mcu3(_ theta: Double, phi: Double, lam: Double, qubits: [Int]) {
        addMultiple(gate: "mcu3", params: [theta, phi, lam], qubits: qubits)
    }

    func mcz(_ qubits: [Int]) {
        addMultiple(gate: "mcz", params: [], qubits: qubits)
    }

    func mcp(_ qubits: [Int]) {
        addMultiple(gate: "mcp", params: [], qubits: qubits)
    }

    func mcrx(_ qubits: [Int]) {
        addMultiple(gate: "mcrx", params: [], qubits: qubits)
    }

    func mcry(_ qubits: [Int]) {
        addMultiple(gate: "mcry", params: [], qubits: qubits)
    }

    func mcrz(_ qubits: [Int]) {
        addMultiple(gate: "mcrz", params: [], qubits: qubits)
    }

    func qft(_ qubits: [Int]) {
        addMultiple(gate: "qft", params: [], qubits: qubits)
    }

    func inverse_qft(_ qubits: [Int]) {
        addMultiple(gate: "iqft", params: [], qubits: qubits)
    }

    func swap(_ qubit1: Int, qubit2: Int) {
        addDouble(gate: "swap", params: [], qubits: [qubit1, qubit2])
    }

    func csx(_ qubit1: Int, qubit2: Int) {
        addDouble(gate: "csx", params: [], qubits: [qubit1, qubit2])
    }

    func p(_ theta: Double, qubit1: Int) {
        addSingle(gate: "p", params: [theta], qubits: [qubit1])
    }

    func cp(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "cp", params: [theta], qubits: [qubit1, qubit2])
    }

    func ccp(_ theta: Double, qubit1: Int, qubit2: Int, qubit3: Int) {
        addTriple(gate: "ccp", params: [theta], qubits: [qubit1, qubit2, qubit3])
    }

    func sqrt_x(_ qubit1: Int) {
        addSingle(gate: "sqrt_x", params: [], qubits: [qubit1])
    }

    func sqrt_y(_ qubit1: Int) {
        addSingle(gate: "sqrt_y", params: [], qubits: [qubit1])
    }

    func sqrt_z(_ qubit1: Int) {
        addSingle(gate: "sqrt_z", params: [], qubits: [qubit1])
    }

    func gpi(_ phi: Double, qubit1: Int) {
        addSingle(gate: "gpi", params: [phi], qubits: [qubit1])
    }

    func gpi2(_ phi: Double, qubit1: Int) {
        addSingle(gate: "gpi2", params: [phi], qubits: [qubit1])
    }

    func xp(_ theta: Double, qubit1: Int) {
        addSingle(gate: "xp", params: [theta], qubits: [qubit1])
    }

    func yp(_ theta: Double, qubit1: Int) {
        addSingle(gate: "yp", params: [theta], qubits: [qubit1])
    }

    func zp(_ theta: Double, qubit1: Int) {
        addSingle(gate: "zp", params: [theta], qubits: [qubit1])
    }

    func xxp(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "xxp", params: [theta], qubits: [qubit1, qubit2])
    }

    func yyp(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "yyp", params: [theta], qubits: [qubit1, qubit2])
    }

    func zzp(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "zzp", params: [theta], qubits: [qubit1, qubit2])
    }

    func phased_xp(_ theta: Double, phi: Double, qubit1: Int) {
        addSingle(gate: "phased_xp", params: [theta, phi], qubits: [qubit1])
    }

    func phased_yp(_ theta: Double, phi: Double, qubit1: Int) {
        addSingle(gate: "phased_yp", params: [theta, phi], qubits: [qubit1])
    }

    func phased_zp(_ theta: Double, phi: Double, qubit1: Int) {
        addSingle(gate: "phased_zp", params: [theta, phi], qubits: [qubit1])
    }

    func cnotp(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "cnotp", params: [theta], qubits: [qubit1, qubit2])
    }

    func ccnotp(_ theta: Double, qubit1: Int, qubit2: Int, qubit3: Int) {
        addTriple(gate: "ccnotp", params: [theta], qubits: [qubit1, qubit2, qubit3])
    }

    func cyp(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "cyp", params: [theta], qubits: [qubit1, qubit2])
    }

    func ccyp(_ theta: Double, qubit1: Int, qubit2: Int, qubit3: Int) {
        addTriple(gate: "ccyp", params: [theta], qubits: [qubit1, qubit2, qubit3])
    }

    func czp(_ theta: Double, qubit1: Int, qubit2: Int) {
        addDouble(gate: "czp", params: [theta], qubits: [qubit1, qubit2])
    }

    func cczp(_ theta: Double, qubit1: Int, qubit2: Int, qubit3: Int) {
        addTriple(gate: "cczp", params: [theta], qubits: [qubit1, qubit2, qubit3])
    }

    func measure(_ qubits: [Int]) {
        var cparams: [Double] = []
        var cqubits: [Int] = []
        let cgate = "measure"
        if qubits.isEmpty {
            fatalError("number of qubits to measure cannot be zero")
        } else {
            for qubit in qubits {
                if qubit < 0 || qubit >= numQubits {
                    fatalError("invalid qubit: \(qubit)")
                } else {
                    cqubits.append(qubit)
                }
            }
        }
        operations.append(Operation(gate: cgate, qubits: cqubits, params: cparams))
    }

    func measureAll() {
        var cparams: [Double] = []
        var cqubits: [Int] = []
        let cgate = "measure"
        for qubit in 0..<numQubits {
            cqubits.append(qubit)
        }
        operations.append(Operation(gate: cgate, qubits: cqubits, params: cparams))
    }

    func randomCircuit(_ numberOfOperations: Int, qubitsToUseForRandomCircuit: [Int]) {
        let qubitsCount = qubitsToUseForRandomCircuit.count
        if qubitsCount < 3 {
            fatalError("The number of qubits needed to generate random circuits is >= 3")
        }

        let gatesAndQubitsMap: [String: Int] = [
            // 1 qubit gates
            "x": 1, "y": 1, "z": 1, "rx": 1, "ry": 1, "rz": 1,
            "h": 1, "s": 1, "sdg": 1, "t": 1, "tdg": 1, "sx": 1, "sxdg": 1,
            // 2 qubit gates
            "cx": 2, "cy": 2, "cz": 2, "crx": 2, "cry": 2, "crz": 2,
            "ch": 2, "dcx": 2, "ecr": 2, "iswap": 2, "swap": 2, "csx": 2,
            // 3 qubit gates
            "cswap": 3, "ccx": 3
        ]

        let allPossibleGates = Array(gatesAndQubitsMap.keys)
        let allPossibleGatesCount = allPossibleGates.count

        for _ in 0..<numberOfOperations {
            let index = Int.random(in: 0..<allPossibleGatesCount)
            let cgate = allPossibleGates[index]

            let numberOfQubits = gatesAndQubitsMap[cgate]!

            var shuffledQubits = qubitsToUseForRandomCircuit.shuffled()
            let cqubits = Array(shuffledQubits.prefix(numberOfQubits))

            var cparams: [Double] = []
            if ["rx", "ry", "rz", "crx", "cry", "crz"].contains(cgate) {
                let theta = Double.random(in: 0...(2 * Double.pi))
                cparams.append(theta)
            }

            operations.append(Operation(gate: cgate, qubits: cqubits, params: cparams))
        }
    }

}