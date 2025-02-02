const axios = require('axios');
const BigNumber = require('bignumber.js');

class AutomatskiKomencoNative {
    constructor(host, port) {
        this.host = host;
        this.port = port;
    }

    async run(circuit, repetitions, topK) {
        const tstart = Date.now();

        const body = this.serializeCircuit(circuit, topK);
        const structData = await this.postRequest(body);

        const tend = Date.now();
        const executionTime = tend - tstart;
        console.log(`Time Taken ${executionTime}ms`);

        if (structData.error) {
            console.error(structData.error);
            throw new Error(structData.error);
        }

        return this.deserializeResult(structData, repetitions);
    }

    serializeCircuit(circuit, topK) {
        const numQubits = circuit.getNumQubits();

        const operations = [];
        const measurements = [];

        for (const operation of circuit.getOperations()) {
            const gate = operation.getGate();
            const paramsList = operation.getParams();
            const qubits = operation.getQubits();

            if (gate === 'measure') {
                measurements.push(...qubits);
            } else {
                const op = {
                    gate: gate,
                    params: paramsList,
                    qubits: qubits
                };
                operations.push(op);
            }
        }

        console.log('Executing Quantum Circuit With...');
        console.log(`${numQubits} Qubits And ...`);
        console.log(`${operations.length} Gates`);

        if (measurements.length === 0) {
            throw new Error('There are no measurements done at the end of the circuit.');
        }

        const json = {
            num_qubits: numQubits,
            operations: operations,
            measurements: measurements,
            topK: topK
        };

        return json;
    }

    async postRequest(body) {
        const url = `http://${this.host}:${this.port}/api/komenco`;
        const response = await axios.post(url, body, {
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'Accept': 'application/json'
            },
            transformResponse: [data => JSON.parse(data)]
        });

        return response.data;
    }
   
    deserializeResult(responseData, repetitions) {
        const measurementsStrings = responseData.measurements;
    
        const measurements = {};
        for (const key in measurementsStrings) {
            if (Object.prototype.hasOwnProperty.call(measurementsStrings, key)) {
                measurements[key] = Math.round(measurementsStrings[key] * repetitions);
            }
        }
    
        return measurements;
    }
}

module.exports = AutomatskiKomencoNative;