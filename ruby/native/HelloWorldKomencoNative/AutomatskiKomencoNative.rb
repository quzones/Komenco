require 'json'
require 'net/http'
require 'uri'

require_relative 'QuantumCircuit'

include Automatski::Komenco

module Automatski
  module Komenco
    class AutomatskiKomencoNative
      def initialize(host, port)
        @host = host
        @port = port
      end

      def run(circuit, repetitions, topK)
        tstart = Time.now

        body = serialize_circuit(circuit, topK)
        struct = post_request(body)

        tend = Time.now
        execution_time = (tend - tstart) * 1000
        puts "Time Taken #{execution_time}ms"

        if struct.key?('error')
          puts struct['error']
          raise RuntimeError, struct['error']
        end

        deserialize_result(struct, repetitions)
      end

      private

      def serialize_circuit(circuit, topK)
        num_qubits = circuit.get_num_qubits

        operations = []
        measurements = []

        circuit.get_operations.each do |operation|
          gate = operation.get_gate
          params = operation.get_params
          qubits = operation.get_qubits

          if gate == 'measure'
            measurements.concat(qubits)
          else
            op = {
              'gate' => gate,
              'params' => params,
              'qubits' => qubits
            }
            operations << op
          end
        end

        puts "Executing Quantum Circuit With..."
        puts "#{num_qubits} Qubits And ..."
        puts "#{operations.size} Gates"

        if measurements.empty?
          raise RuntimeError, 'There are no measurements done at the end of the circuit.'
        end

        {
          'num_qubits' => num_qubits,
          'operations' => operations,
          'measurements' => measurements,
          'topK' => topK
        }
      end

      def post_request(body)
        url = URI.parse("http://#{@host}:#{@port}/api/komenco")
        http = Net::HTTP.new(url.host, url.port)
        request = Net::HTTP::Post.new(url.path, { 'Content-Type' => 'application/json', 'Accept' => 'application/json' })
        request.body = body.to_json

        response = http.request(request)
        if response.code.to_i >= 400
          raise StandardError, 'Error making POST request'
        end

        JSON.parse(response.body)
      end

      def deserialize_result(response_data, repetitions)
        measurements_strings = response_data['measurements']

        measurements = {}
        measurements_strings.each do |key, value|
          count = (value * repetitions).round
          measurements[key] = count
        end

        measurements
      end
    end
  end
end