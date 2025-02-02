module Automatski
  module Komenco
  
    class Operation
      attr_reader :gate, :qubits, :params

      def initialize(gate, qubits, params)
        @gate = gate
        @qubits = qubits
        @params = params
      end

      def get_gate
        @gate
      end

      def get_qubits
        @qubits
      end

      def get_params
        @params
      end
    end
	
    class QuantumCircuit
      attr_reader :num_qubits, :operations

      def initialize(num_qubits)
        @num_qubits = num_qubits
        @operations = []
      end

      def get_num_qubits
        @num_qubits 
      end
	  
	  def get_operations
        @operations
      end

      def add_single(gate, params, qubits)
        if qubits.size != 1
          raise ArgumentError, "Number of qubits for gate #{gate} has to be one"
        end
        qubits.each do |qubit|
          if qubit < 0 || qubit >= @num_qubits
            raise ArgumentError, "Invalid qubit: #{qubit}"
          end
        end
        @operations << Operation.new(gate, qubits, params)
      end

      def add_double(gate, params, qubits)
        if qubits.size != 2
          raise ArgumentError, "Number of qubits for gate #{gate} has to be two"
        end
        qubits.each do |qubit|
          if qubit < 0 || qubit >= @num_qubits
            raise ArgumentError, "Invalid qubit: #{qubit}"
          end
        end
        @operations << Operation.new(gate, qubits, params)
      end

      def add_triple(gate, params, qubits)
        if qubits.size != 3
          raise ArgumentError, "Number of qubits for gate #{gate} has to be three"
        end
        qubits.each do |qubit|
          if qubit < 0 || qubit >= @num_qubits
            raise ArgumentError, "Invalid qubit: #{qubit}"
          end
        end
        @operations << Operation.new(gate, qubits, params)
      end

      def add_multiple(gate, params, qubits)
        required_qubits = Math.log(gate.length) / Math.log(2)
        if qubits.size != required_qubits.to_i
          raise ArgumentError, "Number of qubits for gate #{gate} has to be #{required_qubits.to_i}"
        end
        qubits.each do |qubit|
          if qubit < 0 || qubit >= @num_qubits
            raise ArgumentError, "Invalid qubit: #{qubit}"
          end
        end
        @operations << Operation.new(gate, qubits, params)
      end

      def id(qubit1)
        add_single("id", [], [qubit1])
      end

      def x(qubit1)
        add_single("x", [], [qubit1])
      end

      def y(qubit1)
        add_single("y", [], [qubit1])
      end

      def z(qubit1)
        add_single("z", [], [qubit1])
      end

      def h(qubit1)
        add_single("h", [], [qubit1])
      end

      def s(qubit1)
        add_single("s", [], [qubit1])
      end

      def sdg(qubit1)
        add_single("sdg", [], [qubit1])
      end

      def t(qubit1)
        add_single("t", [], [qubit1])
      end

      def tdg(qubit1)
        add_single("tdg", [], [qubit1])
      end

      def rx(theta, qubit1)
        add_single("rx", [theta], [qubit1])
      end

      def ry(theta, qubit1)
        add_single("ry", [theta], [qubit1])
      end

      def rz(theta, qubit1)
        add_single("rz", [theta], [qubit1])
      end

      def u(theta, phi, lam, qubit1)
        add_single("u", [theta, phi, lam], [qubit1])
      end

      def u1(theta, qubit1)
        add_single("u1", [theta], [qubit1])
      end

      def u2(phi, lam, qubit1)
        add_single("u2", [phi, lam], [qubit1])
      end

      def u3(theta, phi, lam, qubit1)
        add_single("u3", [theta, phi, lam], [qubit1])
      end

      def sx(qubit1)
        add_single("sx", [], [qubit1])
      end

      def sxdg(qubit1)
        add_single("sxdg", [], [qubit1])
      end

      def r(theta, phi, qubit1)
        add_single("r", [theta, phi], [qubit1])
      end

      def cx(qubit1, qubit2)
        add_double("cx", [], [qubit1, qubit2])
      end

      def cy(qubit1, qubit2)
        add_double("cy", [], [qubit1, qubit2])
      end

      def cz(qubit1, qubit2)
        add_double("cz", [], [qubit1, qubit2])
      end

      def ch(qubit1, qubit2)
        add_double("ch", [], [qubit1, qubit2])
      end

      def ucrx(theta, qubit1, qubit2)
        add_double("ucrx", [theta], [qubit1, qubit2])
      end

      def ucry(theta, qubit1, qubit2)
        add_double("ucry", [theta], [qubit1, qubit2])
      end

      def ucrz(theta, qubit1, qubit2)
        add_double("ucrz", [theta], [qubit1, qubit2])
      end

      def crx(theta, qubit1, qubit2)
        add_double("crx", [theta], [qubit1, qubit2])
      end

      def cry(theta, qubit1, qubit2)
        add_double("cry", [theta], [qubit1, qubit2])
      end

      def crz(theta, qubit1, qubit2)
        add_double("crz", [theta], [qubit1, qubit2])
      end

      def cr(theta, phi, lam, qubit1, qubit2)
        add_double("cr", [theta, phi, lam], [qubit1, qubit2])
      end

      def cu(theta, phi, lam, gamma, qubit1, qubit2)
        add_double("cu1", [theta, phi, lam, gamma], [qubit1, qubit2])
      end

      def cu1(theta, qubit1, qubit2)
        add_double("cu1", [theta], [qubit1, qubit2])
      end

      def cu2(phi, lam, qubit1, qubit2)
        add_double("cu2", [phi, lam], [qubit1, qubit2])
      end

      def cu3(theta, phi, lam, qubit1, qubit2)
        add_double("cu3", [theta, phi, lam], [qubit1, qubit2])
      end

      def dcx(qubit1, qubit2)
        add_double("dcx", [], [qubit1, qubit2])
      end

      def ecr(qubit1, qubit2)
        add_double("ecr", [], [qubit1, qubit2])
      end

      def iswap(qubit1, qubit2)
        add_double("iswap", [], [qubit1, qubit2])
      end

      def rxx(theta, qubit1, qubit2)
        add_double("rxx", [theta], [qubit1, qubit2])
      end

      def ryy(theta, qubit1, qubit2)
        add_double("ryy", [theta], [qubit1, qubit2])
      end

      def rzz(theta, qubit1, qubit2)
        add_double("rzz", [theta], [qubit1, qubit2])
      end

      def rzx(theta, qubit1, qubit2)
        add_double("rzx", [theta], [qubit1, qubit2])
      end

      def cswap(qubit1, qubit2, qubit3)
        add_triple("cswap", [], [qubit1, qubit2, qubit3])
      end

      def ccx(qubit1, qubit2, qubit3)
        add_triple("ccx", [], [qubit1, qubit2, qubit3])
      end

      def ccy(qubit1, qubit2, qubit3)
        add_triple("ccy", [], [qubit1, qubit2, qubit3])
      end

      def ccz(qubit1, qubit2, qubit3)
        add_triple("ccz", [], [qubit1, qubit2, qubit3])
      end

      def c3x(qubits)
        add_multiple("c3x", [], qubits)
      end

      def c4x(qubits)
        add_multiple("c4x", [], qubits)
      end

      def mcx(qubits)
        add_multiple("mcx", [], qubits)
      end

      def mcu1(theta, qubits)
        add_multiple("mcu1", [theta], qubits)
      end

      def mcu2(phi, lam, qubits)
        add_multiple("mcu2", [phi, lam], qubits)
      end

      def mcu3(theta, phi, lam, qubits)
        add_multiple("mcu3", [theta, phi, lam], qubits)
      end

      def mcz(qubits)
        add_multiple("mcz", [], qubits)
      end

      def mcp(qubits)
        add_multiple("mcp", [], qubits)
      end

      def mcrx(qubits)
        add_multiple("mcrx", [], qubits)
      end

      def mcry(qubits)
        add_multiple("mcry", [], qubits)
      end

      def mcrz(qubits)
        add_multiple("mcrz", [], qubits)
      end

      def qft(qubits)
        add_multiple("qft", [], qubits)
      end

      def inverse_qft(qubits)
        add_multiple("iqft", [], qubits)
      end

      def swap(qubit1, qubit2)
        add_double("swap", [], [qubit1, qubit2])
      end

      def csx(qubit1, qubit2)
        add_double("csx", [], [qubit1, qubit2])
      end

      def p(theta, qubit1)
        add_single("p", [theta], [qubit1])
      end

      def cp(theta, qubit1, qubit2)
        add_double("cp", [theta], [qubit1, qubit2])
      end

      def ccp(theta, qubit1, qubit2, qubit3)
        add_triple("ccp", [theta], [qubit1, qubit2, qubit3])
      end

      def sqrt_x(qubit1)
        add_single("sqrt_x", [], [qubit1])
      end

      def sqrt_y(qubit1)
        add_single("sqrt_y", [], [qubit1])
      end

      def sqrt_z(qubit1)
        add_single("sqrt_z", [], [qubit1])
      end

      def gpi(phi, qubit1)
        add_single("gpi", [phi], [qubit1])
      end

      def gpi2(phi, qubit1)
        add_single("gpi2", [phi], [qubit1])
      end

      def xp(theta, qubit1)
        add_single("xp", [theta], [qubit1])
      end

      def yp(theta, qubit1)
        add_single("yp", [theta], [qubit1])
      end

      def zp(theta, qubit1)
        add_single("zp", [theta], [qubit1])
      end

      def xxp(theta, qubit1, qubit2)
        add_double("xxp", [theta], [qubit1, qubit2])
      end

      def yyp(theta, qubit1, qubit2)
        add_double("yyp", [theta], [qubit1, qubit2])
      end

      def zzp(theta, qubit1, qubit2)
        add_double("zzp", [theta], [qubit1, qubit2])
      end

      def phased_xp(theta, phi, qubit1)
        add_single("phased_xp", [theta, phi], [qubit1])
      end

      def phased_yp(theta, phi, qubit1)
        add_single("phased_yp", [theta, phi], [qubit1])
      end

      def phased_zp(theta, phi, qubit1)
        add_single("phased_zp", [theta, phi], [qubit1])
      end

      def cnotp(theta, qubit1, qubit2)
        add_double("cnotp", [theta], [qubit1, qubit2])
      end

      def ccnotp(theta, qubit1, qubit2, qubit3)
        add_triple("ccnotp", [theta], [qubit1, qubit2, qubit3])
      end

      def cyp(theta, qubit1, qubit2)
        add_double("cyp", [theta], [qubit1, qubit2])
      end

      def ccyp(theta, qubit1, qubit2, qubit3)
        add_triple("ccyp", [theta], [qubit1, qubit2, qubit3])
      end

      def czp(theta, qubit1, qubit2)
        add_double("czp", [theta], [qubit1, qubit2])
      end

      def cczp(theta, qubit1, qubit2, qubit3)
        add_triple("cczp", [theta], [qubit1, qubit2, qubit3])
      end

      def measure(qubits)
        cparams = []
        cqubits = []
        cgate = "measure"
        if qubits.empty?
          raise ArgumentError, "number of qubits to measure cannot be zero"
        else
          qubits.each do |qubit|
            if qubit < 0 || qubit >= @num_qubits
              raise ArgumentError, "invalid qubit: #{qubit}"
            else
              cqubits << qubit
            end
          end
        end
        @operations << Operation.new(cgate, cqubits, cparams)
      end

      def measure_all
        cparams = []
        cqubits = []
        cgate = "measure"
        (0...@num_qubits).each do |qubit|
          cqubits << qubit
        end
        @operations << Operation.new(cgate, cqubits, cparams)
      end

      def random_circuit(number_of_operations, qubits_to_use_for_random_circuit)
        qubits_count = qubits_to_use_for_random_circuit.size
        if qubits_count < 3
          raise ArgumentError, "The number of qubits needed to generate random circuits is >= 3"
        end

        gates_and_qubits_map = {
          # 1 qubit gates
          "x" => 1, "y" => 1, "z" => 1, "rx" => 1, "ry" => 1, "rz" => 1,
          "h" => 1, "s" => 1, "sdg" => 1, "t" => 1, "tdg" => 1, "sx" => 1, "sxdg" => 1,
          # 2 qubit gates
          "cx" => 2, "cy" => 2, "cz" => 2, "crx" => 2, "cry" => 2, "crz" => 2,
          "ch" => 2, "dcx" => 2, "ecr" => 2, "iswap" => 2, "swap" => 2, "csx" => 2,
          # 3 qubit gates
          "cswap" => 3, "ccx" => 3
        }

        all_possible_gates = gates_and_qubits_map.keys
        all_possible_gates_count = all_possible_gates.size

        number_of_operations.times do
          index = rand(all_possible_gates_count)
          cgate = all_possible_gates[index]

          number_of_qubits = gates_and_qubits_map[cgate]

          qubits_to_use_for_random_circuit.shuffle!
          cqubits = qubits_to_use_for_random_circuit.take(number_of_qubits)

          cparams = []
          if ["rx", "ry", "rz", "crx", "cry", "crz"].include?(cgate)
            theta = rand * 2 * Math::PI
            cparams << theta
          end

          @operations << Operation.new(cgate, cqubits, cparams)
        end
      end
    end
	
  end
end