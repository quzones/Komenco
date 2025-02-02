import 'dart:math';

class Operation {
  final String gate;
  final List<int> qubits;
  final List<double> params;

  Operation(this.gate, this.qubits, this.params);

  String getGate() {
    return gate;
  }

  List<int> getQubits() {
    return qubits;
  }

  List<double> getParams() {
    return params;
  }
}

class QuantumCircuit {
  final int numQubits;
  final List<Operation> operations = [];

  QuantumCircuit(this.numQubits);

  int getNumQubits() {
    return numQubits;
  }

  List<Operation> getOperations() {
    return operations;
  }

  void _addSingle(String gate, List<double> params, List<int> qubits) {
    if (qubits.length != 1) {
      throw ArgumentError("Number of qubits for gate $gate has to be one");
    }
    for (var qubit in qubits) {
      if (qubit < 0 || qubit >= numQubits) {
        throw ArgumentError("Invalid qubit: $qubit");
      }
    }
    operations.add(Operation(gate, qubits, params));
  }

  void _addDouble(String gate, List<double> params, List<int> qubits) {
    if (qubits.length != 2) {
      throw ArgumentError("Number of qubits for gate $gate has to be two");
    }
    for (var qubit in qubits) {
      if (qubit < 0 || qubit >= numQubits) {
        throw ArgumentError("Invalid qubit: $qubit");
      }
    }
    operations.add(Operation(gate, qubits, params));
  }

  void _addTriple(String gate, List<double> params, List<int> qubits) {
    if (qubits.length != 3) {
      throw ArgumentError("Number of qubits for gate $gate has to be three");
    }
    for (var qubit in qubits) {
      if (qubit < 0 || qubit >= numQubits) {
        throw ArgumentError("Invalid qubit: $qubit");
      }
    }
    operations.add(Operation(gate, qubits, params));
  }

  void _addMultiple(String gate, List<double> params, List<int> qubits) {
    int requiredQubits = (log(gate.length) / log(2)).toInt();
    if (qubits.length != requiredQubits) {
      throw ArgumentError("Number of qubits for gate $gate has to be $requiredQubits");
    }
    for (var qubit in qubits) {
      if (qubit < 0 || qubit >= numQubits) {
        throw ArgumentError("Invalid qubit: $qubit");
      }
    }
    operations.add(Operation(gate, qubits, params));
  }

  void id(int qubit1) {
    _addSingle("id", [], [qubit1]);
  }

  void x(int qubit1) {
    _addSingle("x", [], [qubit1]);
  }

  void y(int qubit1) {
    _addSingle("y", [], [qubit1]);
  }

  void z(int qubit1) {
    _addSingle("z", [], [qubit1]);
  }

  void h(int qubit1) {
    _addSingle("h", [], [qubit1]);
  }

  void s(int qubit1) {
    _addSingle("s", [], [qubit1]);
  }

  void sdg(int qubit1) {
    _addSingle("sdg", [], [qubit1]);
  }

  void t(int qubit1) {
    _addSingle("t", [], [qubit1]);
  }

  void tdg(int qubit1) {
    _addSingle("tdg", [], [qubit1]);
  }

  void rx(double theta, int qubit1) {
    _addSingle("rx", [theta], [qubit1]);
  }

  void ry(double theta, int qubit1) {
    _addSingle("ry", [theta], [qubit1]);
  }

  void rz(double theta, int qubit1) {
    _addSingle("rz", [theta], [qubit1]);
  }

  void u(double theta, double phi, double lam, int qubit1) {
    _addSingle("u", [theta, phi, lam], [qubit1]);
  }

  void u1(double theta, int qubit1) {
    _addSingle("u1", [theta], [qubit1]);
  }

  void u2(double phi, double lam, int qubit1) {
    _addSingle("u2", [phi, lam], [qubit1]);
  }

  void u3(double theta, double phi, double lam, int qubit1) {
    _addSingle("u3", [theta, phi, lam], [qubit1]);
  }

  void sx(int qubit1) {
    _addSingle("sx", [], [qubit1]);
  }

  void sxdg(int qubit1) {
    _addSingle("sxdg", [], [qubit1]);
  }

  void r(double theta, double phi, int qubit1) {
    _addSingle("r", [theta, phi], [qubit1]);
  }

  void cx(int qubit1, int qubit2) {
    _addDouble("cx", [], [qubit1, qubit2]);
  }

  void cy(int qubit1, int qubit2) {
    _addDouble("cy", [], [qubit1, qubit2]);
  }

  void cz(int qubit1, int qubit2) {
    _addDouble("cz", [], [qubit1, qubit2]);
  }

  void ch(int qubit1, int qubit2) {
    _addDouble("ch", [], [qubit1, qubit2]);
  }

  void ucrx(double theta, int qubit1, int qubit2) {
    _addDouble("ucrx", [theta], [qubit1, qubit2]);
  }

  void ucry(double theta, int qubit1, int qubit2) {
    _addDouble("ucry", [theta], [qubit1, qubit2]);
  }

