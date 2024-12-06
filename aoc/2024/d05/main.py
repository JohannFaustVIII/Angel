RULES = []
CASES = []

with open("data.txt", "r") as f:
	for s in f.readlines():
		if "|" in s:
			RULES.append(tuple([int(k) for k in s.strip().split('|')]))
		elif "," in s:
			CASES.append([int(k) for k in s.strip().split(',')])

def ex1():
	result = 0
	for c in CASES:
		result += check_case(c)
	return result

def check_case(c):
	for i, p1 in enumerate(c):
		for p2 in c[i+1:]:
			if (p2, p1) in RULES:
				return 0
	return c[int((len(c)-1)/2)]

def ex2():
	result = 0
	for c in CASES:
		result += check_incorrect_case(c)
	return result

def check_incorrect_case(c):
	incorrect = False
	for i in range(len(c)):
		for j in range(i+1, len(c)):
			p1 = c[i]
			p2 = c[j]
			if (p2, p1) in RULES:
				incorrect = True
				c[i] = p2
				c[j] = p1
	return c[int((len(c)-1)/2)] if incorrect else 0

print(f'D05 Task 1 answer: {ex1()}')
print(f'D05 Task 2 answer: {ex2()}')