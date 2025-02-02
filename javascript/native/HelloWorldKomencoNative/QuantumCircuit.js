const Operation = require('./Operation');

class QuantumCircuit {
    constructor(numQubits) {
        this.numQubits = numQubits;
        this.operations = [];
    }

    getNumQubits() {
        return this.numQubits;
    }

    getOperations() {
        return this.operations;
    }

    addSingle(gate, paramsList, qubits) {
        if (qubits.length !== 1) {
            throw new Error(`Number of qubits for gate ${gate} has to be one`);
        }
        for (const qubit of qubits) {
            if (qubit < 0 || qubit >= this.numQubits) {
                throw new Error(`Invalid qubit: ${qubit}`);
            }
        }
        this.operations.push(new Operation(gate, qubits, paramsList));
    }

    addDouble(gate, paramsList, qubits) {
        if (qubits.length !== 2) {
            throw new Error(`Number of qubits for gate ${gate} has to be two`);
        }
        for (const qubit of qubits) {
            if (qubit < 0 || qubit >= this.numQubits) {
                throw new Error(`Invalid qubit: ${qubit}`);
            }
        }
        this.operations.push(new Operation(gate, qubits, paramsList));
    }

    addTriple(gate, paramsList, qubits) {
        if (qubits.length !== 3) {
            throw new Error(`Number of qubits for gate ${gate} has to be three`);
        }
        for (const qubit of qubits) {
            if (qubit < 0 || qubit >= this.numQubits) {
                throw new Error(`Invalid qubit: ${qubit}`);
            }
        }
        this.operations.push(new Operation(gate, qubits, paramsList));
    }

    addMultiple(gate, paramsList, qubits) {
        const requiredQubits = Math.log2(gate.length);
        if (qubits.length !== requiredQubits) {
            throw new Error(`Number of qubits for gate ${gate} has to be ${requiredQubits}`);
        }
        for (const qubit of qubits) {
            if (qubit < 0 || qubit >= this.numQubits) {
                throw new Error(`Invalid qubit: ${qubit}`);
            }
        }
        this.operations.push(new Operation(gate, qubits, paramsList));
    }

    id(qubit1) {
        this.addSingle("id", [], [qubit1]);
    }

    x(qubit1) {
        this.addSingle("x", [], [qubit1]);
    }

    y(qubit1) {
        this.addSingle("y", [], [qubit1]);
    }

    z(qubit1) {
        this.addSingle("z", [], [qubit1]);
    }

    h(qubit1) {
        this.addSingle("h", [], [qubit1]);
    }

    s(qubit1) {
        this.addSingle("s", [], [qubit1]);
    }

    sdg(qubit1) {
        this.addSingle("sdg", [], [qubit1]);
    }

    t(qubit1) {
        this.addSingle("t", [], [qubit1]);
    }

    tdg(qubit1) {
        this.addSingle("tdg", [], [qubit1]);
    }

    rx(theta, qubit1) {
        this.addSingle("rx", [theta], [qubit1]);
    }

    ry(theta, qubit1) {
        this.addSingle("ry", [theta], [qubit1]);
    }

    rz(theta, qubit1) {
        this.addSingle("rz", [theta], [qubit1]);
    }

    u(theta, phi, lam, qubit1) {
        this.addSingle("u", [theta, phi, lam], [qubit1]);
    }

    u1(theta, qubit1) {
        this.addSingle("u1", [theta], [qubit1]);
    }

    u2(phi, lam, qubit1) {
        this.addSingle("u2", [phi, lam], [qubit1]);
    }

    u3(theta, phi, lam, qubit1) {
        this.addSingle("u3", [theta, phi, lam], [qubit1]);
    }

    sx(qubit1) {
        this.addSingle("sx", [], [qubit1]);
    }

    sxdg(qubit1) {
        this.addSingle("sxdg", [], [qubit1]);
    }

    r(theta, phi, qubit1) {
        this.addSingle("r", [theta, phi], [qubit1]);
    }

    cx(qubit1, qubit2) {
        this.addDouble("cx", [], [qubit1, qubit2]);
    }

    cy(qubit1, qubit2) {
        this.addDouble("cy", [], [qubit1, qubit2]);
    }

    cz(qubit1, qubit2) {
        this.addDouble("cz", [], [qubit1, qubit2]);
    }

    ch(qubit1, qubit2) {
        this.addDouble("ch", [], [qubit1, qubit2]);
    }

    ucrx(theta, qubit1, qubit2) {
        this.addDouble("ucrx", [theta], [qubit1, qubit2]);
    }

    ucry(theta, qubit1, qubit2) {
        this.addDouble("ucry", [theta], [qubit1, qubit2]);
    }

    ucrz(theta, qubit1, qubit2) {
        this.addDouble("ucrz", [theta], [qubit1, qubit2]);
    }

