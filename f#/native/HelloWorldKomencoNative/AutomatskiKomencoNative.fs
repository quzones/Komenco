namespace Automatski.Komenco

open System
open System.Net.Http
open System.Collections.Generic
open System.IO
open System.Net
open System.Text
open Newtonsoft.Json.Linq



type AutomatskiKomencoNative(host: string, port: int) =
    let host = host
    let port = port

    member this.Run(circuit: QuantumCircuit, repetitions: int, topK: int) =
        let tstart = DateTimeOffset.Now.ToUnixTimeMilliseconds()

        let body = this.SerializeCircuit(circuit, topK)
        let structData :JObject = this.PostRequest(body)

        let tend = DateTimeOffset.Now.ToUnixTimeMilliseconds()
        let executionTime = tend - tstart
        printfn "Time Taken %dms" executionTime

        if structData.ContainsKey("error") then
            printfn "%s" (structData.["error"].ToString())
            raise (Exception(structData.["error"].ToString()))

        this.DeserializeResult(structData, repetitions)

    member private this.SerializeCircuit(circuit: QuantumCircuit, topK: int) =
        let numQubits = circuit.GetNumQubits()

        let operations = List<Dictionary<string, obj>>()
        let measurements = List<int>()

        for operation : Operation  in circuit.GetOperations() do
            let gate = operation.GetGate()
            let paramsList = operation.GetParams()
            let qubits = operation.GetQubits()

            if gate = "measure" then
                measurements.AddRange(qubits)
            else
                let op = Dictionary<string, obj>()
                op.Add("gate", gate)
                op.Add("params", paramsList)
                op.Add("qubits", qubits)
                operations.Add(op)

        printfn "Executing Quantum Circuit With..."
        printfn "%d Qubits And ..." numQubits
        printfn "%d Gates" operations.Count

        if measurements.Count = 0 then
            raise (Exception("There are no measurements done at the end of the circuit."))

        let json = JObject()
        json.Add("num_qubits", JToken.FromObject(numQubits))
        json.Add("operations", JToken.FromObject(operations))
        json.Add("measurements", JToken.FromObject(measurements))
        json.Add("topK", JToken.FromObject(topK))

        json

    member private this.PostRequest(body: JObject) =
        let url = sprintf "http://%s:%d/api/komenco" host port
        use client = new HttpClient()
        let content = new StringContent(body.ToString(), Encoding.UTF8, "application/json")
        async {
            let! response = client.PostAsync(url, content) |> Async.AwaitTask
            response.EnsureSuccessStatusCode() |> ignore
            let! responseText = response.Content.ReadAsStringAsync() |> Async.AwaitTask
            return JObject.Parse(responseText)
        } |> Async.RunSynchronously

    member private this.DeserializeResult(responseData: JObject, repetitions: int) =
        let measurementsStrings = responseData.["measurements"] :?> JObject

        let measurements = Dictionary<string, int>()
        for key in measurementsStrings.Properties() do
            let count = int (Math.Round(measurementsStrings.[key.Name].ToObject<double>() * float repetitions))
            measurements.Add(key.Name, count)

        measurements