namespace Automatski.Komenco

open System.Collections.Generic

type Operation(gate: string, qubits: List<int>, parameters: List<double>) =
    member this.Gate = gate
    member this.Qubits = qubits
    member this.Params = parameters

    member this.GetGate() = this.Gate
    member this.GetQubits() = this.Qubits
    member this.GetParams() = this.Params