package com.automatski.komenco

import scala.collection.mutable.ListBuffer
import scala.util.Random
import scala.collection.mutable.{ArrayBuffer, ListBuffer}

class QuantumCircuit(val numQubits: Int) {
  private val operations = ListBuffer[Operation]()

  def getNumQubits: Int = numQubits

  def getOperations: List[Operation] = operations.toList

  private def addSingle(gate: String, params: List[Double], qubits: List[Int]): Unit = {
    if (qubits.size != 1) throw new IllegalArgumentException(s"Number of qubits for gate $gate has to be one")
    qubits.foreach { qubit =>
      if (qubit < 0 || qubit >= numQubits) throw new IllegalArgumentException(s"Invalid qubit: $qubit")
    }
    operations += Operation(gate, qubits, params)
  }

  private def addDouble(gate: String, params: List[Double], qubits: List[Int]): Unit = {
    if (qubits.size != 2) throw new IllegalArgumentException(s"Number of qubits for gate $gate has to be two")
    qubits.foreach { qubit =>
      if (qubit < 0 || qubit >= numQubits) throw new IllegalArgumentException(s"Invalid qubit: $qubit")
    }
    operations += Operation(gate, qubits, params)
  }

  private def addTriple(gate: String, params: List[Double], qubits: List[Int]): Unit = {
    if (qubits.size != 3) throw new IllegalArgumentException(s"Number of qubits for gate $gate has to be three")
    qubits.foreach { qubit =>
      if (qubit < 0 || qubit >= numQubits) throw new IllegalArgumentException(s"Invalid qubit: $qubit")
    }
    operations += Operation(gate, qubits, params)
  }

  private def addMultiple(gate: String, params: List[Double], qubits: List[Int]): Unit = {
    val requiredQubits = (Math.log(gate.length) / Math.log(2)).toInt
    if (qubits.size != requiredQubits) throw new IllegalArgumentException(s"Number of qubits for gate $gate has to be $requiredQubits")
    qubits.foreach { qubit =>
      if (qubit < 0 || qubit >= numQubits) throw new IllegalArgumentException(s"Invalid qubit: $qubit")
    }
    operations += Operation(gate, qubits, params)
  }

  def id(qubit1: Int): Unit = addSingle("id", List(), List(qubit1))

  def x(qubit1: Int): Unit = addSingle("x", List(), List(qubit1))

  def y(qubit1: Int): Unit = addSingle("y", List(), List(qubit1))

  def z(qubit1: Int): Unit = addSingle("z", List(), List(qubit1))

  def h(qubit1: Int): Unit = addSingle("h", List(), List(qubit1))

  def s(qubit1: Int): Unit = addSingle("s", List(), List(qubit1))

  def sdg(qubit1: Int): Unit = addSingle("sdg", List(), List(qubit1))

  def t(qubit1: Int): Unit = addSingle("t", List(), List(qubit1))

  def tdg(qubit1: Int): Unit = addSingle("tdg", List(), List(qubit1))

  def rx(theta: Double, qubit1: Int): Unit = addSingle("rx", List(theta), List(qubit1))

  def ry(theta: Double, qubit1: Int): Unit = addSingle("ry", List(theta), List(qubit1))

  def rz(theta: Double, qubit1: Int): Unit = addSingle("rz", List(theta), List(qubit1))

  def u(theta: Double, phi: Double, lam: Double, qubit1: Int): Unit = addSingle("u", List(theta, phi, lam), List(qubit1))

  def u1(theta: Double, qubit1: Int): Unit = addSingle("u1", List(theta), List(qubit1))

  def u2(phi: Double, lam: Double, qubit1: Int): Unit = addSingle("u2", List(phi, lam), List(qubit1))

  def u3(theta: Double, phi: Double, lam: Double, qubit1: Int): Unit = addSingle("u3", List(theta, phi, lam), List(qubit1))

  def sx(qubit1: Int): Unit = addSingle("sx", List(), List(qubit1))

  def sxdg(qubit1: Int): Unit = addSingle("sxdg", List(), List(qubit1))

  def r(theta: Double, phi: Double, qubit1: Int): Unit = addSingle("r", List(theta, phi), List(qubit1))

  def cx(qubit1: Int, qubit2: Int): Unit = addDouble("cx", List(), List(qubit1, qubit2))

  def cy(qubit1: Int, qubit2: Int): Unit = addDouble("cy", List(), List(qubit1, qubit2))

  def cz(qubit1: Int, qubit2: Int): Unit = addDouble("cz", List(), List(qubit1, qubit2))

  def ch(qubit1: Int, qubit2: Int): Unit = addDouble("ch", List(), List(qubit1, qubit2))

