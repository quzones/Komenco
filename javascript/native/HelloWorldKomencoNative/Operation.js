class Operation {
    constructor(gate, qubits, parameters) {
        this.gate = gate;
        this.qubits = qubits;
        this.params = parameters;
    }

    getGate() {
        return this.gate;
    }

    getQubits() {
        return this.qubits;
    }

    getParams() {
        return this.params;
    }
}

module.exports = Operation;