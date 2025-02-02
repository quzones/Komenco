<?php

namespace Automatski\Komenco;

require_once 'Operation.php';

use Automatski\Komenco\Operation;
use InvalidArgumentException;

class QuantumCircuit {
    private $numQubits;
    private $operations;

    public function __construct(int $numQubits) {
        $this->numQubits = $numQubits;
        $this->operations = [];
    }

    public function getNumQubits(): int {
        return $this->numQubits;
    }

    public function getOperations(): array {
        return $this->operations;
    }

    private function addSingle(string $gate, array $params, array $qubits) {
        if (count($qubits) != 1) {
            throw new \InvalidArgumentException("Number of qubits for gate $gate has to be one");
        }
        foreach ($qubits as $qubit) {
            if ($qubit < 0 || $qubit >= $this->numQubits) {
                throw new \InvalidArgumentException("Invalid qubit: $qubit");
            }
        }
        $this->operations[] = new Operation($gate, $qubits, $params);
    }

    private function addDouble(string $gate, array $params, array $qubits) {
        if (count($qubits) != 2) {
            throw new \InvalidArgumentException("Number of qubits for gate $gate has to be two");
        }
        foreach ($qubits as $qubit) {
            if ($qubit < 0 || $qubit >= $this->numQubits) {
                throw new \InvalidArgumentException("Invalid qubit: $qubit");
            }
        }
        $this->operations[] = new Operation($gate, $qubits, $params);
    }

    private function addTriple(string $gate, array $params, array $qubits) {
        if (count($qubits) != 3) {
            throw new \InvalidArgumentException("Number of qubits for gate $gate has to be three");
        }
        foreach ($qubits as $qubit) {
            if ($qubit < 0 || $qubit >= $this->numQubits) {
                throw new \InvalidArgumentException("Invalid qubit: $qubit");
            }
        }
        $this->operations[] = new Operation($gate, $qubits, $params);
    }

    private function addMultiple(string $gate, array $params, array $qubits) {
        $requiredQubits = (int) (log(strlen($gate)) / log(2));
        if (count($qubits) != $requiredQubits) {
            throw new \InvalidArgumentException("Number of qubits for gate $gate has to be $requiredQubits");
        }
        foreach ($qubits as $qubit) {
            if ($qubit < 0 || $qubit >= $this->numQubits) {
                throw new \InvalidArgumentException("Invalid qubit: $qubit");
            }
        }
        $this->operations[] = new Operation($gate, $qubits, $params);
    }

    public function id(int $qubit1) {
        $this->addSingle("id", [], [$qubit1]);
    }

    public function x(int $qubit1) {
        $this->addSingle("x", [], [$qubit1]);
    }

    public function y(int $qubit1) {
        $this->addSingle("y", [], [$qubit1]);
    }

    public function z(int $qubit1) {
        $this->addSingle("z", [], [$qubit1]);
    }

    public function h(int $qubit1) {
        $this->addSingle("h", [], [$qubit1]);
    }

    public function s(int $qubit1) {
        $this->addSingle("s", [], [$qubit1]);
    }

    public function sdg(int $qubit1) {
        $this->addSingle("sdg", [], [$qubit1]);
    }

    public function t(int $qubit1) {
        $this->addSingle("t", [], [$qubit1]);
    }

    public function tdg(int $qubit1) {
        $this->addSingle("tdg", [], [$qubit1]);
    }

    public function rx(float $theta, int $qubit1) {
        $this->addSingle("rx", [$theta], [$qubit1]);
    }

    public function ry(float $theta, int $qubit1) {
        $this->addSingle("ry", [$theta], [$qubit1]);
    }

    public function rz(float $theta, int $qubit1) {
        $this->addSingle("rz", [$theta], [$qubit1]);
    }

    public function u(float $theta, float $phi, float $lam, int $qubit1) {
        $this->addSingle("u", [$theta, $phi, $lam], [$qubit1]);
    }

