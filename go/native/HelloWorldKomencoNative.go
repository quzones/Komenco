package main

import (
    "fmt"
    "log"
    "sort"
	"os"

    "github.com/wcharczuk/go-chart/v2"
    "github.com/wcharczuk/go-chart/v2/drawing"
)

func main() {
    // Create a sample quantum circuit to create a 3 Qubit GHZ State
    circuit := NewQuantumCircuit(3)
    circuit.H(0)
    circuit.Cx(0, 1)
    circuit.Cx(0, 2)
    circuit.MeasureAll()

    // Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
    sampler := NewAutomatskiKomencoNative("103.212.120.18", 80)

    // Run the circuit and get results
    results, err := sampler.Run(circuit, 1000, 20)
    if err != nil {
        log.Fatalf("Failed to run the circuit: %v", err)
    }

    // Extract and count the measurement results
    measurements := results
    fmt.Println(measurements)

    labels := make([]string, 0, len(measurements))
    for label := range measurements {
        labels = append(labels, label)
    }
    sort.Strings(labels)

    values := make([]float64, len(labels))
    for i, label := range labels {
        values[i] = float64(measurements[label])
    }

    // Plot the results
    graph := chart.BarChart{
        Title: "Quantum States & Counts Histogram",
        Background: chart.Style{
            Padding: chart.Box{
                Top: 40,
            },
        },
        Height: 600,
        BarWidth: 60,
        XAxis: chart.Style{
            TextRotationDegrees: 90,
        },
        Bars: []chart.Value{},
    }

    for i, label := range labels {
        graph.Bars = append(graph.Bars, chart.Value{
            Label: label,
            Value: values[i],
            Style: chart.Style{
                FillColor: drawing.ColorFromHex("6495ED"),
            },
        })
    }

    f, err := os.Create("output.png")
    if err != nil {
        log.Fatalf("Failed to create output file: %v", err)
    }
    defer f.Close()

    err = graph.Render(chart.PNG, f)
    if err != nil {
        log.Fatalf("Failed to render chart: %v", err)
    }

    fmt.Println("Chart saved to output.png")
}