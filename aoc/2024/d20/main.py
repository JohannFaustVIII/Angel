with open("data.txt", "r") as f:
	LINES = [l.strip() for l in f.readlines()]

def parse_lines(lines):
	start = None
	end = None
	points = []
	for y, line in enumerate(LINES):
		for x, sign in enumerate(line):
			if sign == 'S':
				start = (x, y)
			if sign == 'E':
				end = (x, y)
			if sign != '#':
				points.append((x, y))

		if start is not None and end is not None:
			break
	dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	path = [start]
	while path[-1] != end:
		last = path[-1]
		for d in dirs:
			_next = (last[0] + d[0], last[1] + d[1])
			if not is_in_bounds(_next):
				continue
			_ns = LINES[_next[1]][_next[0]]
			if _ns == '#':
				continue
			if _next in path:
				continue
			path.append(_next)
			break

	return start, end, path

def is_in_bounds(point):
	if point[0] < 0:
		return False
	if point[1] < 0:
		return False
	if point[0] >= len(LINES[0]):
		return False
	if point[1] >= len(LINES):
		return False
	return True

def ex1and2():
	start, end, path = parse_lines(LINES)
	count1 = 0
	count2 = 0
	for i1, p1 in enumerate(path):
		for i2, p2 in enumerate(path[i1 + 1:]):
			i2 = i2 + i1 + 1
			if i1 == i2:
				continue
			nc = i2 - i1
			diff = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
			if diff <= 2:
				if (nc - diff) >= 100:
					count1 += 1
			if diff <= 20:
				if (nc - diff) >= 100:
					count2 += 1
	return count1, count2

a1, a2 = ex1and2()

print(f'D20 Task 1 answer: {a1}')
print(f'D20 Task 2 answer: {a2}')