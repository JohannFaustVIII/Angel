def to_list(_space):
	return sum([[s[1]] * s[0] for s in _space], [])

with open("data.txt", "r") as f:
	SPACE2 = [(int(k), int(i/2) if i %2 == 0 else -1) for i, k in enumerate(f.readlines()[0])]
	SPACE = to_list(SPACE2)

def ex1():
	disk = [s for s in SPACE]

	try:
		while True:
			ind = disk.index(-1)
			disk[ind] = disk[-1]
			disk = disk[:-1]
	except ValueError:
		pass

	return sum([i*v for i,v in enumerate(disk)])

def ex2():
	_space = [s for s in SPACE2]
	for i in range(len(_space) - 1, -1, -1):
		if _space[i][1] == -1:
			continue
		for j in range(i):
			if _space[j][1] != -1:
				continue
			if _space[j][0] < _space[i][0]:
				continue
			size = _space[i][0]
			value = _space[i][1]
			_space[i] = (_space[i][0], -1)
			_space = _space[:j] + [(size, value), (_space[j][0] - size, -1)] + _space[j + 1:]
			break

	disk = to_list(_space)
	return sum([i*v for i, v in enumerate(disk) if v != -1])

print(f'D09 Task 1 answer: {ex1()}')
print(f'D09 Task 2 answer: {ex2()}')