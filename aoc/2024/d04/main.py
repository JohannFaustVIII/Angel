with open("data.txt", "r") as f:
	INPUT = [f.strip() for f in f.readlines()]

WORD = "XMAS"


def ex1():
	result = 0
	for y in range(len(INPUT)):
		for x in range(len(INPUT[0])):
			cords = (x,y)
			result += check_char(cords, 0, None)
	return result

def check_char(cords, phase, diag):
	if phase == len(WORD):
		return 1
	if diag is None:
		s = 0
		for dx in range(-1,2):
			for dy in range(-1,2):
				s += check_char(cords, phase, (dx, dy))
		return s
	x = cords[0] + phase * diag[0]
	y = cords[1] + phase * diag[1]
	if x < 0 or x >= len(INPUT[0]):
		return 0
	if y < 0 or y >= len(INPUT):
		return 0
	if INPUT[y][x] != WORD[phase]:
		return 0
	return check_char(cords, phase + 1, diag)

def ex2():
	result = 0
	for y in range(len(INPUT)):
		for x in range(len(INPUT[0])):
			cords = (x,y)
			result += check_cross(cords, None)
	return result

def check_cross(cords, diag):
	if diag is None:
		if INPUT[cords[1]][cords[0]] != 'A':
			return 0
		s = 0
		for diag in [(-1, -1), (-1, 1), (1, -1), (1,1)]:
			s += check_cross(cords, diag)
		return 1 if s == 2 else 0
	else:
		x = cords[0] + diag[0]
		y = cords[1] + diag[1]
		if x < 0 or x >= len(INPUT[0]):
			return 0
		if y < 0 or y >= len(INPUT):
			return 0
		if INPUT[y][x] != 'M':
			return 0
		x = cords[0] - diag[0]
		y = cords[1] - diag[1]
		if x < 0 or x >= len(INPUT[0]):
			return 0
		if y < 0 or y >= len(INPUT):
			return 0
		if INPUT[y][x] != 'S':
			return 0
		return 1

print(f'D04 Task 1 answer: {ex1()}')
print(f'D04 Task 2 answer: {ex2()}')