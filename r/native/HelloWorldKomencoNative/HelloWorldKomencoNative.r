# Load necessary libraries
library(ggplot2)
library(jsonlite)

# Source the required files
source("Operation.r")
source("QuantumCircuit.r")
source("AutomatskiKomencoNative.r")

# Main function
main <- function() {
  # Create a sample quantum circuit to create a 3 Qubit GHZ State
  circuit <- QuantumCircuit$new(3)
  circuit$h(0)
  circuit$cx(0, 1)
  circuit$cx(0, 2)
  circuit$measureAll()

  # Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
  sampler <- AutomatskiKomencoNative$new("103.212.120.18", 80)

  # Run the circuit and get results
  results <- tryCatch({
    sampler$run(circuit, 1000, 20)
  }, error = function(e) {
    print(e)
    return(NULL)
  })

  if (is.null(results)) {
    return()
  }

  # Extract and count the measurement results
  measurements <- results
  print(measurements)

  labels <- names(measurements)
  values <- unlist(measurements)

  # Create a data frame for plotting
  data <- data.frame(
    Measurement = labels,
    Counts = values
  )

  # Plot the results using ggplot2
  p <- ggplot(data, aes(x = Measurement, y = Counts)) +
    geom_bar(stat = "identity") +
    ggtitle("Quantum States & Counts Histogram") +
    xlab("Measurement Outcomes") +
    ylab("Counts") +
    theme(axis.text.x = element_text(angle = 90, hjust = 1))

  print(p)
}

# Run the main function
main()