  void ucrz(double theta, int qubit1, int qubit2) {
    _addDouble("ucrz", [theta], [qubit1, qubit2]);
  }

  void crx(double theta, int qubit1, int qubit2) {
    _addDouble("crx", [theta], [qubit1, qubit2]);
  }

  void cry(double theta, int qubit1, int qubit2) {
    _addDouble("cry", [theta], [qubit1, qubit2]);
  }

  void crz(double theta, int qubit1, int qubit2) {
    _addDouble("crz", [theta], [qubit1, qubit2]);
  }

  void cr(double theta, double phi, double lam, int qubit1, int qubit2) {
    _addDouble("cr", [theta, phi, lam], [qubit1, qubit2]);
  }

  void cu(double theta, double phi, double lam, double gamma, int qubit1, int qubit2) {
    _addDouble("cu1", [theta, phi, lam, gamma], [qubit1, qubit2]);
  }

  void cu1(double theta, int qubit1, int qubit2) {
    _addDouble("cu1", [theta], [qubit1, qubit2]);
  }

  void cu2(double phi, double lam, int qubit1, int qubit2) {
    _addDouble("cu2", [phi, lam], [qubit1, qubit2]);
  }

  void cu3(double theta, double phi, double lam, int qubit1, int qubit2) {
    _addDouble("cu3", [theta, phi, lam], [qubit1, qubit2]);
  }

  void dcx(int qubit1, int qubit2) {
    _addDouble("dcx", [], [qubit1, qubit2]);
  }

  void ecr(int qubit1, int qubit2) {
    _addDouble("ecr", [], [qubit1, qubit2]);
  }

  void iswap(int qubit1, int qubit2) {
    _addDouble("iswap", [], [qubit1, qubit2]);
  }

  void rxx(double theta, int qubit1, int qubit2) {
    _addDouble("rxx", [theta], [qubit1, qubit2]);
  }

  void ryy(double theta, int qubit1, int qubit2) {
    _addDouble("ryy", [theta], [qubit1, qubit2]);
  }

  void rzz(double theta, int qubit1, int qubit2) {
    _addDouble("rzz", [theta], [qubit1, qubit2]);
  }

  void rzx(double theta, int qubit1, int qubit2) {
    _addDouble("rzx", [theta], [qubit1, qubit2]);
  }

  void cswap(int qubit1, int qubit2, int qubit3) {
    _addTriple("cswap", [], [qubit1, qubit2, qubit3]);
  }

  void ccx(int qubit1, int qubit2, int qubit3) {
    _addTriple("ccx", [], [qubit1, qubit2, qubit3]);
  }

  void ccy(int qubit1, int qubit2, int qubit3) {
    _addTriple("ccy", [], [qubit1, qubit2, qubit3]);
  }

  void ccz(int qubit1, int qubit2, int qubit3) {
    _addTriple("ccz", [], [qubit1, qubit2, qubit3]);
  }

  void c3x(List<int> qubits) {
    _addMultiple("c3x", [], qubits);
  }

  void c4x(List<int> qubits) {
    _addMultiple("c4x", [], qubits);
  }

  void mcx(List<int> qubits) {
    _addMultiple("mcx", [], qubits);
  }

  void mcu1(double theta, List<int> qubits) {
    _addMultiple("mcu1", [theta], qubits);
  }

  void mcu2(double phi, double lam, List<int> qubits) {
    _addMultiple("mcu2", [phi, lam], qubits);
  }

  void mcu3(double theta, double phi, double lam, List<int> qubits) {
    _addMultiple("mcu3", [theta, phi, lam], qubits);
  }

  void mcz(List<int> qubits) {
    _addMultiple("mcz", [], qubits);
  }

  void mcp(List<int> qubits) {
    _addMultiple("mcp", [], qubits);
  }

  void mcrx(List<int> qubits) {
    _addMultiple("mcrx", [], qubits);
  }

  void mcry(List<int> qubits) {
    _addMultiple("mcry", [], qubits);
  }

  void mcrz(List<int> qubits) {
    _addMultiple("mcrz", [], qubits);
  }

  void qft(List<int> qubits) {
    _addMultiple("qft", [], qubits);
  }

  void inverseQft(List<int> qubits) {
    _addMultiple("iqft", [], qubits);
  }

  void swap(int qubit1, int qubit2) {
    _addDouble("swap", [], [qubit1, qubit2]);
  }

  void csx(int qubit1, int qubit2) {
    _addDouble("csx", [], [qubit1, qubit2]);
  }

  void p(double theta, int qubit1) {
    _addSingle("p", [theta], [qubit1]);
  }

  void cp(double theta, int qubit1, int qubit2) {
    _addDouble("cp", [theta], [qubit1, qubit2]);
  }

  void ccp(double theta, int qubit1, int qubit2, int qubit3) {
    _addTriple("ccp", [theta], [qubit1, qubit2, qubit3]);
  }

  void sqrtX(int qubit1) {
    _addSingle("sqrt_x", [], [qubit1]);
  }

  void sqrtY(int qubit1) {
    _addSingle("sqrt_y", [], [qubit1]);
  }

