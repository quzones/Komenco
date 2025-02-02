package com.automatski.komenco;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.stream.Collectors;
import org.json.JSONObject;
import org.json.JSONArray;

public class AutomatskiKomencoNative {

    private String host;
    private int port;

    public AutomatskiKomencoNative(String host, int port) {
        this.host = host;
        this.port = port;
    }

    public Map<String, Integer> run(QuantumCircuit circuit, int repetitions, int topK) throws IOException {
        long tstart = System.currentTimeMillis();

        JSONObject body = serializeCircuit(circuit, topK);
        JSONObject struct = postRequest(body);

        long tend = System.currentTimeMillis();
        long executionTime = tend - tstart;
        System.out.println("Time Taken " + executionTime + "ms");

        if (struct.has("error")) {
            System.out.println(struct.getString("error"));
            throw new RuntimeException(struct.getString("error"));
        }

        return deserializeResult(struct, repetitions);
    }

    private JSONObject serializeCircuit(QuantumCircuit circuit, int topK) {
        int numQubits = circuit.getNumQubits();

        List<Map<String, Object>> operations = new ArrayList<>();
        List<Integer> measurements = new ArrayList<>();

        for (Operation operation : circuit.getOperations()) {
            String gate = operation.getGate();
            List<Double> params = operation.getParams();
            List<Integer> qubits = operation.getQubits();

            if ("measure".equals(gate)) {
                measurements.addAll(qubits);
            } else {
                Map<String, Object> op = new HashMap<>();
                op.put("gate", gate);
                op.put("params", params);
                op.put("qubits", qubits);
                operations.add(op);
            }
        }

        System.out.println("Executing Quantum Circuit With...");
        System.out.println(numQubits + " Qubits And ...");
        System.out.println(operations.size() + " Gates");

        if (measurements.isEmpty()) {
            throw new RuntimeException("There are no measurements done at the end of the circuit.");
        }

        JSONObject json = new JSONObject();
        json.put("num_qubits", numQubits);
        json.put("operations", operations);
        json.put("measurements", measurements);
        json.put("topK", topK);

        return json;
    }

    private JSONObject postRequest(JSONObject body) throws IOException {
        URL url = new URL("http://" + host + ":" + port + "/api/komenco");
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        connection.setDoOutput(true);
        connection.setRequestProperty("Content-Type", "application/json; utf-8");
        connection.setRequestProperty("Accept", "application/json");

        byte[] input = body.toString().getBytes(StandardCharsets.UTF_8);
        connection.getOutputStream().write(input, 0, input.length);

        Scanner scanner = new Scanner(connection.getInputStream(), StandardCharsets.UTF_8.name());
        String response = scanner.useDelimiter("\\A").next();
        scanner.close();

        return new JSONObject(response);
    }

    private static Map<String, Integer> deserializeResult(JSONObject responseData, int repetitions) {
        JSONObject measurementsStrings = responseData.getJSONObject("measurements");

        Map<String, Integer> measurements = new HashMap<>();
        for (Object ky : measurementsStrings.keySet()) {
        	String key = (String) ky;
            int count = (int) Math.round(measurementsStrings.getDouble(key) * repetitions);
            measurements.put(key, count);
        }

        return measurements;
    }

}