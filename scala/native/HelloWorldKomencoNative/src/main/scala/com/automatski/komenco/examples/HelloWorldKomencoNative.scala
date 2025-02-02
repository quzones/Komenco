package com.automatski.komenco.examples

import java.util.{ArrayList, Collections}
import scala.collection.JavaConverters._
import scala.util.{Failure, Success, Try}

import org.knowm.xchart.{CategoryChart, CategoryChartBuilder, SwingWrapper}
import org.knowm.xchart.style.Styler

import com.automatski.komenco.{AutomatskiKomencoNative, QuantumCircuit}

object HelloWorldKomencoNative {

  def main(args: Array[String]): Unit = {
    // Create a sample quantum circuit to create a 3 Qubit GHZ State
    val circuit = new QuantumCircuit(3)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.cx(0, 2)
    circuit.measureAll()

    // Run the Circuit using Automatski' Quantum Simulators and Quantum Computers 
    val sampler = new AutomatskiKomencoNative("103.212.120.18", 80)

    // Run the circuit and get results
    val results : Map[String, Int] = Try(sampler.run(circuit, 1000, 20)) match {
      case Success(res) => res
      case Failure(e) =>
        e.printStackTrace()
        return
    }

    // Extract and count the measurement results
    val measurements : Map[String, Int] = results
    println(measurements)

    val labels = new java.util.ArrayList[String](measurements.keySet.asJava)
    Collections.sort(labels)
    val values = labels.asScala.map(label => measurements.getOrElse(label, 0)).toList.asJava

    // Plot the results
    val chart = new CategoryChartBuilder()
      .width(800)
      .height(600)
      .title("Quantum States & Counts Histogram")
      .xAxisTitle("Measurement Outcomes")
      .yAxisTitle("Counts")
      .build()

    chart.getStyler.setLegendPosition(Styler.LegendPosition.InsideNW)
    // chart.getStyler.setHasAnnotations(true)
    chart.getStyler.setXAxisLabelRotation(90)

    chart.addSeries("Counts", labels.asInstanceOf[java.util.List[String]], values.asInstanceOf[java.util.List[Integer]])

    new SwingWrapper(chart).displayChart()
  }
}