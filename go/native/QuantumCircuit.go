package main

import (
    "fmt"
    "math"
    "math/rand"
    "time"
)
type QuantumCircuit struct {
    numQubits  int
    operations []Operation
}

func NewQuantumCircuit(numQubits int) *QuantumCircuit {
    return &QuantumCircuit{
        numQubits:  numQubits,
        operations: []Operation{},
    }
}

func (qc *QuantumCircuit) GetNumQubits() int {
    return qc.numQubits
}

func (qc *QuantumCircuit) GetOperations() []Operation {
    return qc.operations
}

func (qc *QuantumCircuit) addSingle(gate string, params []float64, qubits []int) {
    if len(qubits) != 1 {
        panic(fmt.Sprintf("Number of qubits for gate %s has to be one", gate))
    }
    for _, qubit := range qubits {
        if qubit < 0 || qubit >= qc.numQubits {
            panic(fmt.Sprintf("Invalid qubit: %d", qubit))
        }
    }
    qc.operations = append(qc.operations, Operation{gate, qubits, params})
}

func (qc *QuantumCircuit) addDouble(gate string, params []float64, qubits []int) {
    if len(qubits) != 2 {
        panic(fmt.Sprintf("Number of qubits for gate %s has to be two", gate))
    }
    for _, qubit := range qubits {
        if qubit < 0 || qubit >= qc.numQubits {
            panic(fmt.Sprintf("Invalid qubit: %d", qubit))
        }
    }
    qc.operations = append(qc.operations, Operation{gate, qubits, params})
}

func (qc *QuantumCircuit) addTriple(gate string, params []float64, qubits []int) {
    if len(qubits) != 3 {
        panic(fmt.Sprintf("Number of qubits for gate %s has to be three", gate))
    }
    for _, qubit := range qubits {
        if qubit < 0 || qubit >= qc.numQubits {
            panic(fmt.Sprintf("Invalid qubit: %d", qubit))
        }
    }
    qc.operations = append(qc.operations, Operation{gate, qubits, params})
}

func (qc *QuantumCircuit) addMultiple(gate string, params []float64, qubits []int) {
    requiredQubits := int(math.Log2(float64(len(gate))))
    if len(qubits) != requiredQubits {
        panic(fmt.Sprintf("Number of qubits for gate %s has to be %d", gate, requiredQubits))
    }
    for _, qubit := range qubits {
        if qubit < 0 || qubit >= qc.numQubits {
            panic(fmt.Sprintf("Invalid qubit: %d", qubit))
        }
    }
    qc.operations = append(qc.operations, Operation{gate, qubits, params})
}

