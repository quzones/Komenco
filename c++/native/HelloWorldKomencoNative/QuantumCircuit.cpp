#include <vector>
#include <string>
#include <unordered_map>
#include <stdexcept>
#include <algorithm>
#include <random>
#include <cmath>
#include <iostream>
#include "QuantumCircuit.h"


Operation::Operation(const std::string& gate, const std::vector<int>& qubits, const std::vector<double>& params)
    : gate(gate), qubits(qubits), params(params) {}

std::string Operation::getGate() const {
    return gate;
}

std::vector<int> Operation::getQubits() const {
    return qubits;
}

std::vector<double> Operation::getParams() const {
    return params;
}


void QuantumCircuit::addSingle(const std::string& gate, const std::vector<double>& params, const std::vector<int>& qubits) {
    if (qubits.size() != 1) {
        throw std::invalid_argument("Number of qubits for gate " + gate + " has to be one");
    }
    for (int qubit : qubits) {
        if (qubit < 0 || qubit >= numQubits) {
            throw std::invalid_argument("Invalid qubit: " + std::to_string(qubit));
        }
    }
    operations.emplace_back(gate, qubits, params);
}

void QuantumCircuit::addDouble(const std::string& gate, const std::vector<double>& params, const std::vector<int>& qubits) {
    if (qubits.size() != 2) {
        throw std::invalid_argument("Number of qubits for gate " + gate + " has to be two");
    }
    for (int qubit : qubits) {
        if (qubit < 0 || qubit >= numQubits) {
            throw std::invalid_argument("Invalid qubit: " + std::to_string(qubit));
        }
    }
    operations.emplace_back(gate, qubits, params);
}

void QuantumCircuit::addTriple(const std::string& gate, const std::vector<double>& params, const std::vector<int>& qubits) {
    if (qubits.size() != 3) {
        throw std::invalid_argument("Number of qubits for gate " + gate + " has to be three");
    }
    for (int qubit : qubits) {
        if (qubit < 0 || qubit >= numQubits) {
            throw std::invalid_argument("Invalid qubit: " + std::to_string(qubit));
        }
    }
    operations.emplace_back(gate, qubits, params);
}

void QuantumCircuit::addMultiple(const std::string& gate, const std::vector<double>& params, const std::vector<int>& qubits) {
    int requiredQubits = static_cast<int>(std::log(gate.length()) / std::log(2));
    if (qubits.size() != requiredQubits) {
        throw std::invalid_argument("Number of qubits for gate " + gate + " has to be " + std::to_string(requiredQubits));
    }
    for (int qubit : qubits) {
        if (qubit < 0 || qubit >= numQubits) {
            throw std::invalid_argument("Invalid qubit: " + std::to_string(qubit));
        }
    }
    operations.emplace_back(gate, qubits, params);
}

QuantumCircuit::QuantumCircuit(int numQubits) : numQubits(numQubits) {}

int QuantumCircuit::getNumQubits() const {
    return numQubits;
}

std::vector<Operation> QuantumCircuit::getOperations() const {
    return operations;
}

void QuantumCircuit::id(int qubit1) {
    addSingle("id", {}, {qubit1});
}

void QuantumCircuit::x(int qubit1) {
    addSingle("x", {}, {qubit1});
}

void QuantumCircuit::y(int qubit1) {
    addSingle("y", {}, {qubit1});
}

void QuantumCircuit::z(int qubit1) {
    addSingle("z", {}, {qubit1});
}

void QuantumCircuit::h(int qubit1) {
    addSingle("h", {}, {qubit1});
}

void QuantumCircuit::s(int qubit1) {
    addSingle("s", {}, {qubit1});
}

void QuantumCircuit::sdg(int qubit1) {
    addSingle("sdg", {}, {qubit1});
}

void QuantumCircuit::t(int qubit1) {
    addSingle("t", {}, {qubit1});
}

void QuantumCircuit::tdg(int qubit1) {
    addSingle("tdg", {}, {qubit1});
}

void QuantumCircuit::rx(double theta, int qubit1) {
    addSingle("rx", {theta}, {qubit1});
}

void QuantumCircuit::ry(double theta, int qubit1) {
    addSingle("ry", {theta}, {qubit1});
}

