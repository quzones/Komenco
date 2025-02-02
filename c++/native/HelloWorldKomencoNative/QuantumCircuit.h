#ifndef QUANTUM_CIRCUIT_H
#define QUANTUM_CIRCUIT_H

#include <string>
#include <vector>
#include <unordered_map>
#include <stdexcept>
#include <random>
#include <cmath>

class Operation {
private:
    std::string gate;
    std::vector<int> qubits;
    std::vector<double> params;

public:
    Operation(const std::string& gate, const std::vector<int>& qubits, const std::vector<double>& params);

    std::string getGate() const;
    std::vector<int> getQubits() const;
    std::vector<double> getParams() const;
};

class QuantumCircuit {
private:
    int numQubits;
    std::vector<Operation> operations;

    void addSingle(const std::string& gate, const std::vector<double>& params, const std::vector<int>& qubits);
    void addDouble(const std::string& gate, const std::vector<double>& params, const std::vector<int>& qubits);
    void addTriple(const std::string& gate, const std::vector<double>& params, const std::vector<int>& qubits);
    void addMultiple(const std::string& gate, const std::vector<double>& params, const std::vector<int>& qubits);

public:
    QuantumCircuit(int numQubits);

    int getNumQubits() const;
    std::vector<Operation> getOperations() const;

    void id(int qubit1);
    void x(int qubit1);
    void y(int qubit1);
    void z(int qubit1);
    void h(int qubit1);
    void s(int qubit1);
    void sdg(int qubit1);
    void t(int qubit1);
    void tdg(int qubit1);
    void rx(double theta, int qubit1);
    void ry(double theta, int qubit1);
    void rz(double theta, int qubit1);
    void u(double theta, double phi, double lam, int qubit1);
    void u1(double theta, int qubit1);
    void u2(double phi, double lam, int qubit1);
    void u3(double theta, double phi, double lam, int qubit1);
    void sx(int qubit1);
    void sxdg(int qubit1);
    void r(double theta, double phi, int qubit1);
    void cx(int qubit1, int qubit2);
    void cy(int qubit1, int qubit2);
    void cz(int qubit1, int qubit2);
    void ch(int qubit1, int qubit2);
    void ucrx(double theta, int qubit1, int qubit2);
    void ucry(double theta, int qubit1, int qubit2);
    void ucrz(double theta, int qubit1, int qubit2);
    void crx(double theta, int qubit1, int qubit2);
    void cry(double theta, int qubit1, int qubit2);
    void crz(double theta, int qubit1, int qubit2);
    void cr(double theta, double phi, double lam, int qubit1, int qubit2);
    void cu(double theta, double phi, double lam, double gamma, int qubit1, int qubit2);
    void cu1(double theta, int qubit1, int qubit2);
    void cu2(double phi, double lam, int qubit1, int qubit2);
    void cu3(double theta, double phi, double lam, int qubit1, int qubit2);
    void dcx(int qubit1, int qubit2);
    void ecr(int qubit1, int qubit2);
    void iswap(int qubit1, int qubit2);
    void rxx(double theta, int qubit1, int qubit2);
    void ryy(double theta, int qubit1, int qubit2);
    void rzz(double theta, int qubit1, int qubit2);
    void rzx(double theta, int qubit1, int qubit2);
    void cswap(int qubit1, int qubit2, int qubit3);
    void ccx(int qubit1, int qubit2, int qubit3);
    void ccy(int qubit1, int qubit2, int qubit3);
    void ccz(int qubit1, int qubit2, int qubit3);
    void c3x(const std::vector<int>& qubits);
    void c4x(const std::vector<int>& qubits);
    void mcx(const std::vector<int>& qubits);
    void mcu1(double theta, const std::vector<int>& qubits);
    void mcu2(double phi, double lam, const std::vector<int>& qubits);
    void mcu3(double theta, double phi, double lam, const std::vector<int>& qubits);
    void mcz(const std::vector<int>& qubits);
    void mcp(const std::vector<int>& qubits);
    void mcrx(const std::vector<int>& qubits);
    void mcry(const std::vector<int>& qubits);
    void mcrz(const std::vector<int>& qubits);
    void qft(const std::vector<int>& qubits);
    void inverse_qft(const std::vector<int>& qubits);
    void swap(int qubit1, int qubit2);
    void csx(int qubit1, int qubit2);
    void p(double theta, int qubit1);
    void cp(double theta, int qubit1, int qubit2);
    void ccp(double theta, int qubit1, int qubit2, int qubit3);
    void sqrt_x(int qubit1);
    void sqrt_y(int qubit1);
    void sqrt_z(int qubit1);
    void gpi(double phi, int qubit1);
    void gpi2(double phi, int qubit1);
    void xp(double theta, int qubit1);
    void yp(double theta, int qubit1);
    void zp(double theta, int qubit1);
    void xxp(double theta, int qubit1, int qubit2);
    void yyp(double theta, int qubit1, int qubit2);
    void zzp(double theta, int qubit1, int qubit2);
    void phased_xp(double theta, double phi, int qubit1);
    void phased_yp(double theta, double phi, int qubit1);
    void phased_zp(double theta, double phi, int qubit1);
    void cnotp(double theta, int qubit1, int qubit2);
    void ccnotp(double theta, int qubit1, int qubit2, int qubit3);
    void cyp(double theta, int qubit1, int qubit2);
    void ccyp(double theta, int qubit1, int qubit2, int qubit3);
    void czp(double theta, int qubit1, int qubit2);
    void cczp(double theta, int qubit1, int qubit2, int qubit3);
    void measure(const std::vector<int>& qubits);
    void measureAll();
    void randomCircuit(int numberOfOperations, std::vector<int> qubitsToUseForRandomCircuit);
};

#endif // QUANTUM_CIRCUIT_H