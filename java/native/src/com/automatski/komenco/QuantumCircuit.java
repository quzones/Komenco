package com.automatski.komenco;

import java.util.*;

public class QuantumCircuit {
    private int numQubits;
    private List<Operation> operations;

    public QuantumCircuit(int numQubits) {
        this.numQubits = numQubits;
        this.operations = new ArrayList<Operation>();
    }

    
    
    public int getNumQubits() {
		return numQubits;
	}



	public List<Operation> getOperations() {
		return operations;
	}



	private void addSingle(String gate, List<Double> params, List<Integer> qubits) {
        if (qubits.size() != 1) {
            throw new IllegalArgumentException("Number of qubits for gate " + gate + " has to be one");
        }
        for (int qubit : qubits) {
            if (qubit < 0 || qubit >= numQubits) {
                throw new IllegalArgumentException("Invalid qubit: " + qubit);
            }
        }
        operations.add(new Operation(gate,qubits,params));
    }

    private void addDouble(String gate, List<Double> params, List<Integer> qubits) {
        if (qubits.size() != 2) {
            throw new IllegalArgumentException("Number of qubits for gate " + gate + " has to be two");
        }
        for (int qubit : qubits) {
            if (qubit < 0 || qubit >= numQubits) {
                throw new IllegalArgumentException("Invalid qubit: " + qubit);
            }
        }
        operations.add(new Operation(gate,qubits,params));
    }

    private void addTriple(String gate, List<Double> params, List<Integer> qubits) {
        if (qubits.size() != 3) {
            throw new IllegalArgumentException("Number of qubits for gate " + gate + " has to be three");
        }
        for (int qubit : qubits) {
            if (qubit < 0 || qubit >= numQubits) {
                throw new IllegalArgumentException("Invalid qubit: " + qubit);
            }
        }
        operations.add(new Operation(gate,qubits,params));
    }

    private void addMultiple(String gate, List<Double> params, List<Integer> qubits) {
        int requiredQubits = (int) (Math.log(gate.length()) / Math.log(2));
        if (qubits.size() != requiredQubits) {
            throw new IllegalArgumentException("Number of qubits for gate " + gate + " has to be " + requiredQubits);
        }
        for (int qubit : qubits) {
            if (qubit < 0 || qubit >= numQubits) {
                throw new IllegalArgumentException("Invalid qubit: " + qubit);
            }
        }
        operations.add(new Operation(gate,qubits,params));
    }

    public void id(int qubit1) {
        addSingle("id", new ArrayList<>(), List.of(qubit1));
    }

    public void x(int qubit1) {
        addSingle("x", new ArrayList<>(), List.of(qubit1));
    }

    public void y(int qubit1) {
        addSingle("y", new ArrayList<>(), List.of(qubit1));
    }

    public void z(int qubit1) {
        addSingle("z", new ArrayList<>(), List.of(qubit1));
    }

    public void h(int qubit1) {
        addSingle("h", new ArrayList<>(), List.of(qubit1));
    }

    public void s(int qubit1) {
        addSingle("s", new ArrayList<>(), List.of(qubit1));
    }

    public void sdg(int qubit1) {
        addSingle("sdg", new ArrayList<>(), List.of(qubit1));
    }

    public void t(int qubit1) {
        addSingle("t", new ArrayList<>(), List.of(qubit1));
    }

    public void tdg(int qubit1) {
        addSingle("tdg", new ArrayList<>(), List.of(qubit1));
    }

    public void rx(double theta, int qubit1) {
        addSingle("rx", List.of(theta), List.of(qubit1));
    }

    public void ry(double theta, int qubit1) {
        addSingle("ry", List.of(theta), List.of(qubit1));
    }

    public void rz(double theta, int qubit1) {
        addSingle("rz", List.of(theta), List.of(qubit1));
    }

    public void u(double theta, double phi, double lam, int qubit1) {
        addSingle("u", List.of(theta, phi, lam), List.of(qubit1));
    }

    public void u1(double theta, int qubit1) {
        addSingle("u1", List.of(theta), List.of(qubit1));
    }

    public void u2(double phi, double lam, int qubit1) {
        addSingle("u2", List.of(phi, lam), List.of(qubit1));
    }

    public void u3(double theta, double phi, double lam, int qubit1) {
        addSingle("u3", List.of(theta, phi, lam), List.of(qubit1));
    }

    public void sx(int qubit1) {
        addSingle("sx", new ArrayList<>(), List.of(qubit1));
    }

    public void sxdg(int qubit1) {
        addSingle("sxdg", new ArrayList<>(), List.of(qubit1));
    }

