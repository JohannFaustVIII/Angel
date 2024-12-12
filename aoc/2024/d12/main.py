def add_to_map(_map, key, val):
	if key in _map:
		_map[key] += val
	else:
		_map[key] = val
	return _map


with open("data.txt", "r") as f:
	MAP = [s.strip() for s in f.readlines()]

def ex1():
	visited = []
	result = 0
	for y, line in enumerate(MAP):
		for x, sign in enumerate(line):
			if (x, y) in visited:
				continue
			result += compute_fence(visited, (x, y))

	return result

def compute_fence(visited, start):
	sign = MAP[start[1]][start[0]]

	to_visit = [start]
	area = []
	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	fence = {}
	while to_visit:
		_next = to_visit.pop(0)
		if not is_in_bounds(_next):
			add_to_map(fence, _next, 1)
			continue
		if MAP[_next[1]][_next[0]] != sign:
			add_to_map(fence, _next, 1)
			continue
		if _next in visited:
			continue
		visited.append(_next)
		area.append(_next)
		for d in dirs:
			to_visit.append((_next[0] + d[0], _next[1] + d[1]))
	outer = [v for k,v in fence.items()]
	return sum(outer) * len(set(area))

def is_in_bounds(point):
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
	visited = []
	result = 0
	for y, line in enumerate(MAP):
		for x, sign in enumerate(line):
			if (x, y) in visited:
				continue
			result += compute_sided_fence(visited, (x, y))

	return result

def compute_sided_fence(visited, start):
	sign = MAP[start[1]][start[0]]

	to_visit = [(start[0], start[1], -1)]
	area = []
	dirs = [(1, 0, 0), (-1, 0, 1), (0, 1, 2), (0, -1, 3)]
	fence = {}
	while to_visit:
		_next = to_visit.pop(0)
		if not is_in_bounds(_next):
			add_to_map(fence, _next, 1)
			continue
		if MAP[_next[1]][_next[0]] != sign:
			add_to_map(fence, _next, 1)
			continue
		if (_next[0],_next[1]) in visited:
			continue
		visited.append((_next[0],_next[1]))
		area.append((_next[0],_next[1]))
		for d in dirs:
			to_visit.append((_next[0] + d[0], _next[1] + d[1], d[2]))

	sides = get_sides(fence)
	outer = [v for k,v in fence.items()]
	return sides * len(set(area))

def get_sides(fence):
	fence = [k for k in fence.keys()]
	result = 0
	for i in range(4):
		points = [p for p in fence if p[2] == i]
		if i < 2:
			levels = set([p[0] for p in points])
			for level in levels:
				_lp = [p for p in points if p[0] == level]
				_lp.sort(key = lambda p: p[1])
				sides = 1
				for i in range(len(_lp)-1):
					if abs(_lp[i][1] - _lp[i+1][1]) != 1:
						sides += 1
				result += sides
		else:
			levels = set([p[1] for p in points])
			for level in levels:
				_lp = [p for p in points if p[1] == level]
				_lp.sort(key = lambda p: p[0])
				sides = 1
				for i in range(len(_lp)-1):
					if abs(_lp[i][0] - _lp[i+1][0]) != 1:
						sides += 1
				result += sides
	return result


print(f'D12 Task 1 answer: {ex1()}')
print(f'D12 Task 2 answer: {ex2()}')