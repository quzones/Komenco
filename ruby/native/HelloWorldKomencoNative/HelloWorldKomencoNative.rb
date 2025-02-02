require_relative 'AutomatskiKomencoNative'
require_relative 'QuantumCircuit'

include Automatski::Komenco

def main
  # Create a sample quantum circuit to create a 3 Qubit GHZ State
  circuit = QuantumCircuit.new(3)
  circuit.h(0)
  circuit.cx(0, 1)
  circuit.cx(0, 2)
  circuit.measure_all

  # Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
  sampler = AutomatskiKomencoNative.new("103.212.120.18", 80)

  # Run the circuit and get results
  begin
    results = sampler.run(circuit, 100, 20) # changed 1000 samples to 100 so that its easier to print the text histogram on screen
  rescue StandardError => e
    puts e.message
    return
  end

  # Extract and count the measurement results
  measurements = results
  puts measurements

  labels = measurements.keys.sort
  values = labels.map { |label| measurements[label] }

  # Plot the results using a simple text-based histogram
  puts "Quantum States & Counts Histogram"
  puts "---------------------------------"
  labels.each_with_index do |label, index|
    puts "#{label.ljust(10)}: #{'*' * values[index]} (#{values[index]})"
  end
end

main