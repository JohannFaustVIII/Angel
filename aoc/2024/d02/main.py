with open("data.txt", "r") as f:
	lines = [[int(x) for x in f.strip().split(" ")] for f in f.readlines()]

def ex1(lines):
	return sum([is_correct(line) for line in lines])

def is_correct(line):
	inc = line[1] > line[0]
	for i in range(len(line) - 1):
		dif = line[i+1] - line[i]
		if not(0 < abs(dif) <= 3 and ((line[i+1] > line[i]) is inc)):
			return 0
	return 1

def ex2(lines):
	s = 0

	for line in lines:
		to_add = is_correct(line)
		if to_add == 0:
			to_add = is_correct_remove(line)
		s += to_add

	return s

def is_correct_remove(line):
	for i in range(len(line)):
		val = is_correct(line[:i] + line[i+1:])
		if val:
			return val
	return 0

print(f'D02 Task 1 answer: {ex1(lines)}')
print(f'D02 Task 2 answer: {ex2(lines)}')