  void sqrtZ(int qubit1) {
    _addSingle("sqrt_z", [], [qubit1]);
  }

  void gpi(double phi, int qubit1) {
    _addSingle("gpi", [phi], [qubit1]);
  }

  void gpi2(double phi, int qubit1) {
    _addSingle("gpi2", [phi], [qubit1]);
  }

  void xp(double theta, int qubit1) {
    _addSingle("xp", [theta], [qubit1]);
  }

  void yp(double theta, int qubit1) {
    _addSingle("yp", [theta], [qubit1]);
  }

  void zp(double theta, int qubit1) {
    _addSingle("zp", [theta], [qubit1]);
  }

  void xxp(double theta, int qubit1, int qubit2) {
    _addDouble("xxp", [theta], [qubit1, qubit2]);
  }

  void yyp(double theta, int qubit1, int qubit2) {
    _addDouble("yyp", [theta], [qubit1, qubit2]);
  }

  void zzp(double theta, int qubit1, int qubit2) {
    _addDouble("zzp", [theta], [qubit1, qubit2]);
  }

  void phasedXp(double theta, double phi, int qubit1) {
    _addSingle("phased_xp", [theta, phi], [qubit1]);
  }

  void phasedYp(double theta, double phi, int qubit1) {
    _addSingle("phased_yp", [theta, phi], [qubit1]);
  }

  void phasedZp(double theta, double phi, int qubit1) {
    _addSingle("phased_zp", [theta, phi], [qubit1]);
  }

  void cnotp(double theta, int qubit1, int qubit2) {
    _addDouble("cnotp", [theta], [qubit1, qubit2]);
  }

  void ccnotp(double theta, int qubit1, int qubit2, int qubit3) {
    _addTriple("ccnotp", [theta], [qubit1, qubit2, qubit3]);
  }

  void cyp(double theta, int qubit1, int qubit2) {
    _addDouble("cyp", [theta], [qubit1, qubit2]);
  }

  void ccyp(double theta, int qubit1, int qubit2, int qubit3) {
    _addTriple("ccyp", [theta], [qubit1, qubit2, qubit3]);
  }

  void czp(double theta, int qubit1, int qubit2) {
    _addDouble("czp", [theta], [qubit1, qubit2]);
  }

  void cczp(double theta, int qubit1, int qubit2, int qubit3) {
    _addTriple("cczp", [theta], [qubit1, qubit2, qubit3]);
  }

  void measure(List<int> qubits) {
    List<double> cparams = [];
    List<int> cqubits = [];
    String cgate = "measure";
    if (qubits.isEmpty) {
      throw ArgumentError("number of qubits to measure cannot be zero");
    } else {
      for (var qubit in qubits) {
        if (qubit < 0 || qubit >= numQubits) {
          throw ArgumentError("invalid qubit: $qubit");
        } else {
          cqubits.add(qubit);
        }
      }
    }
    operations.add(Operation(cgate, cqubits, cparams));
  }

  void measureAll() {
    List<double> cparams = [];
    List<int> cqubits = [];
    String cgate = "measure";
    for (var qubit = 0; qubit < numQubits; qubit++) {
      cqubits.add(qubit);
    }
    operations.add(Operation(cgate, cqubits, cparams));
  }

  void randomCircuit(int numberOfOperations, List<int> qubitsToUseForRandomCircuit) {
    int qubitsCount = qubitsToUseForRandomCircuit.length;
    if (qubitsCount < 3) {
      throw ArgumentError("The number of qubits needed to generate random circuits is >= 3");
    }

    Map<String, int> gatesAndQubitsMap = {
      // 1 qubit gates
      "x": 1, "y": 1, "z": 1, "rx": 1, "ry": 1, "rz": 1,
      "h": 1, "s": 1, "sdg": 1, "t": 1, "tdg": 1, "sx": 1, "sxdg": 1,
      // 2 qubit gates
      "cx": 2, "cy": 2, "cz": 2, "crx": 2, "cry": 2, "crz": 2,
      "ch": 2, "dcx": 2, "ecr": 2, "iswap": 2, "swap": 2, "csx": 2,
      // 3 qubit gates
      "cswap": 3, "ccx": 3
    };

    List<String> allPossibleGates = gatesAndQubitsMap.keys.toList();
    int allPossibleGatesCount = allPossibleGates.length;
    Random random = Random();

    for (int i = 0; i < numberOfOperations; i++) {
      int index = random.nextInt(allPossibleGatesCount);
      String cgate = allPossibleGates[index];

      int numberOfQubits = gatesAndQubitsMap[cgate]!;

      qubitsToUseForRandomCircuit.shuffle(random);
      List<int> cqubits = qubitsToUseForRandomCircuit.sublist(0, numberOfQubits);

      List<double> cparams = [];
      if (["rx", "ry", "rz", "crx", "cry", "crz"].contains(cgate)) {
        double theta = random.nextDouble() * 2 * pi;
        cparams.add(theta);
      }

      operations.add(Operation(cgate, cqubits, cparams));
    }
  }
}