    public function u1(float $theta, int $qubit1) {
        $this->addSingle("u1", [$theta], [$qubit1]);
    }

    public function u2(float $phi, float $lam, int $qubit1) {
        $this->addSingle("u2", [$phi, $lam], [$qubit1]);
    }

    public function u3(float $theta, float $phi, float $lam, int $qubit1) {
        $this->addSingle("u3", [$theta, $phi, $lam], [$qubit1]);
    }

    public function sx(int $qubit1) {
        $this->addSingle("sx", [], [$qubit1]);
    }

    public function sxdg(int $qubit1) {
        $this->addSingle("sxdg", [], [$qubit1]);
    }

    public function r(float $theta, float $phi, int $qubit1) {
        $this->addSingle("r", [$theta, $phi], [$qubit1]);
    }

    public function cx(int $qubit1, int $qubit2) {
        $this->addDouble("cx", [], [$qubit1, $qubit2]);
    }

    public function cy(int $qubit1, int $qubit2) {
        $this->addDouble("cy", [], [$qubit1, $qubit2]);
    }

    public function cz(int $qubit1, int $qubit2) {
        $this->addDouble("cz", [], [$qubit1, $qubit2]);
    }

    public function ch(int $qubit1, int $qubit2) {
        $this->addDouble("ch", [], [$qubit1, $qubit2]);
    }

    public function ucrx(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("ucrx", [$theta], [$qubit1, $qubit2]);
    }

    public function ucry(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("ucry", [$theta], [$qubit1, $qubit2]);
    }

    public function ucrz(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("ucrz", [$theta], [$qubit1, $qubit2]);
    }

    public function crx(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("crx", [$theta], [$qubit1, $qubit2]);
    }

    public function cry(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("cry", [$theta], [$qubit1, $qubit2]);
    }

    public function crz(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("crz", [$theta], [$qubit1, $qubit2]);
    }

    public function cr(float $theta, float $phi, float $lam, int $qubit1, int $qubit2) {
        $this->addDouble("cr", [$theta, $phi, $lam], [$qubit1, $qubit2]);
    }

    public function cu(float $theta, float $phi, float $lam, float $gamma, int $qubit1, int $qubit2) {
        $this->addDouble("cu1", [$theta, $phi, $lam, $gamma], [$qubit1, $qubit2]);
    }

    public function cu1(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("cu1", [$theta], [$qubit1, $qubit2]);
    }

    public function cu2(float $phi, float $lam, int $qubit1, int $qubit2) {
        $this->addDouble("cu2", [$phi, $lam], [$qubit1, $qubit2]);
    }

    public function cu3(float $theta, float $phi, float $lam, int $qubit1, int $qubit2) {
        $this->addDouble("cu3", [$theta, $phi, $lam], [$qubit1, $qubit2]);
    }

    public function dcx(int $qubit1, int $qubit2) {
        $this->addDouble("dcx", [], [$qubit1, $qubit2]);
    }

    public function ecr(int $qubit1, int $qubit2) {
        $this->addDouble("ecr", [], [$qubit1, $qubit2]);
    }

    public function iswap(int $qubit1, int $qubit2) {
        $this->addDouble("iswap", [], [$qubit1, $qubit2]);
    }

    public function rxx(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("rxx", [$theta], [$qubit1, $qubit2]);
    }

    public function ryy(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("ryy", [$theta], [$qubit1, $qubit2]);
    }

    public function rzz(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("rzz", [$theta], [$qubit1, $qubit2]);
    }

    public function rzx(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("rzx", [$theta], [$qubit1, $qubit2]);
    }

    public function cswap(int $qubit1, int $qubit2, int $qubit3) {
        $this->addTriple("cswap", [], [$qubit1, $qubit2, $qubit3]);
    }

    public function ccx(int $qubit1, int $qubit2, int $qubit3) {
        $this->addTriple("ccx", [], [$qubit1, $qubit2, $qubit3]);
    }