func (qc *QuantumCircuit) Id(qubit1 int) {
    qc.addSingle("id", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) X(qubit1 int) {
    qc.addSingle("x", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) Y(qubit1 int) {
    qc.addSingle("y", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) Z(qubit1 int) {
    qc.addSingle("z", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) H(qubit1 int) {
    qc.addSingle("h", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) S(qubit1 int) {
    qc.addSingle("s", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) Sdg(qubit1 int) {
    qc.addSingle("sdg", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) T(qubit1 int) {
    qc.addSingle("t", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) Tdg(qubit1 int) {
    qc.addSingle("tdg", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) Rx(theta float64, qubit1 int) {
    qc.addSingle("rx", []float64{theta}, []int{qubit1})
}

func (qc *QuantumCircuit) Ry(theta float64, qubit1 int) {
    qc.addSingle("ry", []float64{theta}, []int{qubit1})
}

func (qc *QuantumCircuit) Rz(theta float64, qubit1 int) {
    qc.addSingle("rz", []float64{theta}, []int{qubit1})
}

func (qc *QuantumCircuit) U(theta, phi, lam float64, qubit1 int) {
    qc.addSingle("u", []float64{theta, phi, lam}, []int{qubit1})
}

func (qc *QuantumCircuit) U1(theta float64, qubit1 int) {
    qc.addSingle("u1", []float64{theta}, []int{qubit1})
}

func (qc *QuantumCircuit) U2(phi, lam float64, qubit1 int) {
    qc.addSingle("u2", []float64{phi, lam}, []int{qubit1})
}

func (qc *QuantumCircuit) U3(theta, phi, lam float64, qubit1 int) {
    qc.addSingle("u3", []float64{theta, phi, lam}, []int{qubit1})
}

func (qc *QuantumCircuit) Sx(qubit1 int) {
    qc.addSingle("sx", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) Sxdg(qubit1 int) {
    qc.addSingle("sxdg", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) R(theta, phi float64, qubit1 int) {
    qc.addSingle("r", []float64{theta, phi}, []int{qubit1})
}

func (qc *QuantumCircuit) Cx(qubit1, qubit2 int) {
    qc.addDouble("cx", []float64{}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Cy(qubit1, qubit2 int) {
    qc.addDouble("cy", []float64{}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Cz(qubit1, qubit2 int) {
    qc.addDouble("cz", []float64{}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Ch(qubit1, qubit2 int) {
    qc.addDouble("ch", []float64{}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Ucrx(theta float64, qubit1, qubit2 int) {
    qc.addDouble("ucrx", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Ucry(theta float64, qubit1, qubit2 int) {
    qc.addDouble("ucry", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Ucrz(theta float64, qubit1, qubit2 int) {
    qc.addDouble("ucrz", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Crx(theta float64, qubit1, qubit2 int) {
    qc.addDouble("crx", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Cry(theta float64, qubit1, qubit2 int) {
    qc.addDouble("cry", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Crz(theta float64, qubit1, qubit2 int) {
    qc.addDouble("crz", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Cr(theta, phi, lam float64, qubit1, qubit2 int) {
    qc.addDouble("cr", []float64{theta, phi, lam}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Cu(theta, phi, lam, gamma float64, qubit1, qubit2 int) {
    qc.addDouble("cu1", []float64{theta, phi, lam, gamma}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Cu1(theta float64, qubit1, qubit2 int) {
    qc.addDouble("cu1", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Cu2(phi, lam float64, qubit1, qubit2 int) {
    qc.addDouble("cu2", []float64{phi, lam}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Cu3(theta, phi, lam float64, qubit1, qubit2 int) {
    qc.addDouble("cu3", []float64{theta, phi, lam}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Dcx(qubit1, qubit2 int) {
    qc.addDouble("dcx", []float64{}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Ecr(qubit1, qubit2 int) {
    qc.addDouble("ecr", []float64{}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Iswap(qubit1, qubit2 int) {
    qc.addDouble("iswap", []float64{}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Rxx(theta float64, qubit1, qubit2 int) {
    qc.addDouble("rxx", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Ryy(theta float64, qubit1, qubit2 int) {
    qc.addDouble("ryy", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Rzz(theta float64, qubit1, qubit2 int) {
    qc.addDouble("rzz", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Rzx(theta float64, qubit1, qubit2 int) {
    qc.addDouble("rzx", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Cswap(qubit1, qubit2, qubit3 int) {
    qc.addTriple("cswap", []float64{}, []int{qubit1, qubit2, qubit3})
}

func (qc *QuantumCircuit) Ccx(qubit1, qubit2, qubit3 int) {
    qc.addTriple("ccx", []float64{}, []int{qubit1, qubit2, qubit3})
}

func (qc *QuantumCircuit) Ccy(qubit1, qubit2, qubit3 int) {
    qc.addTriple("ccy", []float64{}, []int{qubit1, qubit2, qubit3})
}

func (qc *QuantumCircuit) Ccz(qubit1, qubit2, qubit3 int) {
    qc.addTriple("ccz", []float64{}, []int{qubit1, qubit2, qubit3})
}

func (qc *QuantumCircuit) C3x(qubits []int) {
    qc.addMultiple("c3x", []float64{}, qubits)
}

func (qc *QuantumCircuit) C4x(qubits []int) {
    qc.addMultiple("c4x", []float64{}, qubits)
}

func (qc *QuantumCircuit) Mcx(qubits []int) {
    qc.addMultiple("mcx", []float64{}, qubits)
}

func (qc *QuantumCircuit) Mcu1(theta float64, qubits []int) {
    qc.addMultiple("mcu1", []float64{theta}, qubits)
}

func (qc *QuantumCircuit) Mcu2(phi, lam float64, qubits []int) {
    qc.addMultiple("mcu2", []float64{phi, lam}, qubits)
}

func (qc *QuantumCircuit) Mcu3(theta, phi, lam float64, qubits []int) {
    qc.addMultiple("mcu3", []float64{theta, phi, lam}, qubits)
}

func (qc *QuantumCircuit) Mcz(qubits []int) {
    qc.addMultiple("mcz", []float64{}, qubits)
}

func (qc *QuantumCircuit) Mcp(qubits []int) {
    qc.addMultiple("mcp", []float64{}, qubits)
}

func (qc *QuantumCircuit) Mcrx(qubits []int) {
    qc.addMultiple("mcrx", []float64{}, qubits)
}

func (qc *QuantumCircuit) Mcry(qubits []int) {
    qc.addMultiple("mcry", []float64{}, qubits)
}

func (qc *QuantumCircuit) Mcrz(qubits []int) {
    qc.addMultiple("mcrz", []float64{}, qubits)
}

func (qc *QuantumCircuit) Qft(qubits []int) {
    qc.addMultiple("qft", []float64{}, qubits)
}

func (qc *QuantumCircuit) InverseQft(qubits []int) {
    qc.addMultiple("iqft", []float64{}, qubits)
}

func (qc *QuantumCircuit) Swap(qubit1, qubit2 int) {
    qc.addDouble("swap", []float64{}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Csx(qubit1, qubit2 int) {
    qc.addDouble("csx", []float64{}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) P(theta float64, qubit1 int) {
    qc.addSingle("p", []float64{theta}, []int{qubit1})
}

func (qc *QuantumCircuit) Cp(theta float64, qubit1, qubit2 int) {
    qc.addDouble("cp", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Ccp(theta float64, qubit1, qubit2, qubit3 int) {
    qc.addTriple("ccp", []float64{theta}, []int{qubit1, qubit2, qubit3})
}

func (qc *QuantumCircuit) SqrtX(qubit1 int) {
    qc.addSingle("sqrt_x", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) SqrtY(qubit1 int) {
    qc.addSingle("sqrt_y", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) SqrtZ(qubit1 int) {
    qc.addSingle("sqrt_z", []float64{}, []int{qubit1})
}

func (qc *QuantumCircuit) Gpi(phi float64, qubit1 int) {
    qc.addSingle("gpi", []float64{phi}, []int{qubit1})
}

func (qc *QuantumCircuit) Gpi2(phi float64, qubit1 int) {
    qc.addSingle("gpi2", []float64{phi}, []int{qubit1})
}

func (qc *QuantumCircuit) Xp(theta float64, qubit1 int) {
    qc.addSingle("xp", []float64{theta}, []int{qubit1})
}

func (qc *QuantumCircuit) Yp(theta float64, qubit1 int) {
    qc.addSingle("yp", []float64{theta}, []int{qubit1})
}

func (qc *QuantumCircuit) Zp(theta float64, qubit1 int) {
    qc.addSingle("zp", []float64{theta}, []int{qubit1})
}

func (qc *QuantumCircuit) Xxp(theta float64, qubit1, qubit2 int) {
    qc.addDouble("xxp", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Yyp(theta float64, qubit1, qubit2 int) {
    qc.addDouble("yyp", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Zzp(theta float64, qubit1, qubit2 int) {
    qc.addDouble("zzp", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) PhasedXp(theta, phi float64, qubit1 int) {
    qc.addSingle("phased_xp", []float64{theta, phi}, []int{qubit1})
}

func (qc *QuantumCircuit) PhasedYp(theta, phi float64, qubit1 int) {
    qc.addSingle("phased_yp", []float64{theta, phi}, []int{qubit1})
}

func (qc *QuantumCircuit) PhasedZp(theta, phi float64, qubit1 int) {
    qc.addSingle("phased_zp", []float64{theta, phi}, []int{qubit1})
}

func (qc *QuantumCircuit) Cnotp(theta float64, qubit1, qubit2 int) {
    qc.addDouble("cnotp", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Ccnotp(theta float64, qubit1, qubit2, qubit3 int) {
    qc.addTriple("ccnotp", []float64{theta}, []int{qubit1, qubit2, qubit3})
}

func (qc *QuantumCircuit) Cyp(theta float64, qubit1, qubit2 int) {
    qc.addDouble("cyp", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Ccyp(theta float64, qubit1, qubit2, qubit3 int) {
    qc.addTriple("ccyp", []float64{theta}, []int{qubit1, qubit2, qubit3})
}

func (qc *QuantumCircuit) Czp(theta float64, qubit1, qubit2 int) {
    qc.addDouble("czp", []float64{theta}, []int{qubit1, qubit2})
}

func (qc *QuantumCircuit) Cczp(theta float64, qubit1, qubit2, qubit3 int) {
    qc.addTriple("cczp", []float64{theta}, []int{qubit1, qubit2, qubit3})
}

func (qc *QuantumCircuit) Measure(qubits []int) {
    var cparams []float64
    var cqubits []int
    cgate := "measure"
    if len(qubits) == 0 {
        panic("number of qubits to measure cannot be zero")
    } else {
        for _, qubit := range qubits {
            if qubit < 0 || qubit >= qc.numQubits {
                panic(fmt.Sprintf("invalid qubit: %d", qubit))
            } else {
                cqubits = append(cqubits, qubit)
            }
        }
    }
    qc.operations = append(qc.operations, Operation{cgate, cqubits, cparams})
}

func (qc *QuantumCircuit) MeasureAll() {
    var cparams []float64
    var cqubits []int
    cgate := "measure"
    for qubit := 0; qubit < qc.numQubits; qubit++ {
        cqubits = append(cqubits, qubit)
    }
    qc.operations = append(qc.operations, Operation{cgate, cqubits, cparams})
}

func (qc *QuantumCircuit) RandomCircuit(numberOfOperations int, qubitsToUseForRandomCircuit []int) {
    qubitsCount := len(qubitsToUseForRandomCircuit)
    if qubitsCount < 3 {
        panic("The number of qubits needed to generate random circuits is >= 3")
    }

    gatesAndQubitsMap := map[string]int{
        "x": 1, "y": 1, "z": 1, "rx": 1, "ry": 1, "rz": 1, "h": 1, "s": 1, "sdg": 1, "t": 1, "tdg": 1, "sx": 1, "sxdg": 1,
        "cx": 2, "cy": 2, "cz": 2, "crx": 2, "cry": 2, "crz": 2, "ch": 2, "dcx": 2, "ecr": 2, "iswap": 2, "swap": 2, "csx": 2,
        "cswap": 3, "ccx": 3,
    }

    allPossibleGates := make([]string, 0, len(gatesAndQubitsMap))
    for gate := range gatesAndQubitsMap {
        allPossibleGates = append(allPossibleGates, gate)
    }
    allPossibleGatesCount := len(allPossibleGates)

    rand.Seed(time.Now().UnixNano())
    for i := 0; i < numberOfOperations; i++ {
        index := rand.Intn(allPossibleGatesCount)
        cgate := allPossibleGates[index]

        numberOfQubits := gatesAndQubitsMap[cgate]

        rand.Shuffle(qubitsCount, func(i, j int) {
            qubitsToUseForRandomCircuit[i], qubitsToUseForRandomCircuit[j] = qubitsToUseForRandomCircuit[j], qubitsToUseForRandomCircuit[i]
        })
        cqubits := make([]int, numberOfQubits)
        copy(cqubits, qubitsToUseForRandomCircuit[:numberOfQubits])

        var cparams []float64
        if contains([]string{"rx", "ry", "rz", "crx", "cry", "crz"}, cgate) {
            theta := rand.Float64() * 2 * math.Pi
            cparams = append(cparams, theta)
        }

        qc.operations = append(qc.operations, Operation{cgate, cqubits, cparams})
    }
}

func contains(slice []string, item string) bool {
    for _, s := range slice {
        if s == item {
            return true
        }
    }
    return false
}