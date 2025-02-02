<?php

namespace Automatski\Komenco;

class Operation {
    private $gate;
    private $qubits;
    private $params;

    public function __construct(string $gate, array $qubits, array $params) {
        $this->gate = $gate;
        $this->qubits = $qubits;
        $this->params = $params;
    }

    public function getGate(): string {
        return $this->gate;
    }

    public function getQubits(): array {
        return $this->qubits;
    }

    public function getParams(): array {
        return $this->params;
    }
}

?>