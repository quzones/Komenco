namespace Automatski.Komenco

open System
open System.Collections.Generic

type QuantumCircuit(numQubits: int) =
    let operations = ResizeArray<Operation>()

    member this.NumQubits = numQubits
    member this.Operations = operations

    member this.GetNumQubits() = numQubits
    member this.GetOperations() = operations

    member private this.AddSingle(gate: string, paramsList: List<double>, qubits: List<int>) =
        if qubits.Count <> 1 then
            raise (ArgumentException(sprintf "Number of qubits for gate %s has to be one" gate))
        for qubit in qubits do
            if qubit < 0 || qubit >= numQubits then
                raise (ArgumentException(sprintf "Invalid qubit: %d" qubit))
        operations.Add(Operation(gate, qubits, paramsList))

    member private this.AddDouble(gate: string, paramsList: List<double>, qubits: List<int>) =
        if qubits.Count <> 2 then
            raise (ArgumentException(sprintf "Number of qubits for gate %s has to be two" gate))
        for qubit in qubits do
            if qubit < 0 || qubit >= numQubits then
                raise (ArgumentException(sprintf "Invalid qubit: %d" qubit))
        operations.Add(Operation(gate, qubits, paramsList))

    member private this.AddTriple(gate: string, paramsList: List<double>, qubits: List<int>) =
        if qubits.Count <> 3 then
            raise (ArgumentException(sprintf "Number of qubits for gate %s has to be three" gate))
        for qubit in qubits do
            if qubit < 0 || qubit >= numQubits then
                raise (ArgumentException(sprintf "Invalid qubit: %d" qubit))
        operations.Add(Operation(gate, qubits, paramsList))

    member private this.AddMultiple(gate: string, paramsList: List<double>, qubits: List<int>) =
        let requiredQubits = int (Math.Log(float gate.Length) / Math.Log(2.0))
        if qubits.Count <> requiredQubits then
            raise (ArgumentException(sprintf "Number of qubits for gate %s has to be %d" gate requiredQubits))
        for qubit in qubits do
            if qubit < 0 || qubit >= numQubits then
                raise (ArgumentException(sprintf "Invalid qubit: %d" qubit))
        operations.Add(Operation(gate, qubits, paramsList))

    member this.Id(qubit1: int) =
        this.AddSingle("id", List<double>(), List<int> [qubit1])

    member this.X(qubit1: int) =
        this.AddSingle("x", List<double>(), List<int> [qubit1])

    member this.Y(qubit1: int) =
        this.AddSingle("y", List<double>(), List<int> [qubit1])

    member this.Z(qubit1: int) =
        this.AddSingle("z", List<double>(), List<int> [qubit1])

    member this.H(qubit1: int) =
        this.AddSingle("h", List<double>(), List<int> [qubit1])

    member this.S(qubit1: int) =
        this.AddSingle("s", List<double>(), List<int> [qubit1])

    member this.Sdg(qubit1: int) =
        this.AddSingle("sdg", List<double>(), List<int> [qubit1])

    member this.T(qubit1: int) =
        this.AddSingle("t", List<double>(), List<int> [qubit1])

    member this.Tdg(qubit1: int) =
        this.AddSingle("tdg", List<double>(), List<int> [qubit1])

    member this.Rx(theta: double, qubit1: int) =
        this.AddSingle("rx", List<double> [theta], List<int> [qubit1])

    member this.Ry(theta: double, qubit1: int) =
        this.AddSingle("ry", List<double> [theta], List<int> [qubit1])

    member this.Rz(theta: double, qubit1: int) =
        this.AddSingle("rz", List<double> [theta], List<int> [qubit1])

    member this.U(theta: double, phi: double, lam: double, qubit1: int) =
        this.AddSingle("u", List<double> [theta; phi; lam], List<int> [qubit1])

    member this.U1(theta: double, qubit1: int) =
        this.AddSingle("u1", List<double> [theta], List<int> [qubit1])

    member this.U2(phi: double, lam: double, qubit1: int) =
        this.AddSingle("u2", List<double> [phi; lam], List<int> [qubit1])

    member this.U3(theta: double, phi: double, lam: double, qubit1: int) =
        this.AddSingle("u3", List<double> [theta; phi; lam], List<int> [qubit1])

    member this.Sx(qubit1: int) =
        this.AddSingle("sx", List<double>(), List<int> [qubit1])

    member this.Sxdg(qubit1: int) =
        this.AddSingle("sxdg", List<double>(), List<int> [qubit1])

    member this.R(theta: double, phi: double, qubit1: int) =
        this.AddSingle("r", List<double> [theta; phi], List<int> [qubit1])

    member this.Cx(qubit1: int, qubit2: int) =
        this.AddDouble("cx", List<double>(), List<int> [qubit1; qubit2])

    member this.Cy(qubit1: int, qubit2: int) =
        this.AddDouble("cy", List<double>(), List<int> [qubit1; qubit2])

    member this.Cz(qubit1: int, qubit2: int) =
        this.AddDouble("cz", List<double>(), List<int> [qubit1; qubit2])

    member this.Ch(qubit1: int, qubit2: int) =
        this.AddDouble("ch", List<double>(), List<int> [qubit1; qubit2])

    member this.Ucrx(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("ucrx", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Ucry(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("ucry", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Ucrz(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("ucrz", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Crx(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("crx", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Cry(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("cry", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Crz(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("crz", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Cr(theta: double, phi: double, lam: double, qubit1: int, qubit2: int) =
        this.AddDouble("cr", List<double> [theta; phi; lam], List<int> [qubit1; qubit2])

    member this.Cu(theta: double, phi: double, lam: double, gamma: double, qubit1: int, qubit2: int) =
        this.AddDouble("cu1", List<double> [theta; phi; lam; gamma], List<int> [qubit1; qubit2])

    member this.Cu1(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("cu1", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Cu2(phi: double, lam: double, qubit1: int, qubit2: int) =
        this.AddDouble("cu2", List<double> [phi; lam], List<int> [qubit1; qubit2])

    member this.Cu3(theta: double, phi: double, lam: double, qubit1: int, qubit2: int) =
        this.AddDouble("cu3", List<double> [theta; phi; lam], List<int> [qubit1; qubit2])

    member this.Dcx(qubit1: int, qubit2: int) =
        this.AddDouble("dcx", List<double>(), List<int> [qubit1; qubit2])

    member this.Ecr(qubit1: int, qubit2: int) =
        this.AddDouble("ecr", List<double>(), List<int> [qubit1; qubit2])

    member this.Iswap(qubit1: int, qubit2: int) =
        this.AddDouble("iswap", List<double>(), List<int> [qubit1; qubit2])

    member this.Rxx(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("rxx", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Ryy(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("ryy", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Rzz(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("rzz", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Rzx(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("rzx", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Cswap(qubit1: int, qubit2: int, qubit3: int) =
        this.AddTriple("cswap", List<double>(), List<int> [qubit1; qubit2; qubit3])

    member this.Ccx(qubit1: int, qubit2: int, qubit3: int) =
        this.AddTriple("ccx", List<double>(), List<int> [qubit1; qubit2; qubit3])

    member this.Ccy(qubit1: int, qubit2: int, qubit3: int) =
        this.AddTriple("ccy", List<double>(), List<int> [qubit1; qubit2; qubit3])

    member this.Ccz(qubit1: int, qubit2: int, qubit3: int) =
        this.AddTriple("ccz", List<double>(), List<int> [qubit1; qubit2; qubit3])

    member this.C3x(qubits: List<int>) =
        this.AddMultiple("c3x", List<double>(), qubits)

    member this.C4x(qubits: List<int>) =
        this.AddMultiple("c4x", List<double>(), qubits)

    member this.Mcx(qubits: List<int>) =
        this.AddMultiple("mcx", List<double>(), qubits)

    member this.Mcu1(theta: double, qubits: List<int>) =
        this.AddMultiple("mcu1", List<double> [theta], qubits)

    member this.Mcu2(phi: double, lam: double, qubits: List<int>) =
        this.AddMultiple("mcu2", List<double> [phi; lam], qubits)

    member this.Mcu3(theta: double, phi: double, lam: double, qubits: List<int>) =
        this.AddMultiple("mcu3", List<double> [theta; phi; lam], qubits)

    member this.Mcz(qubits: List<int>) =
        this.AddMultiple("mcz", List<double>(), qubits)

    member this.Mcp(qubits: List<int>) =
        this.AddMultiple("mcp", List<double>(), qubits)

    member this.Mcrx(qubits: List<int>) =
        this.AddMultiple("mcrx", List<double>(), qubits)

    member this.Mcry(qubits: List<int>) =
        this.AddMultiple("mcry", List<double>(), qubits)

    member this.Mcrz(qubits: List<int>) =
        this.AddMultiple("mcrz", List<double>(), qubits)

    member this.Qft(qubits: List<int>) =
        this.AddMultiple("qft", List<double>(), qubits)

    member this.InverseQft(qubits: List<int>) =
        this.AddMultiple("iqft", List<double>(), qubits)

    member this.Swap(qubit1: int, qubit2: int) =
        this.AddDouble("swap", List<double>(), List<int> [qubit1; qubit2])

    member this.Csx(qubit1: int, qubit2: int) =
        this.AddDouble("csx", List<double>(), List<int> [qubit1; qubit2])

    member this.P(theta: double, qubit1: int) =
        this.AddSingle("p", List<double> [theta], List<int> [qubit1])

    member this.Cp(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("cp", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Ccp(theta: double, qubit1: int, qubit2: int, qubit3: int) =
        this.AddTriple("ccp", List<double> [theta], List<int> [qubit1; qubit2; qubit3])

    member this.SqrtX(qubit1: int) =
        this.AddSingle("sqrt_x", List<double>(), List<int> [qubit1])

    member this.SqrtY(qubit1: int) =
        this.AddSingle("sqrt_y", List<double>(), List<int> [qubit1])

    member this.SqrtZ(qubit1: int) =
        this.AddSingle("sqrt_z", List<double>(), List<int> [qubit1])

    member this.Gpi(phi: double, qubit1: int) =
        this.AddSingle("gpi", List<double> [phi], List<int> [qubit1])

    member this.Gpi2(phi: double, qubit1: int) =
        this.AddSingle("gpi2", List<double> [phi], List<int> [qubit1])

    member this.Xp(theta: double, qubit1: int) =
        this.AddSingle("xp", List<double> [theta], List<int> [qubit1])

    member this.Yp(theta: double, qubit1: int) =
        this.AddSingle("yp", List<double> [theta], List<int> [qubit1])

    member this.Zp(theta: double, qubit1: int) =
        this.AddSingle("zp", List<double> [theta], List<int> [qubit1])

    member this.Xxp(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("xxp", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Yyp(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("yyp", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Zzp(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("zzp", List<double> [theta], List<int> [qubit1; qubit2])

    member this.PhasedXp(theta: double, phi: double, qubit1: int) =
        this.AddSingle("phased_xp", List<double> [theta; phi], List<int> [qubit1])

    member this.PhasedYp(theta: double, phi: double, qubit1: int) =
        this.AddSingle("phased_yp", List<double> [theta; phi], List<int> [qubit1])

    member this.PhasedZp(theta: double, phi: double, qubit1: int) =
        this.AddSingle("phased_zp", List<double> [theta; phi], List<int> [qubit1])

    member this.Cnotp(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("cnotp", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Ccnotp(theta: double, qubit1: int, qubit2: int, qubit3: int) =
        this.AddTriple("ccnotp", List<double> [theta], List<int> [qubit1; qubit2; qubit3])

    member this.Cyp(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("cyp", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Ccyp(theta: double, qubit1: int, qubit2: int, qubit3: int) =
        this.AddTriple("ccyp", List<double> [theta], List<int> [qubit1; qubit2; qubit3])

    member this.Czp(theta: double, qubit1: int, qubit2: int) =
        this.AddDouble("czp", List<double> [theta], List<int> [qubit1; qubit2])

    member this.Cczp(theta: double, qubit1: int, qubit2: int, qubit3: int) =
        this.AddTriple("cczp", List<double> [theta], List<int> [qubit1; qubit2; qubit3])

    member this.Measure(qubits: List<int>) =
        let cparams = List<double>()
        let cqubits = List<int>()
        let cgate = "measure"
        if qubits.Count = 0 then
            raise (ArgumentException("number of qubits to measure cannot be zero"))
        else
            for qubit in qubits do
                if qubit < 0 || qubit >= numQubits then
                    raise (ArgumentException(sprintf "invalid qubit: %d" qubit))
                else
                    cqubits.Add(qubit)
        operations.Add(Operation(cgate, cqubits, cparams))            

    member this.MeasureAll() =
        let cparams = List<double>()
        let cqubits = List<int>()
        let cgate = "measure"
        for qubit in 0 .. numQubits - 1 do
            cqubits.Add(qubit)
        operations.Add(Operation(cgate, cqubits, cparams))  

    member this.RandomCircuit(numberOfOperations: int, qubitsToUseForRandomCircuit: List<int>) =
        let qubitsCount = qubitsToUseForRandomCircuit.Count
        if qubitsCount < 3 then
            raise (ArgumentException("The number of qubits needed to generate random circuits is >= 3"))

        let gatesAndQubitsMap = 
            dict [
                // 1 qubit gates
                "x", 1
                "y", 1
                "z", 1
                "rx", 1
                "ry", 1
                "rz", 1
                "h", 1
                "s", 1
                "sdg", 1
                "t", 1
                "tdg", 1
                "sx", 1
                "sxdg", 1
                // 2 qubit gates
                "cx", 2
                "cy", 2
                "cz", 2
                "crx", 2
                "cry", 2
                "crz", 2
                "ch", 2
                "dcx", 2
                "ecr", 2
                "iswap", 2
                "swap", 2
                "csx", 2
                // 3 qubit gates
                "cswap", 3
                "ccx", 3
            ]

        let allPossibleGates = List<string>(gatesAndQubitsMap.Keys)
        let allPossibleGatesCount = allPossibleGates.Count

        let random = Random()
        for i in 0 .. numberOfOperations - 1 do
            let index = random.Next(allPossibleGatesCount)
            let cgate = allPossibleGates.[index]

            let numberOfQubits = gatesAndQubitsMap.[cgate]

            let shuffledQubits = List<int>(qubitsToUseForRandomCircuit |> Seq.sortBy (fun _ -> random.Next()))
            let cqubits = List<int>()
            for j in 0 .. numberOfQubits - 1 do
                cqubits.Add(shuffledQubits.[j])

            let cparams = List<double>()
            if List.contains cgate ["rx"; "ry"; "rz"; "crx"; "cry"; "crz"] then
                let theta = random.NextDouble() * 2.0 * Math.PI
                cparams.Add(theta)

            operations.Add(Operation(cgate, cqubits, cparams))                