library(httr)
library(jsonlite)

AutomatskiKomencoNative <- setRefClass(
  "AutomatskiKomencoNative",
  fields = list(
    host = "character",
    port = "numeric"
  ),
  methods = list(
    initialize = function(host, port) {
      .self$host <- host
      .self$port <- port
    },
    run = function(circuit, repetitions, topK) {
      tstart <- Sys.time()
      
      body <- .self$serializeCircuit(circuit, topK)
      struct <- .self$postRequest(body)
      
      tend <- Sys.time()
      executionTime <- as.numeric(difftime(tend, tstart, units = "secs")) * 1000
      cat("Time Taken", executionTime, "ms\n")
      
      if (!is.null(struct$error)) {
        cat(struct$error, "\n")
        stop(struct$error)
      }
      
      return(.self$deserializeResult(struct, repetitions))
    },
    serializeCircuit = function(circuit, topK) {
      numQubits <- circuit$getNumQubits()
      
      operations <- list()
      measurements <- list()
      
      for (operation in circuit$getOperations()) {
        gate <- operation$getGate()
        params <- operation$getParams()
        qubits <- operation$getQubits()
        
        if (gate == "measure") {
          measurements <- c(measurements, qubits)
        } else {
          op <- list(
            gate = gate,
            params = params,
            qubits = qubits
          )
          operations <- c(operations, list(op))
        }
      }
      
      cat("Executing Quantum Circuit With...\n")
      cat(numQubits, "Qubits And ...\n")
      cat(length(operations), "Gates\n")
      
      if (length(measurements) == 0) {
        stop("There are no measurements done at the end of the circuit.")
      }
      
      json <- list(
        num_qubits = numQubits,
        operations = operations,
        measurements = measurements,
        topK = topK
      )
      
      return(toJSON(json, auto_unbox = TRUE))
    },
    postRequest = function(body) {
      url <- paste0("http://", .self$host, ":", .self$port, "/api/komenco")
      response <- POST(url, body = body, encode = "json", content_type_json())
      
      if (http_error(response)) {
        stop("Error making POST request")
      }
      
      return(fromJSON(content(response, "text", encoding = "UTF-8")))
    },
    deserializeResult = function(responseData, repetitions) {
      measurementsStrings <- responseData$measurements
      
      measurements <- list()
      for (key in names(measurementsStrings)) {
        count <- round(measurementsStrings[[key]] * repetitions)
        measurements[[key]] <- count
      }
      
      return(measurements)
    }
  )
)