    public function ccy(int $qubit1, int $qubit2, int $qubit3) {
        $this->addTriple("ccy", [], [$qubit1, $qubit2, $qubit3]);
    }

    public function ccz(int $qubit1, int $qubit2, int $qubit3) {
        $this->addTriple("ccz", [], [$qubit1, $qubit2, $qubit3]);
    }

    public function c3x(array $qubits) {
        $this->addMultiple("c3x", [], $qubits);
    }

    public function c4x(array $qubits) {
        $this->addMultiple("c4x", [], $qubits);
    }

    public function mcx(array $qubits) {
        $this->addMultiple("mcx", [], $qubits);
    }

    public function mcu1(float $theta, array $qubits) {
        $this->addMultiple("mcu1", [$theta], $qubits);
    }

    public function mcu2(float $phi, float $lam, array $qubits) {
        $this->addMultiple("mcu2", [$phi, $lam], $qubits);
    }

    public function mcu3(float $theta, float $phi, float $lam, array $qubits) {
        $this->addMultiple("mcu3", [$theta, $phi, $lam], $qubits);
    }

    public function mcz(array $qubits) {
        $this->addMultiple("mcz", [], $qubits);
    }

    public function mcp(array $qubits) {
        $this->addMultiple("mcp", [], $qubits);
    }

    public function mcrx(array $qubits) {
        $this->addMultiple("mcrx", [], $qubits);
    }

    public function mcry(array $qubits) {
        $this->addMultiple("mcry", [], $qubits);
    }

    public function mcrz(array $qubits) {
        $this->addMultiple("mcrz", [], $qubits);
    }

    public function qft(array $qubits) {
        $this->addMultiple("qft", [], $qubits);
    }

    public function inverse_qft(array $qubits) {
        $this->addMultiple("iqft", [], $qubits);
    }

    public function swap(int $qubit1, int $qubit2) {
        $this->addDouble("swap", [], [$qubit1, $qubit2]);
    }

    public function csx(int $qubit1, int $qubit2) {
        $this->addDouble("csx", [], [$qubit1, $qubit2]);
    }

    public function p(float $theta, int $qubit1) {
        $this->addSingle("p", [$theta], [$qubit1]);
    }

    public function cp(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("cp", [$theta], [$qubit1, $qubit2]);
    }

    public function ccp(float $theta, int $qubit1, int $qubit2, int $qubit3) {
        $this->addTriple("ccp", [$theta], [$qubit1, $qubit2, $qubit3]);
    }

    public function sqrt_x(int $qubit1) {
        $this->addSingle("sqrt_x", [], [$qubit1]);
    }

    public function sqrt_y(int $qubit1) {
        $this->addSingle("sqrt_y", [], [$qubit1]);
    }

    public function sqrt_z(int $qubit1) {
        $this->addSingle("sqrt_z", [], [$qubit1]);
    }

    public function gpi(float $phi, int $qubit1) {
        $this->addSingle("gpi", [$phi], [$qubit1]);
    }

    public function gpi2(float $phi, int $qubit1) {
        $this->addSingle("gpi2", [$phi], [$qubit1]);
    }

    public function xp(float $theta, int $qubit1) {
        $this->addSingle("xp", [$theta], [$qubit1]);
    }

    public function yp(float $theta, int $qubit1) {
        $this->addSingle("yp", [$theta], [$qubit1]);
    }

    public function zp(float $theta, int $qubit1) {
        $this->addSingle("zp", [$theta], [$qubit1]);
    }

    public function xxp(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("xxp", [$theta], [$qubit1, $qubit2]);
    }

    public function yyp(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("yyp", [$theta], [$qubit1, $qubit2]);
    }

    public function zzp(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("zzp", [$theta], [$qubit1, $qubit2]);
    }

    public function phased_xp(float $theta, float $phi, int $qubit1) {
        $this->addSingle("phased_xp", [$theta, $phi], [$qubit1]);
    }

    public function phased_yp(float $theta, float $phi, int $qubit1) {
        $this->addSingle("phased_yp", [$theta, $phi], [$qubit1]);
    }

