# Define the Operation class
Operation <- setRefClass(
  "Operation",
  fields = list(
    gate = "character",
    qubits = "list",
    params = "list"
  ),
  methods = list(
    initialize = function(gate, qubits, params) {
      .self$gate <- gate
      .self$qubits <- qubits
      .self$params <- params
    },
    getGate = function() {
      return(.self$gate)
    },
    getQubits = function() {
      return(.self$qubits)
    },
    getParams = function() {
      return(.self$params)
    }
  )
)