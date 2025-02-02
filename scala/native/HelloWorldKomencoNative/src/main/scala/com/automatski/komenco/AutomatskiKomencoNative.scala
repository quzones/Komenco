package com.automatski.komenco

import java.io.{IOException, OutputStreamWriter}
import java.net.{HttpURLConnection, URL}
import java.nio.charset.StandardCharsets
import scala.collection.mutable
import scala.io.Source
import org.json.JSONObject
import scala.collection.JavaConverters._

class AutomatskiKomencoNative(val host: String, val port: Int) {

  def run(circuit: QuantumCircuit, repetitions: Int, topK: Int): Map[String, Int] = {
    val tstart = System.currentTimeMillis()

    val body = serializeCircuit(circuit, topK)

    val struct = postRequest(body)

    val tend = System.currentTimeMillis()
    val executionTime = tend - tstart
    println(s"Time Taken $executionTime ms")

    if (struct.has("error")) {
      println(struct.getString("error"))
      throw new RuntimeException(struct.getString("error"))
    }

    deserializeResult(struct, repetitions)
  }

  private def serializeCircuit(circuit: QuantumCircuit, topK: Int): JSONObject = {
    val numQubits = circuit.getNumQubits

    val operations = new mutable.ListBuffer[Map[String, Any]]()
    val measurements = new mutable.ListBuffer[Int]()

    for (operation <- circuit.getOperations) {
      val gate = operation.getGate
      val params = operation.getParams
      val qubits = operation.getQubits

      if (gate == "measure") {
        measurements ++= qubits
      } else {
        val op = Map(
          "gate" -> gate,
          "params" -> params.asJava,
          "qubits" -> qubits.asJava
        )
        operations += op
      }
    }

    println(s"Executing Quantum Circuit With...")
    println(s"$numQubits Qubits And ...")
    println(s"${operations.size} Gates")

    if (measurements.isEmpty) {
      throw new RuntimeException("There are no measurements done at the end of the circuit.")
    }

    val json = new JSONObject()
    json.put("num_qubits", numQubits)
    json.put("operations", operations.map(_.asJava).asJava)
    json.put("measurements", measurements.asJava)
    json.put("topK", topK)

    json
  }

  private def postRequest(body: JSONObject): JSONObject = {
    val url = new URL(s"http://$host:$port/api/komenco")
    val connection = url.openConnection().asInstanceOf[HttpURLConnection]
    connection.setRequestMethod("POST")
    connection.setDoOutput(true)
    connection.setRequestProperty("Content-Type", "application/json; utf-8")
    connection.setRequestProperty("Accept", "application/json")

    val writer = new OutputStreamWriter(connection.getOutputStream, StandardCharsets.UTF_8)
    writer.write(body.toString)
    writer.flush()
    writer.close()

    val response = Source.fromInputStream(connection.getInputStream, StandardCharsets.UTF_8.name).mkString
    new JSONObject(response)
  }

  private def deserializeResult(responseData: JSONObject, repetitions: Int): Map[String, Int] = {
    val measurementsStrings = responseData.getJSONObject("measurements")

    val measurements = mutable.Map[String, Int]()
    measurementsStrings.keys().asScala.foreach { key =>
      val strKey = key.asInstanceOf[String]
      val count = (measurementsStrings.getDouble(strKey) * repetitions).round.toInt
      measurements.put(strKey, count)
    }

    measurements.toMap
  }
}