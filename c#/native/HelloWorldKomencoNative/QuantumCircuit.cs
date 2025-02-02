using System;
using System.Collections.Generic;
using System.Linq;

namespace Automatski.Komenco
{
    public class QuantumCircuit
    {
        private int numQubits;
        private List<Operation> operations;

        public QuantumCircuit(int numQubits)
        {
            this.numQubits = numQubits;
            this.operations = new List<Operation>();
        }

        public int GetNumQubits()
        {
            return numQubits;
        }

        public List<Operation> GetOperations()
        {
            return operations;
        }

        private void AddSingle(string gate, List<double> paramsList, List<int> qubits)
        {
            if (qubits.Count != 1)
            {
                throw new ArgumentException($"Number of qubits for gate {gate} has to be one");
            }
            foreach (int qubit in qubits)
            {
                if (qubit < 0 || qubit >= numQubits)
                {
                    throw new ArgumentException($"Invalid qubit: {qubit}");
                }
            }
            operations.Add(new Operation(gate, qubits, paramsList));
        }

        private void AddDouble(string gate, List<double> paramsList, List<int> qubits)
        {
            if (qubits.Count != 2)
            {
                throw new ArgumentException($"Number of qubits for gate {gate} has to be two");
            }
            foreach (int qubit in qubits)
            {
                if (qubit < 0 || qubit >= numQubits)
                {
                    throw new ArgumentException($"Invalid qubit: {qubit}");
                }
            }
            operations.Add(new Operation(gate, qubits, paramsList));
        }

        private void AddTriple(string gate, List<double> paramsList, List<int> qubits)
        {
            if (qubits.Count != 3)
            {
                throw new ArgumentException($"Number of qubits for gate {gate} has to be three");
            }
            foreach (int qubit in qubits)
            {
                if (qubit < 0 || qubit >= numQubits)
                {
                    throw new ArgumentException($"Invalid qubit: {qubit}");
                }
            }
            operations.Add(new Operation(gate, qubits, paramsList));
        }

        private void AddMultiple(string gate, List<double> paramsList, List<int> qubits)
        {
            int requiredQubits = (int)(Math.Log(gate.Length) / Math.Log(2));
            if (qubits.Count != requiredQubits)
            {
                throw new ArgumentException($"Number of qubits for gate {gate} has to be {requiredQubits}");
            }
            foreach (int qubit in qubits)
            {
                if (qubit < 0 || qubit >= numQubits)
                {
                    throw new ArgumentException($"Invalid qubit: {qubit}");
                }
            }
            operations.Add(new Operation(gate, qubits, paramsList));
        }

        public void Id(int qubit1)
        {
            AddSingle("id", new List<double>(), new List<int> { qubit1 });
        }

        public void X(int qubit1)
        {
            AddSingle("x", new List<double>(), new List<int> { qubit1 });
        }

        public void Y(int qubit1)
        {
            AddSingle("y", new List<double>(), new List<int> { qubit1 });
        }

        public void Z(int qubit1)
        {
            AddSingle("z", new List<double>(), new List<int> { qubit1 });
        }

        public void H(int qubit1)
        {
            AddSingle("h", new List<double>(), new List<int> { qubit1 });
        }

        public void S(int qubit1)
        {
            AddSingle("s", new List<double>(), new List<int> { qubit1 });
        }

        public void Sdg(int qubit1)
        {
            AddSingle("sdg", new List<double>(), new List<int> { qubit1 });
        }

        public void T(int qubit1)
        {
            AddSingle("t", new List<double>(), new List<int> { qubit1 });
        }

        public void Tdg(int qubit1)
        {
            AddSingle("tdg", new List<double>(), new List<int> { qubit1 });
        }

        public void Rx(double theta, int qubit1)
        {
            AddSingle("rx", new List<double> { theta }, new List<int> { qubit1 });
        }

        public void Ry(double theta, int qubit1)
        {
            AddSingle("ry", new List<double> { theta }, new List<int> { qubit1 });
        }

        public void Rz(double theta, int qubit1)
        {
            AddSingle("rz", new List<double> { theta }, new List<int> { qubit1 });
        }

        public void U(double theta, double phi, double lam, int qubit1)
        {
            AddSingle("u", new List<double> { theta, phi, lam }, new List<int> { qubit1 });
        }

        public void U1(double theta, int qubit1)
        {
            AddSingle("u1", new List<double> { theta }, new List<int> { qubit1 });
        }

