import qiskit.qasm3
import numpy as np
from qiskit import QuantumCircuit
from matplotlib import pyplot as plt
import sys
sys.path.append('../')
from AutomatskiKomencoQiskit import *

'''
//https://docs.quantum.ibm.com/guides/interoperate-qiskit-qasm3
import qiskit.qasm3

qiskit.qasm3.load(file_name)
qiskit.qasm3.loads(program-string)
'''
 
program = """
    OPENQASM 3.0;
    include "stdgates.inc";
 
    input float[64] a;
    qubit[3] q;
    bit[2] mid;
    bit[3] out;
 
    let aliased = q[0:1];
 
    gate my_gate(a) c, t {
      gphase(a / 2);
      ry(a) c;
      cx c, t;
    }
    gate my_phase(a) c {
      ctrl @ inv @ gphase(a) c;
    }
 
    my_gate(a * 2) aliased[0], q[{1, 2}][0];
    measure q[0] -> mid[0];
    measure q[1] -> mid[1];
 
    while (mid == "00") {
      reset q[0];
      reset q[1];
      my_gate(a) q[0], q[1];
      my_phase(a - pi/2) q[1];
      mid[0] = measure q[0];
      mid[1] = measure q[1];
    }
 
    if (mid[0]) {
      let inner_alias = q[{0, 1}];
      reset inner_alias;
    }
 
    out = measure q;
"""
circuit = qiskit.qasm3.loads(program)
circuit.draw("mpl")

# saving the circuit diagram.
# Make sure you use savefig() before show(). 
plt.savefig("qasm3-circuit.png") 

plt.show()