  def ucrx(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("ucrx", List(theta), List(qubit1, qubit2))

  def ucry(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("ucry", List(theta), List(qubit1, qubit2))

  def ucrz(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("ucrz", List(theta), List(qubit1, qubit2))

  def crx(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("crx", List(theta), List(qubit1, qubit2))

  def cry(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("cry", List(theta), List(qubit1, qubit2))

  def crz(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("crz", List(theta), List(qubit1, qubit2))

  def cr(theta: Double, phi: Double, lam: Double, qubit1: Int, qubit2: Int): Unit = addDouble("cr", List(theta, phi, lam), List(qubit1, qubit2))

  def cu(theta: Double, phi: Double, lam: Double, gamma: Double, qubit1: Int, qubit2: Int): Unit = addDouble("cu1", List(theta, phi, lam, gamma), List(qubit1, qubit2))

  def cu1(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("cu1", List(theta), List(qubit1, qubit2))

  def cu2(phi: Double, lam: Double, qubit1: Int, qubit2: Int): Unit = addDouble("cu2", List(phi, lam), List(qubit1, qubit2))

  def cu3(theta: Double, phi: Double, lam: Double, qubit1: Int, qubit2: Int): Unit = addDouble("cu3", List(theta, phi, lam), List(qubit1, qubit2))

  def dcx(qubit1: Int, qubit2: Int): Unit = addDouble("dcx", List(), List(qubit1, qubit2))

  def ecr(qubit1: Int, qubit2: Int): Unit = addDouble("ecr", List(), List(qubit1, qubit2))

  def iswap(qubit1: Int, qubit2: Int): Unit = addDouble("iswap", List(), List(qubit1, qubit2))

  def rxx(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("rxx", List(theta), List(qubit1, qubit2))

  def ryy(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("ryy", List(theta), List(qubit1, qubit2))

  def rzz(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("rzz", List(theta), List(qubit1, qubit2))

  def rzx(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("rzx", List(theta), List(qubit1, qubit2))

  def cswap(qubit1: Int, qubit2: Int, qubit3: Int): Unit = addTriple("cswap", List(), List(qubit1, qubit2, qubit3))

  def ccx(qubit1: Int, qubit2: Int, qubit3: Int): Unit = addTriple("ccx", List(), List(qubit1, qubit2, qubit3))

  def ccy(qubit1: Int, qubit2: Int, qubit3: Int): Unit = addTriple("ccy", List(), List(qubit1, qubit2, qubit3))

  def ccz(qubit1: Int, qubit2: Int, qubit3: Int): Unit = addTriple("ccz", List(), List(qubit1, qubit2, qubit3))

  def c3x(qubits: List[Int]): Unit = addMultiple("c3x", List(), qubits)

  def c4x(qubits: List[Int]): Unit = addMultiple("c4x", List(), qubits)

  def mcx(qubits: List[Int]): Unit = addMultiple("mcx", List(), qubits)

  def mcu1(theta: Double, qubits: List[Int]): Unit = addMultiple("mcu1", List(theta), qubits)

  def mcu2(phi: Double, lam: Double, qubits: List[Int]): Unit = addMultiple("mcu2", List(phi, lam), qubits)

  def mcu3(theta: Double, phi: Double, lam: Double, qubits: List[Int]): Unit = addMultiple("mcu3", List(theta, phi, lam), qubits)

  def mcz(qubits: List[Int]): Unit = addMultiple("mcz", List(), qubits)

  def mcp(qubits: List[Int]): Unit = addMultiple("mcp", List(), qubits)

  def mcrx(qubits: List[Int]): Unit = addMultiple("mcrx", List(), qubits)

  def mcry(qubits: List[Int]): Unit = addMultiple("mcry", List(), qubits)

  def mcrz(qubits: List[Int]): Unit = addMultiple("mcrz", List(), qubits)

  def qft(qubits: List[Int]): Unit = addMultiple("qft", List(), qubits)

  def inverse_qft(qubits: List[Int]): Unit = addMultiple("iqft", List(), qubits)

  def swap(qubit1: Int, qubit2: Int): Unit = addDouble("swap", List(), List(qubit1, qubit2))

  def csx(qubit1: Int, qubit2: Int): Unit = addDouble("csx", List(), List(qubit1, qubit2))

  def p(theta: Double, qubit1: Int): Unit = addSingle("p", List(theta), List(qubit1))

  def cp(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("cp", List(theta), List(qubit1, qubit2))

  def ccp(theta: Double, qubit1: Int, qubit2: Int, qubit3: Int): Unit = addTriple("ccp", List(theta), List(qubit1, qubit2, qubit3))

  def sqrt_x(qubit1: Int): Unit = addSingle("sqrt_x", List(), List(qubit1))

  def sqrt_y(qubit1: Int): Unit = addSingle("sqrt_y", List(), List(qubit1))

  def sqrt_z(qubit1: Int): Unit = addSingle("sqrt_z", List(), List(qubit1))

  def gpi(phi: Double, qubit1: Int): Unit = addSingle("gpi", List(phi), List(qubit1))

  def gpi2(phi: Double, qubit1: Int): Unit = addSingle("gpi2", List(phi), List(qubit1))

  def xp(theta: Double, qubit1: Int): Unit = addSingle("xp", List(theta), List(qubit1))

  def yp(theta: Double, qubit1: Int): Unit = addSingle("yp", List(theta), List(qubit1))

  def zp(theta: Double, qubit1: Int): Unit = addSingle("zp", List(theta), List(qubit1))

  def xxp(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("xxp", List(theta), List(qubit1, qubit2))

  def yyp(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("yyp", List(theta), List(qubit1, qubit2))

  def zzp(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("zzp", List(theta), List(qubit1, qubit2))

  def phased_xp(theta: Double, phi: Double, qubit1: Int): Unit = addSingle("phased_xp", List(theta, phi), List(qubit1))

  def phased_yp(theta: Double, phi: Double, qubit1: Int): Unit = addSingle("phased_yp", List(theta, phi), List(qubit1))

  def phased_zp(theta: Double, phi: Double, qubit1: Int): Unit = addSingle("phased_zp", List(theta, phi), List(qubit1))

  def cnotp(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("cnotp", List(theta), List(qubit1, qubit2))

  def ccnotp(theta: Double, qubit1: Int, qubit2: Int, qubit3: Int): Unit = addTriple("ccnotp", List(theta), List(qubit1, qubit2, qubit3))

  def cyp(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("cyp", List(theta), List(qubit1, qubit2))

  def ccyp(theta: Double, qubit1: Int, qubit2: Int, qubit3: Int): Unit = addTriple("ccyp", List(theta), List(qubit1, qubit2, qubit3))

  def czp(theta: Double, qubit1: Int, qubit2: Int): Unit = addDouble("czp", List(theta), List(qubit1, qubit2))

  def cczp(theta: Double, qubit1: Int, qubit2: Int, qubit3: Int): Unit = addTriple("cczp", List(theta), List(qubit1, qubit2, qubit3))

  def measure(qubits: List[Int]): Unit = {
    val cparams = List[Double]()
    val cqubits = ListBuffer[Int]()
    val cgate = "measure"
    if (qubits.isEmpty) {
      throw new RuntimeException("number of qubits to measure cannot be zero")
    } else {
      qubits.foreach { qubit =>
        if (qubit < 0 || qubit >= this.numQubits) {
          throw new RuntimeException(s"invalid qubit: $qubit")
        } else {
          cqubits += qubit
        }
      }
    }
    operations += Operation(cgate, cqubits.toList, cparams)
  }

  def measureAll(): Unit = {
    val cparams = List[Double]()
    val cqubits = (0 until this.numQubits).toList
    val cgate = "measure"
    operations += Operation(cgate, cqubits, cparams)
  }

   def randomCircuit(numberOfOperations: Int, qubitsToUseForRandomCircuit: List[Int]): Unit = {
    val qubitsCount = qubitsToUseForRandomCircuit.size
    if (qubitsCount < 3) {
      throw new RuntimeException("The number of qubits needed to generate random circuits is >= 3")
    }

    val gatesAndQubitsMap = Map(
      // 1 qubit gates
      "x" -> 1, "y" -> 1, "z" -> 1, "rx" -> 1, "ry" -> 1, "rz" -> 1,
      "h" -> 1, "s" -> 1, "sdg" -> 1, "t" -> 1, "tdg" -> 1, "sx" -> 1, "sxdg" -> 1,
      // 2 qubit gates
      "cx" -> 2, "cy" -> 2, "cz" -> 2, "crx" -> 2, "cry" -> 2, "crz" -> 2,
      "ch" -> 2, "dcx" -> 2, "ecr" -> 2, "iswap" -> 2, "swap" -> 2, "csx" -> 2,
      // 3 qubit gates
      "cswap" -> 3, "ccx" -> 3
    )

    val allPossibleGates = gatesAndQubitsMap.keys.toList
    val allPossibleGatesCount = allPossibleGates.size

    val random = new Random()
    for (_ <- 0 until numberOfOperations) {
      val index = random.nextInt(allPossibleGatesCount)
      val cgate = allPossibleGates(index)

      val numberOfQubits = gatesAndQubitsMap(cgate)

      val shuffledQubits = Random.shuffle(qubitsToUseForRandomCircuit)
      val cqubits = shuffledQubits.take(numberOfQubits)

      val cparams = ArrayBuffer[Double]()
      if (List("rx", "ry", "rz", "crx", "cry", "crz").contains(cgate)) {
        val theta = random.nextDouble() * 2 * Math.PI
        cparams += theta
      }

      operations += Operation(cgate, cqubits, cparams.toList)
    }
  }

}