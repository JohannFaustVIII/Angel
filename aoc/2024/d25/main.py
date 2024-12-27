
KEYS = []
LOCKS = []

MAP = []
with open("data.txt", "r") as f:
	for l in f.readlines():
		l = l.strip()
		if l:
			MAP.append(l)
		else:
			val = (tuple([sum([1 for row in range(len(MAP)) if MAP[row][column] == '#']) for column in range(len(MAP[0]))]))
			if MAP[0][0] == '#':
				KEYS.append(val)
			else:
				LOCKS.append(val)
			MAP = []
	val = (tuple([sum([1 for row in range(len(MAP)) if MAP[row][column] == '#']) for column in range(len(MAP[0]))]))
	if MAP[0][0] == '#':
		KEYS.append(val)
	else:
		LOCKS.append(val)

def ex1():
	count = 0

	for k in KEYS:
		for l in LOCKS:
			if all([k[i] + l[i] <= 7 for i in range(len(k))]):
				count += 1

	return count
	pass

print(f'D25 Task 1 answer: {ex1()}')