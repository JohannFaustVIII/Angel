def bin_towel(t):
	_map = {'w': 0, 'u': 1, 'b':2, 'r':3, 'g':4}
	value = 0
	for mult, sign in enumerate(t):
		value += (1 << (_map[sign])) << (mult*5)
	return value

MEM = {}
MEM2 = {}
with open("data.txt", "r") as f:
	LINES = f.readlines()
	TOWELS = [(bin_towel(t.strip()), len(t.strip())) for t in LINES[0].strip().split(",")]
	PATTERNS = [bin_towel(p.strip()) for p in LINES[2:]]

TOWELS.sort(reverse = True, key= lambda x : x[0])

def ex1():
	result = 0
	for p in PATTERNS:
		if is_pattern_possible(p):
			result += 1
	return result

def is_pattern_possible(v):
	# print(f'Case = {v}')
	if v == 0:
		return True
	if v in MEM:
		return MEM[v]

	for towel, length in TOWELS:
		v_to_check = v & ((1 << ((length)*5)) - 1)
		# print(towel, length, v_to_check)
		if v_to_check == towel:
			v_next = v >> (length*5)
			if is_pattern_possible(v_next):
				MEM[v] = True
				return True

	MEM[v] = False
	return False


def ex2():
	result = 0
	for p in PATTERNS:
		result += is_pattern_possible2(p)
	return result

def is_pattern_possible2(v):
	if v == 0:
		return 1
	if v in MEM2:
		return MEM2[v]

	result = 0

	for towel, length in TOWELS:
		v_to_check = v & ((1 << ((length)*5)) - 1)
		# print(towel, length, v_to_check)
		if v_to_check == towel:
			v_next = v >> (length*5)
			result += is_pattern_possible2(v_next)

	MEM2[v] = result
	return result



print(f'D19 Task 1 answer: {ex1()}')
print(f'D19 Task 2 answer: {ex2()}')