using System.Collections.Generic;

namespace Automatski.Komenco
{
    public class Operation
    {
        public string Gate { get; }
        public List<int> Qubits { get; }
        public List<double> Params { get; }

        public Operation(string gate, List<int> qubits, List<double> parameters)
        {
            this.Gate = gate;
            this.Qubits = qubits;
            this.Params = parameters;
        }

        public string GetGate()
        {
            return Gate;
        }

        public List<int> GetQubits()
        {
            return Qubits;
        }

        public List<double> GetParams()
        {
            return Params;
        }
    }
}