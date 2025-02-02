#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>
#include "QuantumCircuit.h"
#include "AutomatskiKomencoNative.h"


// sudo apt-get install libcurl4-openssl-dev
// sudo apt-get install libjsoncpp-dev
// g++ -o HelloWorldKomencoNative *.cpp  -lcurl -ljsoncpp


int main() {
    // Create a sample quantum circuit to create a 3 Qubit GHZ State
    QuantumCircuit circuit(3);
    circuit.h(0);
    circuit.cx(0, 1);
    circuit.cx(0, 2);
    circuit.measureAll();

    // Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
    AutomatskiKomencoNative sampler("103.212.120.18", 80);

    // Run the circuit and get results
    std::unordered_map<std::string, int> measurements;
    try {
        measurements = sampler.run(circuit, 100, 20); // changed 1000 samples to 100 so that its easier to print the text histogram on screen
    } catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
        return 100;
    }

    // Extract and count the measurement results
    std::vector<std::string> labels;
    for (const auto& pair : measurements) {
        labels.push_back(pair.first);
    }
    std::sort(labels.begin(), labels.end());

    std::vector<int> values;
    for (const auto& label : labels) {
        values.push_back(measurements[label]);
    }

    // Plot the results using a simple text-based histogram
    std::cout << "Quantum States & Counts Histogram" << std::endl;
    std::cout << "---------------------------------" << std::endl;
    for (size_t i = 0; i < labels.size(); ++i) {
        std::cout << labels[i] << ": " << std::string(values[i], '*') << " (" << values[i] << ")" << std::endl;
    }

    return 0;
}
