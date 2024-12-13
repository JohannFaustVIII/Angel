import re

CASES = []
with open("data.txt", "r") as f:
	lines = [s.strip() for s in f.readlines()]
	for i in range(0, len(lines), 4):
		case = []
		for j in range(3):
			case.append([int(k) for k in re.findall("[0-9]+", lines[i + j])])
		CASES.append(case)

def ex1(CASES, minimum = True):
	result = 0
	for case in CASES:
		result += get_tokens(case, minimum)
	return result

def get_tokens(case, minimum):
	a_button = case[0]
	b_button = case[1]
	goal = case[2]

	det = case[0][0]*case[1][1] - case[0][1]*case[1][0]
	a_det = case[2][0]*case[1][1] - case[2][1]*case[1][0]
	b_det = case[0][0]*case[2][1] - case[0][1]*case[2][0]

	if det == 0:
		return 0

	if a_det % det != 0 or b_det % det != 0:
		return 0

	a = a_det // det
	b = b_det // det

	if minimum:
		if a >= 100 or b >= 100:
			return 0

	if a < 0 or b < 0:
		return 0

	return 3 * a + b

def ex2(CASES):
	for case in CASES:
		case[2][0] += 10000000000000
		case[2][1] += 10000000000000
	return ex1(CASES, False)

print(f'D13 Task 1 answer: {ex1(CASES)}')
print(f'D13 Task 2 answer: {ex2(CASES)}')