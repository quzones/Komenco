package com.automatski.komenco

case class Operation(gate: String, qubits: List[Int], params: List[Double]) {

  def getGate: String = gate

  def getQubits: List[Int] = qubits

  def getParams: List[Double] = params
}