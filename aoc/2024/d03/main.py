import re

with open("data.txt", "r") as f:
	lines = f.readlines()

def ex1(lines):
	s = 0
	for l in lines:
		s += check_line(l)
	return s

def check_line(line):
	s = 0
	found = re.findall("mul\([1-9][0-9]*,[1-9][0-9]*\)", line)
	for f in found:
		s += compute(f)
	return s

def compute(mul):
	left, right = [int(x) for x in mul[4:-1].split(",")]
	return left * right


def ex2(lines):
	instructions = []
	for l in lines:
		instructions += check_line_2(l)
	return compute_instructions(instructions)


def check_line_2(line):
	s = 0
	found = re.findall("mul\([1-9][0-9]*,[1-9][0-9]*\)|do\(\)|don't\(\)", line)
	return found

def compute_instructions(instructions):
	mult = 1
	to_add = 0
	result = 0
	for inst in instructions:
		if inst.startswith("mul"):
			to_add = compute(inst)
			result += to_add * mult
		else:
			mult = 1 if len(inst) == 4 else 0
	return result

print(f'D03 Task 1 answer: {ex1(lines)}')
print(f'D03 Task 2 answer: {ex2(lines)}')