    public void r(double theta, double phi, int qubit1) {
        addSingle("r", List.of(theta, phi), List.of(qubit1));
    }

    public void cx(int qubit1, int qubit2) {
        addDouble("cx", new ArrayList<>(), List.of(qubit1, qubit2));
    }

    public void cy(int qubit1, int qubit2) {
    	addDouble("cy", new ArrayList<>(), List.of(qubit1, qubit2));
    }

    public void cz(int qubit1, int qubit2) {
    	addDouble("cz", new ArrayList<>(), List.of(qubit1, qubit2));
    }

    public void ch(int qubit1, int qubit2) {
    	addDouble("ch", new ArrayList<>(), List.of(qubit1, qubit2));
    }

    public void ucrx(double theta, int qubit1, int qubit2) {
    	addDouble("ucrx", List.of(theta), List.of(qubit1, qubit2));
    }

    public void ucry(double theta, int qubit1, int qubit2) {
    	addDouble("ucry", List.of(theta), List.of(qubit1, qubit2));
    }

    public void ucrz(double theta, int qubit1, int qubit2) {
    	addDouble("ucrz", List.of(theta), List.of(qubit1, qubit2));
    }

    public void crx(double theta, int qubit1, int qubit2) {
    	addDouble("crx", List.of(theta), List.of(qubit1, qubit2));
    }

    public void cry(double theta, int qubit1, int qubit2) {
    	addDouble("cry", List.of(theta), List.of(qubit1, qubit2));
    }

    public void crz(double theta, int qubit1, int qubit2) {
    	addDouble("crz", List.of(theta), List.of(qubit1, qubit2));
    }

    public void cr(double theta, double phi, double lam, int qubit1, int qubit2) {
    	addDouble("cr", List.of(theta, phi, lam), List.of(qubit1, qubit2));
    }

    public void cu(double theta, double phi, double lam, double gamma, int qubit1, int qubit2) {
    	addDouble("cu1", List.of(theta, phi, lam, gamma), List.of(qubit1, qubit2));
    }

    public void cu1(double theta, int qubit1, int qubit2) {
    	addDouble("cu1", List.of(theta), List.of(qubit1, qubit2));
    }

    public void cu2(double phi, double lam, int qubit1, int qubit2) {
    	addDouble("cu2", List.of(phi, lam), List.of(qubit1, qubit2));
    }

    public void cu3(double theta, double phi, double lam, int qubit1, int qubit2) {
    	addDouble("cu3", List.of(theta, phi, lam), List.of(qubit1, qubit2));
    }

    public void dcx(int qubit1, int qubit2) {
    	addDouble("dcx", new ArrayList<>(), List.of(qubit1, qubit2));
    }

    public void ecr(int qubit1, int qubit2) {
    	addDouble("ecr", new ArrayList<>(), List.of(qubit1, qubit2));
    }

    public void iswap(int qubit1, int qubit2) {
    	addDouble("iswap", new ArrayList<>(), List.of(qubit1, qubit2));
    }

    public void rxx(double theta, int qubit1, int qubit2) {
    	addDouble("rxx", List.of(theta), List.of(qubit1, qubit2));
    }

    public void ryy(double theta, int qubit1, int qubit2) {
    	addDouble("ryy", List.of(theta), List.of(qubit1, qubit2));
    }

    public void rzz(double theta, int qubit1, int qubit2) {
    	addDouble("rzz", List.of(theta), List.of(qubit1, qubit2));
    }

    public void rzx(double theta, int qubit1, int qubit2) {
    	addDouble("rzx", List.of(theta), List.of(qubit1, qubit2));
    }

    public void cswap(int qubit1, int qubit2, int qubit3) {
        addTriple("cswap", new ArrayList<>(), List.of(qubit1, qubit2, qubit3));
    }

    public void ccx(int qubit1, int qubit2, int qubit3) {
        addTriple("ccx", new ArrayList<>(), List.of(qubit1, qubit2, qubit3));
    }

    public void ccy(int qubit1, int qubit2, int qubit3) {
        addTriple("ccy", new ArrayList<>(), List.of(qubit1, qubit2, qubit3));
    }

    public void ccz(int qubit1, int qubit2, int qubit3) {
        addTriple("ccz", new ArrayList<>(), List.of(qubit1, qubit2, qubit3));
    }

    public void c3x(List<Integer> qubits) {
        addMultiple("c3x", new ArrayList<>(), qubits);
    }

    public void c4x(List<Integer> qubits) {
        addMultiple("c4x", new ArrayList<>(), qubits);
    }

    public void mcx(List<Integer> qubits) {
        addMultiple("mcx", new ArrayList<>(), qubits);
    }

