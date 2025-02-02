package com.automatski.komenco;

import java.util.List;

public class Operation {

	private String gate;
	private List<Integer> qubits;
	private List<Double> params;
	
	public Operation(String gate, List<Integer> qubits, List<Double> params) {
		this.gate = gate;
		this.qubits = qubits;
		this.params = params;
		
	}

	public String getGate() {
		return gate;
	}

	public List<Integer> getQubits() {
		return qubits;
	}

	public List<Double> getParams() {
		return params;
	}
	
	
}