        public void U2(double phi, double lam, int qubit1)
        {
            AddSingle("u2", new List<double> { phi, lam }, new List<int> { qubit1 });
        }

        public void U3(double theta, double phi, double lam, int qubit1)
        {
            AddSingle("u3", new List<double> { theta, phi, lam }, new List<int> { qubit1 });
        }

        public void Sx(int qubit1)
        {
            AddSingle("sx", new List<double>(), new List<int> { qubit1 });
        }

        public void Sxdg(int qubit1)
        {
            AddSingle("sxdg", new List<double>(), new List<int> { qubit1 });
        }

        public void R(double theta, double phi, int qubit1)
        {
            AddSingle("r", new List<double> { theta, phi }, new List<int> { qubit1 });
        }

        public void Cx(int qubit1, int qubit2)
        {
            AddDouble("cx", new List<double>(), new List<int> { qubit1, qubit2 });
        }

        public void Cy(int qubit1, int qubit2)
        {
            AddDouble("cy", new List<double>(), new List<int> { qubit1, qubit2 });
        }

        public void Cz(int qubit1, int qubit2)
        {
            AddDouble("cz", new List<double>(), new List<int> { qubit1, qubit2 });
        }

        public void Ch(int qubit1, int qubit2)
        {
            AddDouble("ch", new List<double>(), new List<int> { qubit1, qubit2 });
        }

