const QuickChart = require('quickchart-js');
const fs = require('fs');
const QuantumCircuit = require('./QuantumCircuit');
const AutomatskiKomencoNative = require('./AutomatskiKomencoNative');

async function main() {
    
    // Create a sample quantum circuit to create a 3 Qubit GHZ State
    const circuit = new QuantumCircuit(3);
    circuit.h(0);
    circuit.cx(0, 1);
    circuit.cx(0, 2);
    circuit.measureAll();

    // Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
    const sampler = new AutomatskiKomencoNative('103.212.120.18', 80);

    // Run the circuit and get results
    let results;
    try {
        results = await sampler.run(circuit, 1000, 20);
    } catch (e) {
        console.error(e);
        return;
    }

    // Extract and count the measurement results
    const measurements = results;
    console.log(measurements);

    const labels = Object.keys(measurements).sort();
    const values = labels.map(label => measurements[label]);

    // Plot the results using QuickChart
    const chart = new QuickChart();
    chart.setConfig({
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Counts',
                data: values,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Measurement Outcomes'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Counts'
                    }
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Quantum States & Counts Histogram'
                }
            }
        }
    });

    const chartUrl = chart.getUrl();
    console.log('Chart URL:', chartUrl);

    // Save the chart as an image
    const imageBuffer = await chart.toBinary();
    fs.writeFileSync('chart.png', imageBuffer);
    console.log('Chart saved to chart.png');
}

main().catch(console.error);