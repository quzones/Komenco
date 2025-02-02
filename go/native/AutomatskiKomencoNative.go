package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
    "time"
)

type AutomatskiKomencoNative struct {
    host string
    port int
}

func NewAutomatskiKomencoNative(host string, port int) *AutomatskiKomencoNative {
    return &AutomatskiKomencoNative{
        host: host,
        port: port,
    }
}

func (akn *AutomatskiKomencoNative) Run(circuit *QuantumCircuit, repetitions, topK int) (map[string]int, error) {
    tstart := time.Now()

    body, err := akn.serializeCircuit(circuit, topK)
    if err != nil {
        return nil, err
    }

    structData, err := akn.postRequest(body)
    if err != nil {
        return nil, err
    }

    tend := time.Now()
    executionTime := tend.Sub(tstart)
    fmt.Println("Time Taken", executionTime.Milliseconds(), "ms")

    if errorMsg, exists := structData["error"]; exists {
        fmt.Println(errorMsg)
        return nil, fmt.Errorf("%v", errorMsg)
    }

    return akn.deserializeResult(structData, repetitions), nil
}

func (akn *AutomatskiKomencoNative) serializeCircuit(circuit *QuantumCircuit, topK int) ([]byte, error) {
    numQubits := circuit.GetNumQubits()

    var operations []map[string]interface{}
    var measurements []int

    for _, operation := range circuit.GetOperations() {
        gate := operation.gate
        params := operation.params
        qubits := operation.qubits

        if gate == "measure" {
            measurements = append(measurements, qubits...)
        } else {
            op := map[string]interface{}{
                "gate":   gate,
                "params": params,
                "qubits": qubits,
            }
            operations = append(operations, op)
        }
    }

    fmt.Println("Executing Quantum Circuit With...")
    fmt.Println(numQubits, "Qubits And ...")
    fmt.Println(len(operations), "Gates")

    if len(measurements) == 0 {
        return nil, fmt.Errorf("there are no measurements done at the end of the circuit")
    }

    jsonData := map[string]interface{}{
        "num_qubits":  numQubits,
        "operations":  operations,
        "measurements": measurements,
        "topK":        topK,
    }

    return json.Marshal(jsonData)
}

func (akn *AutomatskiKomencoNative) postRequest(body []byte) (map[string]interface{}, error) {
    url := fmt.Sprintf("http://%s:%d/api/komenco", akn.host, akn.port)
    resp, err := http.Post(url, "application/json", bytes.NewBuffer(body))
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()

    responseData, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        return nil, err
    }

    var structData map[string]interface{}
    if err := json.Unmarshal(responseData, &structData); err != nil {
        return nil, err
    }

    return structData, nil
}

func (akn *AutomatskiKomencoNative) deserializeResult(responseData map[string]interface{}, repetitions int) map[string]int {
    measurementsStrings := responseData["measurements"].(map[string]interface{})

    measurements := make(map[string]int)
    for key, value := range measurementsStrings {
        count := int(value.(float64) * float64(repetitions))
        measurements[key] = count
    }

    return measurements
}


type Operation struct {
	gate   string
	qubits []int
	params []float64
}
	
func NewOperation(gate string, qubits []int, params []float64) *Operation {
	return &Operation{
		gate:   gate,
		qubits: qubits,
		params: params,
	}
}
	
func (op *Operation) GetGate() string {
	return op.gate
}
	
func (op *Operation) GetQubits() []int {
	return op.qubits
}
	
func (op *Operation) GetParams() []float64 {
	return op.params
}	