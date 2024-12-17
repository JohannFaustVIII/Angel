with open("data.txt", "r") as f:
	VALUES = [[int(k) for k in line.split(":")[1].strip().split(",") if k] for line in f.readlines() if line.strip()]

print(VALUES)

class Device:

	def __init__(self, A, B, C, program):
		self.A = A
		self.B = B
		self.C = C
		self.program = program

	def run_program(self):
		self.inst = 0
		output = []
		funcs = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self. out, self.bdv, self.cdv]
		while self.inst < len(self.program):
			combo = self.program[self.inst]
			operand = self.program[self.inst + 1]
			self.inst += 2

			out = funcs[combo](operand)
			if out is not None:
				output.append(out)

		return output


	def get_combo(self, value):
		if value < 4:
			return value
		elif value == 4:
			return self.A
		elif value == 5:
			return self.B
		elif value == 6:
			return self.C

	def adv(self, operand):
		self.A = self.A // (2**self.get_combo(operand))

	def bdv(self, operand):
		self.B = self.A // (2**self.get_combo(operand))

	def cdv(self, operand):
		self.C = self.A // (2**self.get_combo(operand))

	def jnz(self, operand):
		if self.A != 0:
			self.inst = operand

	def bxl(self, operand):
		self.B = self.B ^ operand

	def bst(self, operand):
		self.B = self.get_combo(operand) % 8

	def bxc(self, operand):
		self.B = self.B ^ self.C

	def out(self, operand):
		return self.get_combo(operand) % 8


device = Device(VALUES[0][0], VALUES[1][0], VALUES[2][0], VALUES[3])

def ex1():
	device = Device(VALUES[0][0], VALUES[1][0], VALUES[2][0], VALUES[3])
	output = device.run_program()
	return ",".join([str(o) for o in output])

def ex2():
	expected_program = VALUES[3]
	reg_a = 0
	while True:
		device = Device(reg_a, VALUES[1][0], VALUES[2][0], VALUES[3])
		out = device.run_program()
		if len(out) > 1:
			break
		reg_a += 1

	mult = reg_a
	out = []
	reg_a = 0
	while len(out) != len(expected_program):
		device = Device(reg_a, VALUES[1][0], VALUES[2][0], VALUES[3])
		out = device.run_program()
		if out != expected_program[-1 * len(out):]:
			reg_a += 1
		else:
			reg_a *= mult

	return reg_a

print(f'D17 Task 1 answer: {ex1()}')
print(f'D17 Task 2 answer: {ex2()}')