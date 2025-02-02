import 'dart:async';
import 'dart:io';
import 'automatskikomenconative.dart';
import 'quantumcircuit.dart';

void main() async {
  // Create a sample quantum circuit to create a 3 Qubit GHZ State
  QuantumCircuit circuit = QuantumCircuit(3);
  circuit.h(0);
  circuit.cx(0, 1);
  circuit.cx(0, 2);
  circuit.measureAll();

  // Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
  AutomatskiKomencoNative sampler = AutomatskiKomencoNative("103.212.120.18", 80);

  // Run the circuit and get results
  Map<String, int> measurements;
  try {
    measurements = await sampler.run(circuit, 100, 20); // changed 1000 samples to 100 so that its easier to print the text histogram on screen
  } catch (e) {
    print(e);
    return;
  }

  // Extract and count the measurement results
  List<String> labels = measurements.keys.toList();
  labels.sort();

  List<int> values = labels.map((label) => measurements[label]!).toList();

  // Plot the results using a simple text-based histogram
  print("Quantum States & Counts Histogram");
  print("---------------------------------");
  for (int i = 0; i < labels.length; i++) {
    print("${labels[i].padRight(10)}: ${'*' * values[i]} (${values[i]})");
  }
}