    crx(theta, qubit1, qubit2) {
        this.addDouble("crx", [theta], [qubit1, qubit2]);
    }

    cry(theta, qubit1, qubit2) {
        this.addDouble("cry", [theta], [qubit1, qubit2]);
    }

    crz(theta, qubit1, qubit2) {
        this.addDouble("crz", [theta], [qubit1, qubit2]);
    }

    cr(theta, phi, lam, qubit1, qubit2) {
        this.addDouble("cr", [theta, phi, lam], [qubit1, qubit2]);
    }

    cu(theta, phi, lam, gamma, qubit1, qubit2) {
        this.addDouble("cu1", [theta, phi, lam, gamma], [qubit1, qubit2]);
    }

    cu1(theta, qubit1, qubit2) {
        this.addDouble("cu1", [theta], [qubit1, qubit2]);
    }

    cu2(phi, lam, qubit1, qubit2) {
        this.addDouble("cu2", [phi, lam], [qubit1, qubit2]);
    }

    cu3(theta, phi, lam, qubit1, qubit2) {
        this.addDouble("cu3", [theta, phi, lam], [qubit1, qubit2]);
    }

    dcx(qubit1, qubit2) {
        this.addDouble("dcx", [], [qubit1, qubit2]);
    }

    ecr(qubit1, qubit2) {
        this.addDouble("ecr", [], [qubit1, qubit2]);
    }

    iswap(qubit1, qubit2) {
        this.addDouble("iswap", [], [qubit1, qubit2]);
    }

    rxx(theta, qubit1, qubit2) {
        this.addDouble("rxx", [theta], [qubit1, qubit2]);
    }

    ryy(theta, qubit1, qubit2) {
        this.addDouble("ryy", [theta], [qubit1, qubit2]);
    }

    rzz(theta, qubit1, qubit2) {
        this.addDouble("rzz", [theta], [qubit1, qubit2]);
    }

    rzx(theta, qubit1, qubit2) {
        this.addDouble("rzx", [theta], [qubit1, qubit2]);
    }

    cswap(qubit1, qubit2, qubit3) {
        this.addTriple("cswap", [], [qubit1, qubit2, qubit3]);
    }

    ccx(qubit1, qubit2, qubit3) {
        this.addTriple("ccx", [], [qubit1, qubit2, qubit3]);
    }

    ccy(qubit1, qubit2, qubit3) {
        this.addTriple("ccy", [], [qubit1, qubit2, qubit3]);
    }

    ccz(qubit1, qubit2, qubit3) {
        this.addTriple("ccz", [], [qubit1, qubit2, qubit3]);
    }

    c3x(qubits) {
        this.addMultiple("c3x", [], qubits);
    }

    c4x(qubits) {
        this.addMultiple("c4x", [], qubits);
    }

    mcx(qubits) {
        this.addMultiple("mcx", [], qubits);
    }

    mcu1(theta, qubits) {
        this.addMultiple("mcu1", [theta], qubits);
    }

    mcu2(phi, lam, qubits) {
        this.addMultiple("mcu2", [phi, lam], qubits);
    }

    mcu3(theta, phi, lam, qubits) {
        this.addMultiple("mcu3", [theta, phi, lam], qubits);
    }

    mcz(qubits) {
        this.addMultiple("mcz", [], qubits);
    }

    mcp(qubits) {
        this.addMultiple("mcp", [], qubits);
    }

    mcrx(qubits) {
        this.addMultiple("mcrx", [], qubits);
    }

    mcry(qubits) {
        this.addMultiple("mcry", [], qubits);
    }

    mcrz(qubits) {
        this.addMultiple("mcrz", [], qubits);
    }

    qft(qubits) {
        this.addMultiple("qft", [], qubits);
    }

    inverseQft(qubits) {
        this.addMultiple("iqft", [], qubits);
    }

    swap(qubit1, qubit2) {
        this.addDouble("swap", [], [qubit1, qubit2]);
    }

    csx(qubit1, qubit2) {
        this.addDouble("csx", [], [qubit1, qubit2]);
    }

    p(theta, qubit1) {
        this.addSingle("p", [theta], [qubit1]);
    }

    cp(theta, qubit1, qubit2) {
        this.addDouble("cp", [theta], [qubit1, qubit2]);
    }

    ccp(theta, qubit1, qubit2, qubit3) {
        this.addTriple("ccp", [theta], [qubit1, qubit2, qubit3]);
    }

    sqrtX(qubit1) {
        this.addSingle("sqrt_x", [], [qubit1]);
    }

    sqrtY(qubit1) {
        this.addSingle("sqrt_y", [], [qubit1]);
    }

    sqrtZ(qubit1) {
        this.addSingle("sqrt_z", [], [qubit1]);
    }

