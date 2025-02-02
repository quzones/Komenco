import 'dart:convert';
import 'dart:io';
import 'dart:math';
import 'quantumcircuit.dart';

class AutomatskiKomencoNative {
  final String host;
  final int port;

  AutomatskiKomencoNative(this.host, this.port);

  Future<Map<String, int>> run(QuantumCircuit circuit, int repetitions, int topK) async {
    final tstart = DateTime.now().millisecondsSinceEpoch;

    final body = serializeCircuit(circuit, topK);
    final struct = await postRequest(body);

    final tend = DateTime.now().millisecondsSinceEpoch;
    final executionTime = tend - tstart;
    print("Time Taken ${executionTime}ms");

    if (struct.containsKey('error')) {
      print(struct['error']);
      throw Exception(struct['error']);
    }

    return deserializeResult(struct, repetitions);
  }

  Map<String, dynamic> serializeCircuit(QuantumCircuit circuit, int topK) {
    final numQubits = circuit.getNumQubits();

    final operations = <Map<String, dynamic>>[];
    final measurements = <int>[];

    for (final operation in circuit.getOperations()) {
      final gate = operation.getGate();
      final params = operation.getParams();
      final qubits = operation.getQubits();

      if (gate == "measure") {
        measurements.addAll(qubits);
      } else {
        final op = {
          "gate": gate,
          "params": params,
          "qubits": qubits
        };
        operations.add(op);
      }
    }

    print("Executing Quantum Circuit With...");
    print("$numQubits Qubits And ...");
    print("${operations.length} Gates");

    if (measurements.isEmpty) {
      throw Exception("There are no measurements done at the end of the circuit.");
    }

    return {
      "num_qubits": numQubits,
      "operations": operations,
      "measurements": measurements,
      "topK": topK
    };
  }

  Future<Map<String, dynamic>> postRequest(Map<String, dynamic> body) async {
    final url = Uri.parse("http://$host:$port/api/komenco");
    final request = await HttpClient().postUrl(url);
    request.headers.set(HttpHeaders.contentTypeHeader, "application/json");
    request.headers.set(HttpHeaders.acceptHeader, "application/json");
    request.write(jsonEncode(body));

    final response = await request.close();
    final responseBody = await response.transform(utf8.decoder).join();

    if (response.statusCode != 200) {
      throw Exception("Error making POST request");
    }

    return jsonDecode(responseBody);
  }

  Map<String, int> deserializeResult(Map<String, dynamic> responseData, int repetitions) {
    final measurementsStrings = responseData['measurements'] as Map<String, dynamic>;

    final measurements = <String, int>{};
    measurementsStrings.forEach((key, value) {
      final count = (value * repetitions).round();
      measurements[key] = count;
    });

    return measurements;
  }
}