void QuantumCircuit::rz(double theta, int qubit1) {
    addSingle("rz", {theta}, {qubit1});
}

void QuantumCircuit::u(double theta, double phi, double lam, int qubit1) {
    addSingle("u", {theta, phi, lam}, {qubit1});
}

void QuantumCircuit::u1(double theta, int qubit1) {
    addSingle("u1", {theta}, {qubit1});
}

void QuantumCircuit::u2(double phi, double lam, int qubit1) {
    addSingle("u2", {phi, lam}, {qubit1});
}

void QuantumCircuit::u3(double theta, double phi, double lam, int qubit1) {
    addSingle("u3", {theta, phi, lam}, {qubit1});
}

void QuantumCircuit::sx(int qubit1) {
    addSingle("sx", {}, {qubit1});
}

void QuantumCircuit::sxdg(int qubit1) {
    addSingle("sxdg", {}, {qubit1});
}

void QuantumCircuit::r(double theta, double phi, int qubit1) {
    addSingle("r", {theta, phi}, {qubit1});
}

void QuantumCircuit::cx(int qubit1, int qubit2) {
    addDouble("cx", {}, {qubit1, qubit2});
}

void QuantumCircuit::cy(int qubit1, int qubit2) {
    addDouble("cy", {}, {qubit1, qubit2});
}

void QuantumCircuit::cz(int qubit1, int qubit2) {
    addDouble("cz", {}, {qubit1, qubit2});
}

void QuantumCircuit::ch(int qubit1, int qubit2) {
    addDouble("ch", {}, {qubit1, qubit2});
}