    public function phased_zp(float $theta, float $phi, int $qubit1) {
        $this->addSingle("phased_zp", [$theta, $phi], [$qubit1]);
    }

    public function cnotp(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("cnotp", [$theta], [$qubit1, $qubit2]);
    }

    public function ccnotp(float $theta, int $qubit1, int $qubit2, int $qubit3) {
        $this->addTriple("ccnotp", [$theta], [$qubit1, $qubit2, $qubit3]);
    }

    public function cyp(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("cyp", [$theta], [$qubit1, $qubit2]);
    }

    public function ccyp(float $theta, int $qubit1, int $qubit2, int $qubit3) {
        $this->addTriple("ccyp", [$theta], [$qubit1, $qubit2, $qubit3]);
    }

    public function czp(float $theta, int $qubit1, int $qubit2) {
        $this->addDouble("czp", [$theta], [$qubit1, $qubit2]);
    }

    public function cczp(float $theta, int $qubit1, int $qubit2, int $qubit3) {
        $this->addTriple("cczp", [$theta], [$qubit1, $qubit2, $qubit3]);
    }

    public function measure(array $qubits) {
        $cparams = [];
        $cqubits = [];
        $cgate = "measure";
        if (empty($qubits)) {
            throw new InvalidArgumentException("number of qubits to measure cannot be zero");
        } else {
            foreach ($qubits as $qubit) {
                if ($qubit < 0 || $qubit >= $this->numQubits) {
                    throw new InvalidArgumentException("invalid qubit: " . $qubit);
                } else {
                    $cqubits[] = $qubit;
                }
            }
        }
        $this->operations[] = new Operation($cgate, $cqubits, $cparams);
    }

    public function measureAll() {
        $cparams = [];
        $cqubits = [];
        $cgate = "measure";
        for ($qubit = 0; $qubit < $this->numQubits; $qubit++) {
            $cqubits[] = $qubit;
        }
        $this->operations[] = new Operation($cgate, $cqubits, $cparams);
    }

    public function randomCircuit(int $numberOfOperations, array $qubitsToUseForRandomCircuit) {
        $qubitsCount = count($qubitsToUseForRandomCircuit);
        if ($qubitsCount < 3) {
            throw new InvalidArgumentException("The number of qubits needed to generate random circuits is >= 3");
        }

        $gatesAndQubitsMap = [
            // 1 qubit gates
            "x" => 1, "y" => 1, "z" => 1, "rx" => 1, "ry" => 1, "rz" => 1,
            "h" => 1, "s" => 1, "sdg" => 1, "t" => 1, "tdg" => 1, "sx" => 1, "sxdg" => 1,
            // 2 qubit gates
            "cx" => 2, "cy" => 2, "cz" => 2, "crx" => 2, "cry" => 2, "crz" => 2,
            "ch" => 2, "dcx" => 2, "ecr" => 2, "iswap" => 2, "swap" => 2, "csx" => 2,
            // 3 qubit gates
            "cswap" => 3, "ccx" => 3
        ];

        $allPossibleGates = array_keys($gatesAndQubitsMap);
        $allPossibleGatesCount = count($allPossibleGates);

        for ($i = 0; $i < $numberOfOperations; $i++) {
            $index = array_rand($allPossibleGates);
            $cgate = $allPossibleGates[$index];

            $numberOfQubits = $gatesAndQubitsMap[$cgate];

            shuffle($qubitsToUseForRandomCircuit);
            $cqubits = array_slice($qubitsToUseForRandomCircuit, 0, $numberOfQubits);

            $cparams = [];
            if (in_array($cgate, ["rx", "ry", "rz", "crx", "cry", "crz"])) {
                $theta = mt_rand() / mt_getrandmax() * 2 * M_PI;
                $cparams[] = $theta;
            }

            $this->operations[] = new Operation($cgate, $cqubits, $cparams);
        }
    }

}

?>