    public void mcu1(double theta, List<Integer> qubits) {
        addMultiple("mcu1", Arrays.asList(theta), qubits);
    }

    public void mcu2(double phi, double lam, List<Integer> qubits) {
        addMultiple("mcu2", Arrays.asList(phi, lam), qubits);
    }

    public void mcu3(double theta, double phi, double lam, List<Integer> qubits) {
        addMultiple("mcu3", Arrays.asList(theta, phi, lam), qubits);
    }

    public void mcz(List<Integer> qubits) {
        addMultiple("mcz", new ArrayList<>(), qubits);
    }

    public void mcp(List<Integer> qubits) {
        addMultiple("mcp", new ArrayList<>(), qubits);
    }

    public void mcrx(List<Integer> qubits) {
        addMultiple("mcrx", new ArrayList<>(), qubits);
    }

    public void mcry(List<Integer> qubits) {
        addMultiple("mcry", new ArrayList<>(), qubits);
    }

    public void mcrz(List<Integer> qubits) {
        addMultiple("mcrz", new ArrayList<>(), qubits);
    }

    public void qft(List<Integer> qubits) {
        addMultiple("qft", new ArrayList<>(), qubits);
    }

    public void inverse_qft(List<Integer> qubits) {
        addMultiple("iqft", new ArrayList<>(), qubits);
    }

    public void swap(int qubit1, int qubit2) {
        addDouble("swap", new ArrayList<>(), Arrays.asList(qubit1, qubit2));
    }

    public void csx(int qubit1, int qubit2) {
        addDouble("csx", new ArrayList<>(), Arrays.asList(qubit1, qubit2));
    }

    public void p(double theta, int qubit1) {
        addSingle("p", Arrays.asList(theta), Arrays.asList(qubit1));
    }

    public void cp(double theta, int qubit1, int qubit2) {
        addDouble("cp", Arrays.asList(theta), Arrays.asList(qubit1, qubit2));
    }

    public void ccp(double theta, int qubit1, int qubit2, int qubit3) {
        addTriple("ccp", Arrays.asList(theta), Arrays.asList(qubit1, qubit2, qubit3));
    }

    public void sqrt_x(int qubit1) {
        addSingle("sqrt_x", new ArrayList<>(), Arrays.asList(qubit1));
    }

    public void sqrt_y(int qubit1) {
        addSingle("sqrt_y", new ArrayList<>(), Arrays.asList(qubit1));
    }

    public void sqrt_z(int qubit1) {
        addSingle("sqrt_z", new ArrayList<>(), Arrays.asList(qubit1));
    }

    public void gpi(double phi, int qubit1) {
        addSingle("gpi", Arrays.asList(phi), Arrays.asList(qubit1));
    }

    public void gpi2(double phi, int qubit1) {
        addSingle("gpi2", Arrays.asList(phi), Arrays.asList(qubit1));
    }

    public void xp(double theta, int qubit1) {
        addSingle("xp", Arrays.asList(theta), Arrays.asList(qubit1));
    }

    public void yp(double theta, int qubit1) {
        addSingle("yp", Arrays.asList(theta), Arrays.asList(qubit1));
    }

    public void zp(double theta, int qubit1) {
        addSingle("zp", Arrays.asList(theta), Arrays.asList(qubit1));
    }

    public void xxp(double theta, int qubit1, int qubit2) {
        addDouble("xxp", Arrays.asList(theta), Arrays.asList(qubit1, qubit2));
    }

    public void yyp(double theta, int qubit1, int qubit2) {
        addDouble("yyp", Arrays.asList(theta), Arrays.asList(qubit1, qubit2));
    }

    public void zzp(double theta, int qubit1, int qubit2) {
        addDouble("zzp", Arrays.asList(theta), Arrays.asList(qubit1, qubit2));
    }

    public void phased_xp(double theta, double phi, int qubit1) {
        addSingle("phased_xp", Arrays.asList(theta, phi), Arrays.asList(qubit1));
    }

    public void phased_yp(double theta, double phi, int qubit1) {
        addSingle("phased_yp", Arrays.asList(theta, phi), Arrays.asList(qubit1));
    }

    public void phased_zp(double theta, double phi, int qubit1) {
        addSingle("phased_zp", Arrays.asList(theta, phi), Arrays.asList(qubit1));
    }

    public void cnotp(double theta, int qubit1, int qubit2) {
    	addDouble("cnotp", Arrays.asList(theta), Arrays.asList(qubit1, qubit2));
    }

    public void ccnotp(double theta, int qubit1, int qubit2, int qubit3) {
        addTriple("ccnotp", Arrays.asList(theta), Arrays.asList(qubit1, qubit2, qubit3));
    }