    gpi(phi, qubit1) {
        this.addSingle("gpi", [phi], [qubit1]);
    }

    gpi2(phi, qubit1) {
        this.addSingle("gpi2", [phi], [qubit1]);
    }

    xp(theta, qubit1) {
        this.addSingle("xp", [theta], [qubit1]);
    }

    yp(theta, qubit1) {
        this.addSingle("yp", [theta], [qubit1]);
    }

    zp(theta, qubit1) {
        this.addSingle("zp", [theta], [qubit1]);
    }

    xxp(theta, qubit1, qubit2) {
        this.addDouble("xxp", [theta], [qubit1, qubit2]);
    }

    yyp(theta, qubit1, qubit2) {
        this.addDouble("yyp", [theta], [qubit1, qubit2]);
    }

    zzp(theta, qubit1, qubit2) {
        this.addDouble("zzp", [theta], [qubit1, qubit2]);
    }

    phasedXp(theta, phi, qubit1) {
        this.addSingle("phased_xp", [theta, phi], [qubit1]);
    }

    phasedYp(theta, phi, qubit1) {
        this.addSingle("phased_yp", [theta, phi], [qubit1]);
    }

    phasedZp(theta, phi, qubit1) {
        this.addSingle("phased_zp", [theta, phi], [qubit1]);
    }

    cnotp(theta, qubit1, qubit2) {
        this.addDouble("cnotp", [theta], [qubit1, qubit2]);
    }

    ccnotp(theta, qubit1, qubit2, qubit3) {
        this.addTriple("ccnotp", [theta], [qubit1, qubit2, qubit3]);
    }

    cyp(theta, qubit1, qubit2) {
        this.addDouble("cyp", [theta], [qubit1, qubit2]);
    }

    ccyp(theta, qubit1, qubit2, qubit3) {
        this.addTriple("ccyp", [theta], [qubit1, qubit2, qubit3]);
    }

    czp(theta, qubit1, qubit2) {
        this.addDouble("czp", [theta], [qubit1, qubit2]);
    }

    cczp(theta, qubit1, qubit2, qubit3) {
        this.addTriple("cczp", [theta], [qubit1, qubit2, qubit3]);
    }

    measure(qubits) {
        if (qubits.length === 0) {
            throw new Error("number of qubits to measure cannot be zero");
        }

        const cqubits = [];
        for (const qubit of qubits) {
            if (qubit < 0 || qubit >= this.numQubits) {
                throw new Error(`invalid qubit: ${qubit}`);
            }
            cqubits.push(qubit);
        }

        this.operations.push(new Operation("measure", cqubits, []));
    }

    measureAll() {
        const cqubits = [];
        for (let qubit = 0; qubit < this.numQubits; qubit++) {
            cqubits.push(qubit);
        }

        this.operations.push(new Operation("measure", cqubits, []));
    }

    randomCircuit(numberOfOperations, qubitsToUseForRandomCircuit) {
        const qubitsCount = qubitsToUseForRandomCircuit.length;
        if (qubitsCount < 3) {
            throw new Error("The number of qubits needed to generate random circuits is >= 3");
        }

        const gatesAndQubitsMap = {
            // 1 qubit gates
            "x": 1,
            "y": 1,
            "z": 1,
            "rx": 1,
            "ry": 1,
            "rz": 1,
            "h": 1,
            "s": 1,
            "sdg": 1,
            "t": 1,
            "tdg": 1,
            "sx": 1,
            "sxdg": 1,
            // 2 qubit gates
            "cx": 2,
            "cy": 2,
            "cz": 2,
            "crx": 2,
            "cry": 2,
            "crz": 2,
            "ch": 2,
            "dcx": 2,
            "ecr": 2,
            "iswap": 2,
            "swap": 2,
            "csx": 2,
            // 3 qubit gates
            "cswap": 3,
            "ccx": 3
        };

        const allPossibleGates = Object.keys(gatesAndQubitsMap);
        const allPossibleGatesCount = allPossibleGates.length;

        for (let i = 0; i < numberOfOperations; i++) {
            const index = Math.floor(Math.random() * allPossibleGatesCount);
            const cgate = allPossibleGates[index];

            const numberOfQubits = gatesAndQubitsMap[cgate];

            qubitsToUseForRandomCircuit = qubitsToUseForRandomCircuit.sort(() => Math.random() - 0.5);
            const cqubits = qubitsToUseForRandomCircuit.slice(0, numberOfQubits);

            const cparams = [];
            if (["rx", "ry", "rz", "crx", "cry", "crz"].includes(cgate)) {
                const theta = Math.random() * 2 * Math.PI;
                cparams.push(theta);
            }

            this.operations.push(new Operation(cgate, cqubits, cparams));
        }
    }
}    

module.exports = QuantumCircuit;