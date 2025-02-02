package com.automatski.komenco.examples;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import org.knowm.xchart.CategoryChart;
import org.knowm.xchart.CategoryChartBuilder;
import org.knowm.xchart.SwingWrapper;
import org.knowm.xchart.style.Styler;

import com.automatski.komenco.AutomatskiKomencoNative;
import com.automatski.komenco.QuantumCircuit;

public class HelloWorldKomencoNative {

    public static void main(String[] args) {
        // Create a sample quantum circuit to create a 3 Qubit GHZ State
        QuantumCircuit circuit = new QuantumCircuit(3);
        circuit.h(0);
        circuit.cx(0, 1);
        circuit.cx(0, 2);
        circuit.measureAll();

        // Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
        AutomatskiKomencoNative sampler = new AutomatskiKomencoNative("103.212.120.18", 80);

        // Run the circuit and get results
        Map<String, Integer> results = null;
        try {
            results = sampler.run(circuit, 1000, 20);
        } catch (Exception e) {
            e.printStackTrace();
            return;
        }

        // Extract and count the measurement results
        Map<String, Integer> measurements = results;
        System.out.println(measurements);

        List<String> labels = new ArrayList<>(measurements.keySet());
        Collections.sort(labels);
        List<Integer> values = labels.stream().map(measurements::get).collect(Collectors.toList());

        // Plot the results
        CategoryChart chart = new CategoryChartBuilder().width(800).height(600).title("Quantum States & Counts Histogram")
                .xAxisTitle("Measurement Outcomes").yAxisTitle("Counts").build();

        chart.getStyler().setLegendPosition(Styler.LegendPosition.InsideNW);
        //chart.getStyler().setHasAnnotations(true);
        chart.getStyler().setXAxisLabelRotation(90);

        chart.addSeries("Counts", labels, values);

        new SwingWrapper<>(chart).displayChart();
    }
}
