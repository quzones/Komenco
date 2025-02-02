<?php

namespace Automatski\Komenco;

require_once 'QuantumCircuit.php';
require_once 'Operation.php';

use Automatski\Komenco\Operation;
use Automatski\Komenco\QuantumCircuit;

use Exception;
use RuntimeException;

class AutomatskiKomencoNative {
    private $host;
    private $port;

    public function __construct(string $host, int $port) {
        $this->host = $host;
        $this->port = $port;
    }

    public function run(QuantumCircuit $circuit, int $repetitions, int $topK): array {
        $tstart = microtime(true);

        $body = $this->serializeCircuit($circuit, $topK);
        $struct = $this->postRequest($body);

        $tend = microtime(true);
        $executionTime = ($tend - $tstart) * 1000;
        echo "Time Taken " . $executionTime . "ms\n";

        if (isset($struct['error'])) {
            echo $struct['error'] . "\n";
            throw new RuntimeException($struct['error']);
        }

        return $this->deserializeResult($struct, $repetitions);
    }

    private function serializeCircuit(QuantumCircuit $circuit, int $topK): array {
        $numQubits = $circuit->getNumQubits();

        $operations = [];
        $measurements = [];

        foreach ($circuit->getOperations() as $operation) {
            $gate = $operation->getGate();
            $params = $operation->getParams();
            $qubits = $operation->getQubits();

            if ($gate === "measure") {
                $measurements = array_merge($measurements, $qubits);
            } else {
                $op = [
                    "gate" => $gate,
                    "params" => $params,
                    "qubits" => $qubits
                ];
                $operations[] = $op;
            }
        }

        echo "Executing Quantum Circuit With...\n";
        echo $numQubits . " Qubits And ...\n";
        echo count($operations) . " Gates\n";

        if (empty($measurements)) {
            throw new RuntimeException("There are no measurements done at the end of the circuit.");
        }

        return [
            "num_qubits" => $numQubits,
            "operations" => $operations,
            "measurements" => $measurements,
            "topK" => $topK
        ];
    }

    private function postRequest(array $body): array {
        $url = "http://{$this->host}:{$this->port}/api/komenco";
        $options = [
            'http' => [
                'header' => "Content-Type: application/json\r\n" .
                            "Accept: application/json\r\n",
                'method' => 'POST',
                'content' => json_encode($body),
                'timeout' => 60
            ]
        ];
        $context = stream_context_create($options);
        $response = file_get_contents($url, false, $context);

        if ($response === FALSE) {
            throw new Exception("Error making POST request");
        }

        return json_decode($response, true);
    }

    private function deserializeResult(array $responseData, int $repetitions): array {
        $measurementsStrings = $responseData['measurements'];

        $measurements = [];
        foreach ($measurementsStrings as $key => $value) {
            $count = round($value * $repetitions);
            $measurements[$key] = $count;
        }

        return $measurements;
    }
}

?>