    public void cyp(double theta, int qubit1, int qubit2) {
    	addDouble("cyp", Arrays.asList(theta), Arrays.asList(qubit1, qubit2));
    }

    public void ccyp(double theta, int qubit1, int qubit2, int qubit3) {
        addTriple("ccyp", Arrays.asList(theta), Arrays.asList(qubit1, qubit2, qubit3));
    }

    public void czp(double theta, int qubit1, int qubit2) {
    	addDouble("czp", Arrays.asList(theta), Arrays.asList(qubit1, qubit2));
    }

    public void cczp(double theta, int qubit1, int qubit2, int qubit3) {
    	addTriple("cczp", Arrays.asList(theta), Arrays.asList(qubit1, qubit2, qubit3));
    }

    public void measure(List<Integer> qubits) {
        List<Double> cparams = new ArrayList<>();
        List<Integer> cqubits = new ArrayList<>();
        String cgate = "measure";
        if (qubits.isEmpty()) {
            throw new RuntimeException("number of qubits to measure cannot be zero");
        } else {
            for (int qubit : qubits) {
                if (qubit < 0 || qubit >= this.numQubits) {
                    throw new RuntimeException("invalid qubit: " + qubit);
                } else {
                    cqubits.add(qubit);
                }
            }
        }
        operations.add(new Operation(cgate, cqubits, cparams));
    }

    public void measureAll() {
        List<Double> cparams = new ArrayList<>();
        List<Integer> cqubits = new ArrayList<>();
        String cgate = "measure";
        for (int qubit = 0; qubit < this.numQubits; qubit++) {
            cqubits.add(qubit);
        }
        operations.add(new Operation(cgate, cqubits,cparams));
    }

    public void randomCircuit(int numberOfOperations, List<Integer> qubitsToUseForRandomCircuit) {
        int qubitsCount = qubitsToUseForRandomCircuit.size();
        if (qubitsCount < 3) {
            throw new RuntimeException("The number of qubits needed to generate random circuits is >= 3");
        }

        Map<String, Integer> gatesAndQubitsMap = new HashMap<>();
        // 1 qubit gates
        gatesAndQubitsMap.put("x", 1);
        gatesAndQubitsMap.put("y", 1);
        gatesAndQubitsMap.put("z", 1);
        gatesAndQubitsMap.put("rx", 1);
        gatesAndQubitsMap.put("ry", 1);
        gatesAndQubitsMap.put("rz", 1);
        gatesAndQubitsMap.put("h", 1);
        gatesAndQubitsMap.put("s", 1);
        gatesAndQubitsMap.put("sdg", 1);
        gatesAndQubitsMap.put("t", 1);
        gatesAndQubitsMap.put("tdg", 1);
        gatesAndQubitsMap.put("sx", 1);
        gatesAndQubitsMap.put("sxdg", 1);
        // 2 qubit gates
        gatesAndQubitsMap.put("cx", 2);
        gatesAndQubitsMap.put("cy", 2);
        gatesAndQubitsMap.put("cz", 2);
        gatesAndQubitsMap.put("crx", 2);
        gatesAndQubitsMap.put("cry", 2);
        gatesAndQubitsMap.put("crz", 2);
        gatesAndQubitsMap.put("ch", 2);
        gatesAndQubitsMap.put("dcx", 2);
        gatesAndQubitsMap.put("ecr", 2);
        gatesAndQubitsMap.put("iswap", 2);
        gatesAndQubitsMap.put("swap", 2);
        gatesAndQubitsMap.put("csx", 2);
        // 3 qubit gates
        gatesAndQubitsMap.put("cswap", 3);
        gatesAndQubitsMap.put("ccx", 3);

        List<String> allPossibleGates = new ArrayList<>(gatesAndQubitsMap.keySet());
        int allPossibleGatesCount = allPossibleGates.size();

        Random random = new Random();
        for (int i = 0; i < numberOfOperations; i++) {
            int index = random.nextInt(allPossibleGatesCount);
            String cgate = allPossibleGates.get(index);

            int numberOfQubits = gatesAndQubitsMap.get(cgate);

            Collections.shuffle(qubitsToUseForRandomCircuit);
            List<Integer> cqubits = new ArrayList<>();
            for (int j = 0; j < numberOfQubits; j++) {
                cqubits.add(qubitsToUseForRandomCircuit.get(j));
            }

            List<Double> cparams = new ArrayList<>();
            if (Arrays.asList("rx", "ry", "rz", "crx", "cry", "crz").contains(cgate)) {
                double theta = random.nextDouble() * 2 * Math.PI;
                cparams.add(theta);
            }

            operations.add(new Operation(cgate, cqubits, cparams));
        }
    }

}