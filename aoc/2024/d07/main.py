CASES = []
with open("data.txt", "r") as f:
	for x in f.readlines():
		left, right = x.strip().split(":")
		CASES.append((int(left), [int(k) for k in right.strip().split(" ")]))

def ex1and2(concat):
	result = 0
	for c in CASES:
		expected = c[0]
		numbers = c[1]
		if check_number(concat, numbers, expected, len(numbers)):
			result += expected
	return result

def check_number(concat, numbers, value, calcs_left):
	if calcs_left == 1:
		return value == numbers[0]
	if value < 1:
		return False
	calcs_left -= 1
	next_val = numbers[calcs_left]
	if value % next_val == 0:
		if check_number(concat, numbers, int(value/next_val), calcs_left):
			return True
	if check_number(concat, numbers, value - next_val, calcs_left):
		return True
	if concat:
		i = 1
		while next_val % i != next_val:
			i *= 10
		if value % i == next_val:
			return check_number(concat, numbers, int((value - next_val)/i), calcs_left)
	return False

print(f'D07 Task 1 answer: {ex1and2(False)}')
print(f'D07 Task 2 answer: {ex1and2(True)}')