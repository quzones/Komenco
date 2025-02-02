% Add necessary paths
addpath('./');


% Create a sample quantum circuit to create a 3 Qubit GHZ State
circuit = QuantumCircuit(3);
circuit = circuit.h(0);
circuit = circuit.cx(0, 1);
circuit = circuit.cx(0, 2);
circuit = circuit.measureAll();


% Run the Circuit using Automatskis Quantum Simulators and Quantum Computers 
sampler = AutomatskiKomencoNative('103.212.120.18', 80);

% Run the circuit and get results
try
    results = sampler.run(circuit, 100, 20); % changed 1000 samples to 100 so that its easier to print the text histogram on screen
catch e
    disp(e.message);
    return;
end

% Extract and count the measurement results
measurements = results;
disp(measurements);

labels = keys(measurements);
labels = sort(labels);
values = cellfun(@(label) measurements(label), labels);

% Plot the results using a simple text-based histogram
disp('Quantum States & Counts Histogram');
disp('---------------------------------');
for i = 1:length(labels)
    fprintf('%-10s: %s (%d)\n', labels{i}, repmat('*', 1, values(i)), values(i));
end