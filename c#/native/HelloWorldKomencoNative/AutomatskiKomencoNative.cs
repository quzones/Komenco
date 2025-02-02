using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Text;
using Newtonsoft.Json.Linq;

namespace Automatski.Komenco
{
    public class AutomatskiKomencoNative
    {
        private string host;
        private int port;

        public AutomatskiKomencoNative(string host, int port)
        {
            this.host = host;
            this.port = port;
        }

        public Dictionary<string, int> Run(QuantumCircuit circuit, int repetitions, int topK)
        {
            long tstart = DateTimeOffset.Now.ToUnixTimeMilliseconds();

            JObject body = SerializeCircuit(circuit, topK);
            JObject structData = PostRequest(body);

            long tend = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            long executionTime = tend - tstart;
            Console.WriteLine("Time Taken " + executionTime + "ms");

            if (structData.ContainsKey("error"))
            {
                Console.WriteLine(structData["error"].ToString());
                throw new Exception(structData["error"].ToString());
            }

            return DeserializeResult(structData, repetitions);
        }

        private JObject SerializeCircuit(QuantumCircuit circuit, int topK)
        {
            int numQubits = circuit.GetNumQubits();

            var operations = new List<Dictionary<string, object>>();
            var measurements = new List<int>();

            foreach (var operation in circuit.GetOperations())
            {
                string gate = operation.GetGate();
                var paramsList = operation.GetParams();
                var qubits = operation.GetQubits();

                if (gate == "measure")
                {
                    measurements.AddRange(qubits);
                }
                else
                {
                    var op = new Dictionary<string, object>
                    {
                        { "gate", gate },
                        { "params", paramsList },
                        { "qubits", qubits }
                    };
                    operations.Add(op);
                }
            }

            Console.WriteLine("Executing Quantum Circuit With...");
            Console.WriteLine(numQubits + " Qubits And ...");
            Console.WriteLine(operations.Count + " Gates");

            if (measurements.Count == 0)
            {
                throw new Exception("There are no measurements done at the end of the circuit.");
            }

            var json = new JObject
            {
                { "num_qubits", numQubits },
                { "operations", JToken.FromObject(operations) },
                { "measurements", JToken.FromObject(measurements) },
                { "topK", topK }
            };

            return json;
        }

        private JObject PostRequest(JObject body)
        {
            var url = $"http://{host}:{port}/api/komenco";
            var request = (HttpWebRequest)WebRequest.Create(url);
            request.Method = "POST";
            request.ContentType = "application/json; utf-8";
            request.Accept = "application/json";

            var input = Encoding.UTF8.GetBytes(body.ToString());
            using (var stream = request.GetRequestStream())
            {
                stream.Write(input, 0, input.Length);
            }

            using (var response = (HttpWebResponse)request.GetResponse())
            using (var reader = new StreamReader(response.GetResponseStream(), Encoding.UTF8))
            {
                var responseText = reader.ReadToEnd();
                return JObject.Parse(responseText);
            }
        }

        private static Dictionary<string, int> DeserializeResult(JObject responseData, int repetitions)
        {
            var measurementsStrings = (JObject)responseData["measurements"];

            var measurements = new Dictionary<string, int>();
            foreach (var key in measurementsStrings.Properties())
            {
                int count = (int)Math.Round(measurementsStrings[key.Name].ToObject<double>() * repetitions);
                measurements[key.Name] = count;
            }

            return measurements;
        }
    }
}