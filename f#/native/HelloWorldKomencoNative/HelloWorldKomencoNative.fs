open System
open System.Collections.Generic
open System.IO
open XPlot.Plotly
open Automatski.Komenco

module HelloWorldKomencoNative =

    [<EntryPoint>]
    let main argv =
        // Create a sample quantum circuit to create a 3 Qubit GHZ State
        let circuit = Automatski.Komenco.QuantumCircuit(3)
        circuit.H(0)
        circuit.Cx(0, 1)
        circuit.Cx(0, 2)
        circuit.MeasureAll()

        // Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
        let sampler = Automatski.Komenco.AutomatskiKomencoNative("103.212.120.18", 80)

        // Run the circuit and get results
        let results = 
            try
                sampler.Run(circuit, 1000, 20)
            with
            | ex -> 
                Console.WriteLine(ex)
                Environment.Exit(1)
                null // This is needed because F# requires an expression after the try-with block

        // Extract and count the measurement results
        let measurements = results
        Console.WriteLine(measurements)

        let labels = measurements.Keys |> Seq.toList |> List.sort
        let values = labels |> List.map (fun label -> measurements.[label])

        // Plot the results
        let chart = 
            Chart.Plot(
                Bar(
                    x = labels,
                    y = values,
                    text = labels
                )
            )

        chart.WithTitle("Quantum States & Counts Histogram")
        chart.WithXTitle("Measurement Outcomes")
        chart.WithYTitle("Counts")

        let chartHtml = chart.GetHtml()
        File.WriteAllText("chart.html", chartHtml)
        Console.WriteLine("Chart saved to chart.html")

        0 // return an integer exit code