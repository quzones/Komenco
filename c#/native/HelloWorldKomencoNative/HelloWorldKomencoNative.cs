using System;
using System.Collections.Generic;
using System.Linq;
using XPlot.Plotly;
using Automatski.Komenco;

namespace Automatski.Komenco.Examples
{
    class HelloWorldKomencoNative
    {
        static void Main(string[] args)
        {
            // Create a sample quantum circuit to create a 3 Qubit GHZ State
            QuantumCircuit circuit = new QuantumCircuit(3);
            circuit.H(0);
            circuit.Cx(0, 1);
            circuit.Cx(0, 2);
            circuit.MeasureAll();

            // Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
            AutomatskiKomencoNative sampler = new AutomatskiKomencoNative("103.212.120.18", 80);

            // Run the circuit and get results
            Dictionary<string, int> results = new Dictionary<string, int>();
            try
            {
                results = sampler.Run(circuit, 1000, 20);
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                return;
            }

            // Extract and count the measurement results
            Dictionary<string, int> measurements = results;
            Console.WriteLine(measurements);

            List<string> labels = new List<string>(measurements.Keys);
            labels.Sort();
            List<int> values = labels.Select(label => measurements[label]).ToList();

            // Plot the results
            var chart = Chart.Plot(
                new Bar
                {
                    x = labels,
                    y = values,
                    text = labels
                }
            );

            chart.WithTitle("Quantum States & Counts Histogram");
            chart.WithXTitle("Measurement Outcomes");
            chart.WithYTitle("Counts");

            var chartHtml = chart.GetHtml();
            System.IO.File.WriteAllText("chart.html", chartHtml);
            Console.WriteLine("Chart saved to chart.html");
        }
    }
}