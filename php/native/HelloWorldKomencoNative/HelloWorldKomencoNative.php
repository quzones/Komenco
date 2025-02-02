<?php

require_once 'AutomatskiKomencoNative.php';
require_once 'QuantumCircuit.php';

use Automatski\Komenco\AutomatskiKomencoNative;
use Automatski\Komenco\QuantumCircuit;

function main() {
    // Create a sample quantum circuit to create a 3 Qubit GHZ State
    $circuit = new QuantumCircuit(3);
    $circuit->h(0);
    $circuit->cx(0, 1);
    $circuit->cx(0, 2);
    $circuit->measureAll();

    // Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
    $sampler = new AutomatskiKomencoNative("103.212.120.18", 80);

    // Run the circuit and get results
    try {
        $results = $sampler->run($circuit, 100, 20); // changed 1000 samples to 100 so that its easier to print the text histogram on screen
    } catch (Exception $e) {
        echo $e->getMessage();
        return;
    }

    // Extract and count the measurement results
    $measurements = $results;
    print_r($measurements);

    $labels = array_keys($measurements);
    sort($labels);
    $values = array_map(function($label) use ($measurements) {
        return $measurements[$label];
    }, $labels);

    // Plot the results using a simple text-based histogram
    echo "Quantum States & Counts Histogram\n";
    echo "---------------------------------\n";
    foreach ($labels as $index => $label) {
        echo str_pad($label, 10) . ": " . str_repeat('*', $values[$index]) . " (" . $values[$index] . ")\n";
    }
}

main();

?>