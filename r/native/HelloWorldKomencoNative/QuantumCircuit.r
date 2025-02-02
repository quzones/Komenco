# Define the QuantumCircuit class
QuantumCircuit <- setRefClass(
  "QuantumCircuit",
  fields = list(
    numQubits = "numeric",
    operations = "list"
  ),
  methods = list(
    initialize = function(numQubits) {
      .self$numQubits <- numQubits
      .self$operations <- list()
    },
    getNumQubits = function() {
      return(.self$numQubits)
    },
    getOperations = function() {
      return(.self$operations)
    },
    addSingle = function(gate, params, qubits) {
      if (length(qubits) != 1) {
        stop(paste("Number of qubits for gate", gate, "has to be one"))
      }
      for (qubit in qubits) {
        if (qubit < 0 || qubit >= .self$numQubits) {
          stop(paste("Invalid qubit:", qubit))
        }
      }
      .self$operations <- c(.self$operations, list(Operation$new(gate, qubits, params)))
    },
    addDouble = function(gate, params, qubits) {
      if (length(qubits) != 2) {
        stop(paste("Number of qubits for gate", gate, "has to be two"))
      }
      for (qubit in qubits) {
        if (qubit < 0 || qubit >= .self$numQubits) {
          stop(paste("Invalid qubit:", qubit))
        }
      }
      .self$operations <- c(.self$operations, list(Operation$new(gate, qubits, params)))
    },
    addTriple = function(gate, params, qubits) {
      if (length(qubits) != 3) {
        stop(paste("Number of qubits for gate", gate, "has to be three"))
      }
      for (qubit in qubits) {
        if (qubit < 0 || qubit >= .self$numQubits) {
          stop(paste("Invalid qubit:", qubit))
        }
      }
      .self$operations <- c(.self$operations, list(Operation$new(gate, qubits, params)))
    },
    addMultiple = function(gate, params, qubits) {
      requiredQubits <- as.integer(log(length(gate)) / log(2))
      if (length(qubits) != requiredQubits) {
        stop(paste("Number of qubits for gate", gate, "has to be", requiredQubits))
      }
      for (qubit in qubits) {
        if (qubit < 0 || qubit >= .self$numQubits) {
          stop(paste("Invalid qubit:", qubit))
        }
      }
      .self$operations <- c(.self$operations, list(Operation$new(gate, qubits, params)))
    },
    id = function(qubit1) {
      .self$addSingle("id", list(), list(qubit1))
    },
    x = function(qubit1) {
      .self$addSingle("x", list(), list(qubit1))
    },
    y = function(qubit1) {
      .self$addSingle("y", list(), list(qubit1))
    },
    z = function(qubit1) {
      .self$addSingle("z", list(), list(qubit1))
    },
    h = function(qubit1) {
      .self$addSingle("h", list(), list(qubit1))
    },
    s = function(qubit1) {
      .self$addSingle("s", list(), list(qubit1))
    },
    sdg = function(qubit1) {
      .self$addSingle("sdg", list(), list(qubit1))
    },
    t = function(qubit1) {
      .self$addSingle("t", list(), list(qubit1))
    },
    tdg = function(qubit1) {
      .self$addSingle("tdg", list(), list(qubit1))
    },
    rx = function(theta, qubit1) {
      .self$addSingle("rx", list(theta), list(qubit1))
    },
    ry = function(theta, qubit1) {
      .self$addSingle("ry", list(theta), list(qubit1))
    },
    rz = function(theta, qubit1) {
      .self$addSingle("rz", list(theta), list(qubit1))
    },
    u = function(theta, phi, lam, qubit1) {
      .self$addSingle("u", list(theta, phi, lam), list(qubit1))
    },
    u1 = function(theta, qubit1) {
      .self$addSingle("u1", list(theta), list(qubit1))
    },
    u2 = function(phi, lam, qubit1) {
      .self$addSingle("u2", list(phi, lam), list(qubit1))
    },
    u3 = function(theta, phi, lam, qubit1) {
      .self$addSingle("u3", list(theta, phi, lam), list(qubit1))
    },
    sx = function(qubit1) {
      .self$addSingle("sx", list(), list(qubit1))
    },
    sxdg = function(qubit1) {
      .self$addSingle("sxdg", list(), list(qubit1))
    },
    r = function(theta, phi, qubit1) {
      .self$addSingle("r", list(theta, phi), list(qubit1))
    },
    cx = function(qubit1, qubit2) {
      .self$addDouble("cx", list(), list(qubit1, qubit2))
    },
    cy = function(qubit1, qubit2) {
      .self$addDouble("cy", list(), list(qubit1, qubit2))
    },
    cz = function(qubit1, qubit2) {
      .self$addDouble("cz", list(), list(qubit1, qubit2))
    },
    ch = function(qubit1, qubit2) {
      .self$addDouble("ch", list(), list(qubit1, qubit2))
    },
    ucrx = function(theta, qubit1, qubit2) {
      .self$addDouble("ucrx", list(theta), list(qubit1, qubit2))
    },
    ucry = function(theta, qubit1, qubit2) {
      .self$addDouble("ucry", list(theta), list(qubit1, qubit2))
    },
    ucrz = function(theta, qubit1, qubit2) {
      .self$addDouble("ucrz", list(theta), list(qubit1, qubit2))
    },
    crx = function(theta, qubit1, qubit2) {
      .self$addDouble("crx", list(theta), list(qubit1, qubit2))
    },
    cry = function(theta, qubit1, qubit2) {
      .self$addDouble("cry", list(theta), list(qubit1, qubit2))
    },
    crz = function(theta, qubit1, qubit2) {
      .self$addDouble("crz", list(theta), list(qubit1, qubit2))
    },
    cr = function(theta, phi, lam, qubit1, qubit2) {
      .self$addDouble("cr", list(theta, phi, lam), list(qubit1, qubit2))
    },
    cu = function(theta, phi, lam, gamma, qubit1, qubit2) {
      .self$addDouble("cu1", list(theta, phi, lam, gamma), list(qubit1, qubit2))
    },
    cu1 = function(theta, qubit1, qubit2) {
      .self$addDouble("cu1", list(theta), list(qubit1, qubit2))
    },
    cu2 = function(phi, lam, qubit1, qubit2) {
      .self$addDouble("cu2", list(phi, lam), list(qubit1, qubit2))
    },
    cu3 = function(theta, phi, lam, qubit1, qubit2) {
      .self$addDouble("cu3", list(theta, phi, lam), list(qubit1, qubit2))
    },
    dcx = function(qubit1, qubit2) {
      .self$addDouble("dcx", list(), list(qubit1, qubit2))
    },
    ecr = function(qubit1, qubit2) {
      .self$addDouble("ecr", list(), list(qubit1, qubit2))
    },
    iswap = function(qubit1, qubit2) {
      .self$addDouble("iswap", list(), list(qubit1, qubit2))
    },
    rxx = function(theta, qubit1, qubit2) {
      .self$addDouble("rxx", list(theta), list(qubit1, qubit2))
    },
    ryy = function(theta, qubit1, qubit2) {
      .self$addDouble("ryy", list(theta), list(qubit1, qubit2))
    },
    rzz = function(theta, qubit1, qubit2) {
      .self$addDouble("rzz", list(theta), list(qubit1, qubit2))
    },
    rzx = function(theta, qubit1, qubit2) {
      .self$addDouble("rzx", list(theta), list(qubit1, qubit2))
    },
    cswap = function(qubit1, qubit2, qubit3) {
      .self$addTriple("cswap", list(), list(qubit1, qubit2, qubit3))
    },
    ccx = function(qubit1, qubit2, qubit3) {
      .self$addTriple("ccx", list(), list(qubit1, qubit2, qubit3))
    },
    ccy = function(qubit1, qubit2, qubit3) {
      .self$addTriple("ccy", list(), list(qubit1, qubit2, qubit3))
    },
    ccz = function(qubit1, qubit2, qubit3) {
      .self$addTriple("ccz", list(), list(qubit1, qubit2, qubit3))
    },
    c3x = function(qubits) {
      .self$addMultiple("c3x", list(), qubits)
    },
    c4x = function(qubits) {
      .self$addMultiple("c4x", list(), qubits)
    },
    mcx = function(qubits) {
      .self$addMultiple("mcx", list(), qubits)
    },
    mcu1 = function(theta, qubits) {
      .self$addMultiple("mcu1", list(theta), qubits)
    },
    mcu2 = function(phi, lam, qubits) {
      .self$addMultiple("mcu2", list(phi, lam), qubits)
    },
    mcu3 = function(theta, phi, lam, qubits) {
      .self$addMultiple("mcu3", list(theta, phi, lam), qubits)
    },
    mcz = function(qubits) {
      .self$addMultiple("mcz", list(), qubits)
    },
    mcp = function(qubits) {
      .self$addMultiple("mcp", list(), qubits)
    },
    mcrx = function(qubits) {
      .self$addMultiple("mcrx", list(), qubits)
    },
    mcry = function(qubits) {
      .self$addMultiple("mcry", list(), qubits)
    },
    mcrz = function(qubits) {
      .self$addMultiple("mcrz", list(), qubits)
    },
    qft = function(qubits) {
      .self$addMultiple("qft", list(), qubits)
    },
    inverse_qft = function(qubits) {
      .self$addMultiple("iqft", list(), qubits)
    },
    swap = function(qubit1, qubit2) {
      .self$addDouble("swap", list(), list(qubit1, qubit2))
    },
    csx = function(qubit1, qubit2) {
      .self$addDouble("csx", list(), list(qubit1, qubit2))
    },
    p = function(theta, qubit1) {
      .self$addSingle("p", list(theta), list(qubit1))
    },
    cp = function(theta, qubit1, qubit2) {
      .self$addDouble("cp", list(theta), list(qubit1, qubit2))
    },
    ccp = function(theta, qubit1, qubit2, qubit3) {
      .self$addTriple("ccp", list(theta), list(qubit1, qubit2, qubit3))
    },
    sqrt_x = function(qubit1) {
      .self$addSingle("sqrt_x", list(), list(qubit1))
    },
    sqrt_y = function(qubit1) {
      .self$addSingle("sqrt_y", list(), list(qubit1))
    },
    sqrt_z = function(qubit1) {
      .self$addSingle("sqrt_z", list(), list(qubit1))
    },
    gpi = function(phi, qubit1) {
      .self$addSingle("gpi", list(phi), list(qubit1))
    },
    gpi2 = function(phi, qubit1) {
      .self$addSingle("gpi2", list(phi), list(qubit1))
    },
    xp = function(theta, qubit1) {
      .self$addSingle("xp", list(theta), list(qubit1))
    },
    yp = function(theta, qubit1) {
      .self$addSingle("yp", list(theta), list(qubit1))
    },
    zp = function(theta, qubit1) {
      .self$addSingle("zp", list(theta), list(qubit1))
    },
    xxp = function(theta, qubit1, qubit2) {
      .self$addDouble("xxp", list(theta), list(qubit1, qubit2))
    },
    yyp = function(theta, qubit1, qubit2) {
      .self$addDouble("yyp", list(theta), list(qubit1, qubit2))
    },
    zzp = function(theta, qubit1, qubit2) {
      .self$addDouble("zzp", list(theta), list(qubit1, qubit2))
    },
    phased_xp = function(theta, phi, qubit1) {
      .self$addSingle("phased_xp", list(theta, phi), list(qubit1))
    },
    phased_yp = function(theta, phi, qubit1) {
      .self$addSingle("phased_yp", list(theta, phi), list(qubit1))
    },
    phased_zp = function(theta, phi, qubit1) {
      .self$addSingle("phased_zp", list(theta, phi), list(qubit1))
    },
    cnotp = function(theta, qubit1, qubit2) {
      .self$addDouble("cnotp", list(theta), list(qubit1, qubit2))
    },
    ccnotp = function(theta, qubit1, qubit2, qubit3) {
      .self$addTriple("ccnotp", list(theta), list(qubit1, qubit2, qubit3))
    },
    cyp = function(theta, qubit1, qubit2) {
      .self$addDouble("cyp", list(theta), list(qubit1, qubit2))
    },
    ccyp = function(theta, qubit1, qubit2, qubit3) {
      .self$addTriple("ccyp", list(theta), list(qubit1, qubit2, qubit3))
    },
    czp = function(theta, qubit1, qubit2) {
      .self$addDouble("czp", list(theta), list(qubit1, qubit2))
    },
    cczp = function(theta, qubit1, qubit2, qubit3) {
      .self$addTriple("cczp", list(theta), list(qubit1, qubit2, qubit3))
    },
    measure = function(qubits) {
      cparams <- list()
      cqubits <- list()
      cgate <- "measure"
      if (length(qubits) == 0) {
        stop("number of qubits to measure cannot be zero")
      } else {
        for (qubit in qubits) {
          if (qubit < 0 || qubit >= .self$numQubits) {
            stop(paste("invalid qubit:", qubit))
          } else {
            cqubits <- c(cqubits, qubit)
          }
        }
      }
      .self$operations <- c(.self$operations, Operation$new(cgate, cqubits, cparams))
    },
    measureAll = function() {
      cparams <- list()
      cqubits <- list()
      cgate <- "measure"
      for (qubit in 0:(.self$numQubits - 1)) {
        cqubits <- c(cqubits, qubit)
      }
      .self$operations <- c(.self$operations, Operation$new(cgate, cqubits, cparams))
    },
    randomCircuit = function(numberOfOperations, qubitsToUseForRandomCircuit) {
      qubitsCount <- length(qubitsToUseForRandomCircuit)
      if (qubitsCount < 3) {
        stop("The number of qubits needed to generate random circuits is >= 3")
      }

      gatesAndQubitsMap <- list(
        # 1 qubit gates
        x = 1, y = 1, z = 1, rx = 1, ry = 1, rz = 1,
        h = 1, s = 1, sdg = 1, t = 1, tdg = 1, sx = 1, sxdg = 1,
        # 2 qubit gates
        cx = 2, cy = 2, cz = 2, crx = 2, cry = 2, crz = 2,
        ch = 2, dcx = 2, ecr = 2, iswap = 2, swap = 2, csx = 2,
        # 3 qubit gates
        cswap = 3, ccx = 3
      )

      allPossibleGates <- names(gatesAndQubitsMap)
      allPossibleGatesCount <- length(allPossibleGates)

      operations <<- list()
      for (i in 1:numberOfOperations) {
        index <- sample(1:allPossibleGatesCount, 1)
        cgate <- allPossibleGates[index]

        numberOfQubits <- gatesAndQubitsMap[[cgate]]

        qubitsToUseForRandomCircuit <- sample(qubitsToUseForRandomCircuit)
        cqubits <- qubitsToUseForRandomCircuit[1:numberOfQubits]

        cparams <- list()
        if (cgate %in% c("rx", "ry", "rz", "crx", "cry", "crz")) {
          theta <- runif(1, 0, 2 * pi)
          cparams <- c(cparams, theta)
        }

        .self$operations <- c(.self$operations, Operation$new(cgate, cqubits, cparams))
      }
    }
  )
)