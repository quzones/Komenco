#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <stdexcept>
#include <chrono>
#include <cmath>
#include <curl/curl.h>
#include <jsoncpp/json/json.h>
#include "QuantumCircuit.h"
#include "AutomatskiKomencoNative.h"

// Constructor
AutomatskiKomencoNative::AutomatskiKomencoNative(const std::string& host, int port)
    : host(host), port(port) {}

// Run method
std::unordered_map<std::string, int> AutomatskiKomencoNative::run(QuantumCircuit& circuit, int repetitions, int topK) {
    auto tstart = std::chrono::high_resolution_clock::now();

    Json::Value body = serializeCircuit(circuit, topK);
    Json::Value struct_ = postRequest(body);

    auto tend = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> executionTime = tend - tstart;
    std::cout << "Time Taken " << executionTime.count() << "ms\n";

    if (struct_.isMember("error")) {
        std::cout << struct_["error"].asString() << "\n";
        throw std::runtime_error(struct_["error"].asString());
    }

    return deserializeResult(struct_, repetitions);
}

// Serialize Circuit method
Json::Value AutomatskiKomencoNative::serializeCircuit(QuantumCircuit& circuit, int topK) {
    int numQubits = circuit.getNumQubits();

    Json::Value operations(Json::arrayValue);
    Json::Value measurements(Json::arrayValue);

    for (const auto& operation : circuit.getOperations()) {
        std::string gate = operation.getGate();
        std::vector<double> params = operation.getParams();
        std::vector<int> qubits = operation.getQubits();

        if (gate == "measure") {
            for (int qubit : qubits) {
                measurements.append(qubit);
            }
        } else {
            Json::Value op;
            op["gate"] = gate;
            for (double param : params) {
                op["params"].append(param);
            }
            for (int qubit : qubits) {
                op["qubits"].append(qubit);
            }
            operations.append(op);
        }
    }

    std::cout << "Executing Quantum Circuit With...\n";
    std::cout << numQubits << " Qubits And ...\n";
    std::cout << operations.size() << " Gates\n";

    if (measurements.empty()) {
        throw std::runtime_error("There are no measurements done at the end of the circuit.");
    }

    Json::Value result;
    result["num_qubits"] = numQubits;
    result["operations"] = operations;
    result["measurements"] = measurements;
    result["topK"] = topK;

    return result;
}

// Post Request method
Json::Value AutomatskiKomencoNative::postRequest(const Json::Value& body) {
    CURL* curl;
    CURLcode res;
    std::string readBuffer;

    curl = curl_easy_init();
    if (curl) {
        std::string url = "http://" + host + ":" + std::to_string(port) + "/api/komenco";
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_POST, 1L);

        struct curl_slist* headers = NULL;
        headers = curl_slist_append(headers, "Content-Type: application/json");
        headers = curl_slist_append(headers, "Accept: application/json");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        std::string jsonData = body.toStyledString();
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, jsonData.c_str());

        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

        res = curl_easy_perform(curl);
        if (res != CURLE_OK) {
            curl_easy_cleanup(curl);
            throw std::runtime_error("Error making POST request");
        }

        curl_easy_cleanup(curl);
    }

    Json::Value jsonResponse;
    Json::CharReaderBuilder readerBuilder;
    std::string errs;
    std::istringstream s(readBuffer);
    std::string doc;
    s >> doc;
    std::istringstream ss(doc);
    if (!Json::parseFromStream(readerBuilder, ss, &jsonResponse, &errs)) {
        throw std::runtime_error("Failed to parse JSON response");
    }

    return jsonResponse;
}

// Deserialize Result method
std::unordered_map<std::string, int> AutomatskiKomencoNative::deserializeResult(const Json::Value& responseData, int repetitions) {
    const Json::Value& measurementsStrings = responseData["measurements"];

    std::unordered_map<std::string, int> measurements;
    for (const auto& key : measurementsStrings.getMemberNames()) {
        int count = std::round(measurementsStrings[key].asDouble() * repetitions);
        measurements[key] = count;
    }

    return measurements;
}

// Write Callback method
size_t AutomatskiKomencoNative::WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}