void QuantumCircuit::ucrx(double theta, int qubit1, int qubit2) {
    addDouble("ucrx", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::ucry(double theta, int qubit1, int qubit2) {
    addDouble("ucry", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::ucrz(double theta, int qubit1, int qubit2) {
    addDouble("ucrz", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::crx(double theta, int qubit1, int qubit2) {
    addDouble("crx", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::cry(double theta, int qubit1, int qubit2) {
    addDouble("cry", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::crz(double theta, int qubit1, int qubit2) {
    addDouble("crz", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::cr(double theta, double phi, double lam, int qubit1, int qubit2) {
    addDouble("cr", {theta, phi, lam}, {qubit1, qubit2});
}

void QuantumCircuit::cu(double theta, double phi, double lam, double gamma, int qubit1, int qubit2) {
    addDouble("cu1", {theta, phi, lam, gamma}, {qubit1, qubit2});
}

void QuantumCircuit::cu1(double theta, int qubit1, int qubit2) {
    addDouble("cu1", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::cu2(double phi, double lam, int qubit1, int qubit2) {
    addDouble("cu2", {phi, lam}, {qubit1, qubit2});
}

void QuantumCircuit::cu3(double theta, double phi, double lam, int qubit1, int qubit2) {
    addDouble("cu3", {theta, phi, lam}, {qubit1, qubit2});
}

void QuantumCircuit::dcx(int qubit1, int qubit2) {
    addDouble("dcx", {}, {qubit1, qubit2});
}

void QuantumCircuit::ecr(int qubit1, int qubit2) {
    addDouble("ecr", {}, {qubit1, qubit2});
}

void QuantumCircuit::iswap(int qubit1, int qubit2) {
    addDouble("iswap", {}, {qubit1, qubit2});
}

void QuantumCircuit::rxx(double theta, int qubit1, int qubit2) {
    addDouble("rxx", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::ryy(double theta, int qubit1, int qubit2) {
    addDouble("ryy", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::rzz(double theta, int qubit1, int qubit2) {
    addDouble("rzz", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::rzx(double theta, int qubit1, int qubit2) {
    addDouble("rzx", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::cswap(int qubit1, int qubit2, int qubit3) {
    addTriple("cswap", {}, {qubit1, qubit2, qubit3});
}

void QuantumCircuit::ccx(int qubit1, int qubit2, int qubit3) {
    addTriple("ccx", {}, {qubit1, qubit2, qubit3});
}

void QuantumCircuit::ccy(int qubit1, int qubit2, int qubit3) {
    addTriple("ccy", {}, {qubit1, qubit2, qubit3});
}

void QuantumCircuit::ccz(int qubit1, int qubit2, int qubit3) {
    addTriple("ccz", {}, {qubit1, qubit2, qubit3});
}

void QuantumCircuit::c3x(const std::vector<int>& qubits) {
    addMultiple("c3x", {}, qubits);
}

void QuantumCircuit::c4x(const std::vector<int>& qubits) {
    addMultiple("c4x", {}, qubits);
}

void QuantumCircuit::mcx(const std::vector<int>& qubits) {
    addMultiple("mcx", {}, qubits);
}

void QuantumCircuit::mcu1(double theta, const std::vector<int>& qubits) {
    addMultiple("mcu1", {theta}, qubits);
}

void QuantumCircuit::mcu2(double phi, double lam, const std::vector<int>& qubits) {
    addMultiple("mcu2", {phi, lam}, qubits);
}

void QuantumCircuit::mcu3(double theta, double phi, double lam, const std::vector<int>& qubits) {
    addMultiple("mcu3", {theta, phi, lam}, qubits);
}

void QuantumCircuit::mcz(const std::vector<int>& qubits) {
    addMultiple("mcz", {}, qubits);
}

void QuantumCircuit::mcp(const std::vector<int>& qubits) {
    addMultiple("mcp", {}, qubits);
}

void QuantumCircuit::mcrx(const std::vector<int>& qubits) {
    addMultiple("mcrx", {}, qubits);
}

void QuantumCircuit::mcry(const std::vector<int>& qubits) {
    addMultiple("mcry", {}, qubits);
}

void QuantumCircuit::mcrz(const std::vector<int>& qubits) {
    addMultiple("mcrz", {}, qubits);
}

void QuantumCircuit::qft(const std::vector<int>& qubits) {
    addMultiple("qft", {}, qubits);
}

void QuantumCircuit::inverse_qft(const std::vector<int>& qubits) {
    addMultiple("iqft", {}, qubits);
}

void QuantumCircuit::swap(int qubit1, int qubit2) {
    addDouble("swap", {}, {qubit1, qubit2});
}

void QuantumCircuit::csx(int qubit1, int qubit2) {
    addDouble("csx", {}, {qubit1, qubit2});
}

void QuantumCircuit::p(double theta, int qubit1) {
    addSingle("p", {theta}, {qubit1});
}

void QuantumCircuit::cp(double theta, int qubit1, int qubit2) {
    addDouble("cp", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::ccp(double theta, int qubit1, int qubit2, int qubit3) {
    addTriple("ccp", {theta}, {qubit1, qubit2, qubit3});
}

void QuantumCircuit::sqrt_x(int qubit1) {
    addSingle("sqrt_x", {}, {qubit1});
}

void QuantumCircuit::sqrt_y(int qubit1) {
    addSingle("sqrt_y", {}, {qubit1});
}

void QuantumCircuit::sqrt_z(int qubit1) {
    addSingle("sqrt_z", {}, {qubit1});
}

void QuantumCircuit::gpi(double phi, int qubit1) {
    addSingle("gpi", {phi}, {qubit1});
}

void QuantumCircuit::gpi2(double phi, int qubit1) {
    addSingle("gpi2", {phi}, {qubit1});
}

void QuantumCircuit::xp(double theta, int qubit1) {
    addSingle("xp", {theta}, {qubit1});
}

void QuantumCircuit::yp(double theta, int qubit1) {
    addSingle("yp", {theta}, {qubit1});
}

void QuantumCircuit::zp(double theta, int qubit1) {
    addSingle("zp", {theta}, {qubit1});
}

void QuantumCircuit::xxp(double theta, int qubit1, int qubit2) {
    addDouble("xxp", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::yyp(double theta, int qubit1, int qubit2) {
    addDouble("yyp", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::zzp(double theta, int qubit1, int qubit2) {
    addDouble("zzp", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::phased_xp(double theta, double phi, int qubit1) {
    addSingle("phased_xp", {theta, phi}, {qubit1});
}

void QuantumCircuit::phased_yp(double theta, double phi, int qubit1) {
    addSingle("phased_yp", {theta, phi}, {qubit1});
}

void QuantumCircuit::phased_zp(double theta, double phi, int qubit1) {
    addSingle("phased_zp", {theta, phi}, {qubit1});
}

void QuantumCircuit::cnotp(double theta, int qubit1, int qubit2) {
    addDouble("cnotp", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::ccnotp(double theta, int qubit1, int qubit2, int qubit3) {
    addTriple("ccnotp", {theta}, {qubit1, qubit2, qubit3});
}

void QuantumCircuit::cyp(double theta, int qubit1, int qubit2) {
    addDouble("cyp", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::ccyp(double theta, int qubit1, int qubit2, int qubit3) {
    addTriple("ccyp", {theta}, {qubit1, qubit2, qubit3});
}

void QuantumCircuit::czp(double theta, int qubit1, int qubit2) {
    addDouble("czp", {theta}, {qubit1, qubit2});
}

void QuantumCircuit::cczp(double theta, int qubit1, int qubit2, int qubit3) {
    addTriple("cczp", {theta}, {qubit1, qubit2, qubit3});
}

void QuantumCircuit::measure(const std::vector<int>& qubits) {
    std::vector<double> cparams;
    std::vector<int> cqubits;
    std::string cgate = "measure";
    if (qubits.empty()) {
        throw std::invalid_argument("number of qubits to measure cannot be zero");
    } else {
        for (int qubit : qubits) {
            if (qubit < 0 || qubit >= numQubits) {
                throw std::invalid_argument("invalid qubit: " + std::to_string(qubit));
            } else {
                cqubits.push_back(qubit);
            }
        }
    }
    operations.emplace_back(cgate, cqubits, cparams);
}

void QuantumCircuit::measureAll() {
    std::vector<double> cparams;
    std::vector<int> cqubits;
    std::string cgate = "measure";
    for (int qubit = 0; qubit < numQubits; qubit++) {
        cqubits.push_back(qubit);
    }
    operations.emplace_back(cgate, cqubits, cparams);
}

void QuantumCircuit::randomCircuit(int numberOfOperations, std::vector<int> qubitsToUseForRandomCircuit) {
    int qubitsCount = qubitsToUseForRandomCircuit.size();
    if (qubitsCount < 3) {
        throw std::invalid_argument("The number of qubits needed to generate random circuits is >= 3");
    }

    std::unordered_map<std::string, int> gatesAndQubitsMap = {
        // 1 qubit gates
        {"x", 1}, {"y", 1}, {"z", 1}, {"rx", 1}, {"ry", 1}, {"rz", 1},
        {"h", 1}, {"s", 1}, {"sdg", 1}, {"t", 1}, {"tdg", 1}, {"sx", 1}, {"sxdg", 1},
        // 2 qubit gates
        {"cx", 2}, {"cy", 2}, {"cz", 2}, {"crx", 2}, {"cry", 2}, {"crz", 2},
        {"ch", 2}, {"dcx", 2}, {"ecr", 2}, {"iswap", 2}, {"swap", 2}, {"csx", 2},
        // 3 qubit gates
        {"cswap", 3}, {"ccx", 3}
    };

    std::vector<std::string> allPossibleGates;
    for (const auto& gate : gatesAndQubitsMap) {
        allPossibleGates.push_back(gate.first);
    }
    int allPossibleGatesCount = allPossibleGates.size();

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> gateDist(0, allPossibleGatesCount - 1);
    std::uniform_real_distribution<> paramDist(0, 2 * M_PI);

    for (int i = 0; i < numberOfOperations; ++i) {
        int index = gateDist(gen);
        std::string cgate = allPossibleGates[index];

        int numberOfQubits = gatesAndQubitsMap[cgate];

        std::shuffle(qubitsToUseForRandomCircuit.begin(), qubitsToUseForRandomCircuit.end(), gen);
        std::vector<int> cqubits(qubitsToUseForRandomCircuit.begin(), qubitsToUseForRandomCircuit.begin() + numberOfQubits);

        std::vector<double> cparams;
        if (cgate == "rx" || cgate == "ry" || cgate == "rz" || cgate == "crx" || cgate == "cry" || cgate == "crz") {
            double theta = paramDist(gen);
            cparams.push_back(theta);
        }

        operations.push_back(Operation(cgate, cqubits, cparams));
    }
}