        public void Ucrx(double theta, int qubit1, int qubit2)
        {
            AddDouble("ucrx", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Ucry(double theta, int qubit1, int qubit2)
        {
            AddDouble("ucry", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Ucrz(double theta, int qubit1, int qubit2)
        {
            AddDouble("ucrz", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Crx(double theta, int qubit1, int qubit2)
        {
            AddDouble("crx", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Cry(double theta, int qubit1, int qubit2)
        {
            AddDouble("cry", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Crz(double theta, int qubit1, int qubit2)
        {
            AddDouble("crz", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Cr(double theta, double phi, double lam, int qubit1, int qubit2)
        {
            AddDouble("cr", new List<double> { theta, phi, lam }, new List<int> { qubit1, qubit2 });
        }

        public void Cu(double theta, double phi, double lam, double gamma, int qubit1, int qubit2)
        {
            AddDouble("cu1", new List<double> { theta, phi, lam, gamma }, new List<int> { qubit1, qubit2 });
        }

        public void Cu1(double theta, int qubit1, int qubit2)
        {
            AddDouble("cu1", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Cu2(double phi, double lam, int qubit1, int qubit2)
        {
            AddDouble("cu2", new List<double> { phi, lam }, new List<int> { qubit1, qubit2 });
        }

        public void Cu3(double theta, double phi, double lam, int qubit1, int qubit2)
        {
            AddDouble("cu3", new List<double> { theta, phi, lam }, new List<int> { qubit1, qubit2 });
        }

        public void Dcx(int qubit1, int qubit2)
        {
            AddDouble("dcx", new List<double>(), new List<int> { qubit1, qubit2 });
        }

        public void Ecr(int qubit1, int qubit2)
        {
            AddDouble("ecr", new List<double>(), new List<int> { qubit1, qubit2 });
        }
    
        public void Iswap(int qubit1, int qubit2)
        {
            AddDouble("iswap", new List<double>(), new List<int> { qubit1, qubit2 });
        }

        public void Rxx(double theta, int qubit1, int qubit2)
        {
            AddDouble("rxx", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Ryy(double theta, int qubit1, int qubit2)
        {
            AddDouble("ryy", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Rzz(double theta, int qubit1, int qubit2)
        {
            AddDouble("rzz", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Rzx(double theta, int qubit1, int qubit2)
        {
            AddDouble("rzx", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Cswap(int qubit1, int qubit2, int qubit3)
        {
            AddTriple("cswap", new List<double>(), new List<int> { qubit1, qubit2, qubit3 });
        }

        public void Ccx(int qubit1, int qubit2, int qubit3)
        {
            AddTriple("ccx", new List<double>(), new List<int> { qubit1, qubit2, qubit3 });
        }

        public void Ccy(int qubit1, int qubit2, int qubit3)
        {
            AddTriple("ccy", new List<double>(), new List<int> { qubit1, qubit2, qubit3 });
        }

        public void Ccz(int qubit1, int qubit2, int qubit3)
        {
            AddTriple("ccz", new List<double>(), new List<int> { qubit1, qubit2, qubit3 });
        }

        public void C3x(List<int> qubits)
        {
            AddMultiple("c3x", new List<double>(), qubits);
        }

        public void C4x(List<int> qubits)
        {
            AddMultiple("c4x", new List<double>(), qubits);
        }

        public void Mcx(List<int> qubits)
        {
            AddMultiple("mcx", new List<double>(), qubits);
        }

        public void Mcu1(double theta, List<int> qubits)
        {
            AddMultiple("mcu1", new List<double> { theta }, qubits);
        }

        public void Mcu2(double phi, double lam, List<int> qubits)
        {
            AddMultiple("mcu2", new List<double> { phi, lam }, qubits);
        }

        public void Mcu3(double theta, double phi, double lam, List<int> qubits)
        {
            AddMultiple("mcu3", new List<double> { theta, phi, lam }, qubits);
        }

        public void Mcz(List<int> qubits)
        {
            AddMultiple("mcz", new List<double>(), qubits);
        }

        public void Mcp(List<int> qubits)
        {
            AddMultiple("mcp", new List<double>(), qubits);
        }

        public void Mcrx(List<int> qubits)
        {
            AddMultiple("mcrx", new List<double>(), qubits);
        }

        public void Mcry(List<int> qubits)
        {
            AddMultiple("mcry", new List<double>(), qubits);
        }

        public void Mcrz(List<int> qubits)
        {
            AddMultiple("mcrz", new List<double>(), qubits);
        }

        public void Qft(List<int> qubits)
        {
            AddMultiple("qft", new List<double>(), qubits);
        }
    
        public void InverseQft(List<int> qubits)
        {
            AddMultiple("iqft", new List<double>(), qubits);
        }

        public void Swap(int qubit1, int qubit2)
        {
            AddDouble("swap", new List<double>(), new List<int> { qubit1, qubit2 });
        }

        public void Csx(int qubit1, int qubit2)
        {
            AddDouble("csx", new List<double>(), new List<int> { qubit1, qubit2 });
        }

        public void P(double theta, int qubit1)
        {
            AddSingle("p", new List<double> { theta }, new List<int> { qubit1 });
        }

        public void Cp(double theta, int qubit1, int qubit2)
        {
            AddDouble("cp", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Ccp(double theta, int qubit1, int qubit2, int qubit3)
        {
            AddTriple("ccp", new List<double> { theta }, new List<int> { qubit1, qubit2, qubit3 });
        }

        public void SqrtX(int qubit1)
        {
            AddSingle("sqrt_x", new List<double>(), new List<int> { qubit1 });
        }

        public void SqrtY(int qubit1)
        {
            AddSingle("sqrt_y", new List<double>(), new List<int> { qubit1 });
        }

        public void SqrtZ(int qubit1)
        {
            AddSingle("sqrt_z", new List<double>(), new List<int> { qubit1 });
        }

        public void Gpi(double phi, int qubit1)
        {
            AddSingle("gpi", new List<double> { phi }, new List<int> { qubit1 });
        }

        public void Gpi2(double phi, int qubit1)
        {
            AddSingle("gpi2", new List<double> { phi }, new List<int> { qubit1 });
        }

        public void Xp(double theta, int qubit1)
        {
            AddSingle("xp", new List<double> { theta }, new List<int> { qubit1 });
        }

        public void Yp(double theta, int qubit1)
        {
            AddSingle("yp", new List<double> { theta }, new List<int> { qubit1 });
        }

        public void Zp(double theta, int qubit1)
        {
            AddSingle("zp", new List<double> { theta }, new List<int> { qubit1 });
        }

        public void Xxp(double theta, int qubit1, int qubit2)
        {
            AddDouble("xxp", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Yyp(double theta, int qubit1, int qubit2)
        {
            AddDouble("yyp", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Zzp(double theta, int qubit1, int qubit2)
        {
            AddDouble("zzp", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void PhasedXp(double theta, double phi, int qubit1)
        {
            AddSingle("phased_xp", new List<double> { theta, phi }, new List<int> { qubit1 });
        }

        public void PhasedYp(double theta, double phi, int qubit1)
        {
            AddSingle("phased_yp", new List<double> { theta, phi }, new List<int> { qubit1 });
        }

        public void PhasedZp(double theta, double phi, int qubit1)
        {
            AddSingle("phased_zp", new List<double> { theta, phi }, new List<int> { qubit1 });
        }

        public void Cnotp(double theta, int qubit1, int qubit2)
        {
            AddDouble("cnotp", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Ccnotp(double theta, int qubit1, int qubit2, int qubit3)
        {
            AddTriple("ccnotp", new List<double> { theta }, new List<int> { qubit1, qubit2, qubit3 });
        }

        public void Cyp(double theta, int qubit1, int qubit2)
        {
            AddDouble("cyp", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Ccyp(double theta, int qubit1, int qubit2, int qubit3)
        {
            AddTriple("ccyp", new List<double> { theta }, new List<int> { qubit1, qubit2, qubit3 });
        }

        public void Czp(double theta, int qubit1, int qubit2)
        {
            AddDouble("czp", new List<double> { theta }, new List<int> { qubit1, qubit2 });
        }

        public void Cczp(double theta, int qubit1, int qubit2, int qubit3)
        {
            AddTriple("cczp", new List<double> { theta }, new List<int> { qubit1, qubit2, qubit3 });
        }

        public void Measure(List<int> qubits)
        {
            List<double> cparams = new List<double>();
            List<int> cqubits = new List<int>();
            string cgate = "measure";
            if (qubits.Count == 0)
            {
                throw new ArgumentException("number of qubits to measure cannot be zero");
            }
            else
            {
                foreach (int qubit in qubits)
                {
                    if (qubit < 0 || qubit >= this.numQubits)
                    {
                        throw new ArgumentException("invalid qubit: " + qubit);
                    }
                    else
                    {
                        cqubits.Add(qubit);
                    }
                }
            }
            operations.Add(new Operation(cgate, cqubits, cparams));
        }

        public void MeasureAll()
        {
            List<double> cparams = new List<double>();
            List<int> cqubits = new List<int>();
            string cgate = "measure";
            for (int qubit = 0; qubit < this.numQubits; qubit++)
            {
                cqubits.Add(qubit);
            }
            operations.Add(new Operation(cgate, cqubits, cparams));
        }

        public void RandomCircuit(int numberOfOperations, List<int> qubitsToUseForRandomCircuit)
        {
            int qubitsCount = qubitsToUseForRandomCircuit.Count;
            if (qubitsCount < 3)
            {
                throw new ArgumentException("The number of qubits needed to generate random circuits is >= 3");
            }

            Dictionary<string, int> gatesAndQubitsMap = new Dictionary<string, int>
            {
                // 1 qubit gates
                { "x", 1 },
                { "y", 1 },
                { "z", 1 },
                { "rx", 1 },
                { "ry", 1 },
                { "rz", 1 },
                { "h", 1 },
                { "s", 1 },
                { "sdg", 1 },
                { "t", 1 },
                { "tdg", 1 },
                { "sx", 1 },
                { "sxdg", 1 },
                // 2 qubit gates
                { "cx", 2 },
                { "cy", 2 },
                { "cz", 2 },
                { "crx", 2 },
                { "cry", 2 },
                { "crz", 2 },
                { "ch", 2 },
                { "dcx", 2 },
                { "ecr", 2 },
                { "iswap", 2 },
                { "swap", 2 },
                { "csx", 2 },
                // 3 qubit gates
                { "cswap", 3 },
                { "ccx", 3 }
            };

            List<string> allPossibleGates = gatesAndQubitsMap.Keys.ToList();
            int allPossibleGatesCount = allPossibleGates.Count;

            Random random = new Random();
            for (int i = 0; i < numberOfOperations; i++)
            {
                int index = random.Next(allPossibleGatesCount);
                string cgate = allPossibleGates[index];

                int numberOfQubits = gatesAndQubitsMap[cgate];

                qubitsToUseForRandomCircuit = qubitsToUseForRandomCircuit.OrderBy(x => random.Next()).ToList();
                List<int> cqubits = new List<int>();
                for (int j = 0; j < numberOfQubits; j++)
                {
                    cqubits.Add(qubitsToUseForRandomCircuit[j]);
                }

                List<double> cparams = new List<double>();
                if (new List<string> { "rx", "ry", "rz", "crx", "cry", "crz" }.Contains(cgate))
                {
                    double theta = random.NextDouble() * 2 * Math.PI;
                    cparams.Add(theta);
                }

                operations.Add(new Operation(cgate, cqubits, cparams));
            }
        }
    
    }
}