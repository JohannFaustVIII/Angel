with open("test.txt", "r") as f:
	MAP = [[int(v) for v in s.strip()] for s in f.readlines()]

def ex1():
	
	result = 0
	starting_points = find_starting_points()
	for start in starting_points:
		result += find_trails(start)
	return result

def find_starting_points():
	result = []
	for y, line in enumerate(MAP):
		for x, sign in enumerate(line):
			if sign == 0:
				result.append((x, y))
	return result

def find_trails(start):
	dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	result = []
	visited = [start]
	to_visit = [start]

	while len(to_visit) > 0:
		_p = to_visit[0]
		if MAP[_p[1]][_p[0]] == 9:
			result.append(_p)
		for d in dirs:
			_np = (_p[0] + d[0], _p[1] + d[1])
			if check_bound(_np):
				if _np in visited:
					continue
				elif MAP[_np[1]][_np[0]] == MAP[_p[1]][_p[0]] + 1:
					to_visit.append(_np)
					visited.append(_np)

		to_visit.pop(0)

	return len(set(result))

def check_bound(point):
	if point[0] < 0:
		return False
	if point[0] >= len(MAP[0]):
		return False
	if point[1] < 0:
		return False
	if point[1] >= len(MAP):
		return False
	return True

def ex2():
	result = 0
	starting_points = find_starting_points()
	for start in starting_points:
		result += get_rating([start])
	return result

def get_rating(trail):
	result = 0
	dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	if len(trail) == 10:
		return 1

	_p = trail[-1]
	for d in dirs:
		_np = (_p[0] + d[0], _p[1] + d[1])
		if check_bound(_np):
			if _np in trail:
				continue
			elif MAP[_np[1]][_np[0]] == MAP[_p[1]][_p[0]] + 1:
				result += get_rating(trail + [_np])

	return result


print(f'D10 Task 1 answer: {ex1()}')
print(f'D10 Task 2 answer: {ex2()}')