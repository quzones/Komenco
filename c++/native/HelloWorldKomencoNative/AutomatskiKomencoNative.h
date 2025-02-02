#ifndef AUTOMATSKI_KOMENCO_NATIVE_H
#define AUTOMATSKI_KOMENCO_NATIVE_H

#include <string>
#include <vector>
#include <unordered_map>
#include <jsoncpp/json/json.h>
#include "QuantumCircuit.h"

class AutomatskiKomencoNative {
private:
    std::string host;
    int port;

public:
    AutomatskiKomencoNative(const std::string& host, int port);

    std::unordered_map<std::string, int> run(QuantumCircuit& circuit, int repetitions, int topK);

private:
    Json::Value serializeCircuit(QuantumCircuit& circuit, int topK);
    Json::Value postRequest(const Json::Value& body);
    std::unordered_map<std::string, int> deserializeResult(const Json::Value& responseData, int repetitions);
    static size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp);
};

#endif // AUTOMATSKI_KOMENCO_NATIVE_H