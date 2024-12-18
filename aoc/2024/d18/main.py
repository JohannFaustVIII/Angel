with open("data.txt", "r") as f:
	VALUES = tuple([tuple([int(k) for k in line.strip().split(",")]) for line in f.readlines()])

MAX_SIZE = 70
SIZE = 1024

def ex1(SIZE):
	_map = VALUES[:SIZE]
	start = (0, 0)
	end = (MAX_SIZE, MAX_SIZE)
	to_visit = [(start, 0, [start])]
	min_vals = {}
	dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	while to_visit:
		to_visit.sort(key = lambda x : x[1])
		p, val, path = to_visit.pop(0)
		if p in min_vals:
			continue
		min_vals[p] = val
		if p == end:
			return val, path
		for d in dirs:
			next_p = (p[0] + d[0], p[1] + d[1])
			if not is_in_bounds(next_p):
				continue
			if next_p in _map:
				continue
			if next_p not in min_vals:
				to_visit.append((next_p, val + 1, [x for x in path] + [next_p]))
	return None


def is_in_bounds(point):
	for p in point:
		if p < 0:
			return False
		if p > MAX_SIZE:
			return False
	return True


def ex2():
	result = ""
	blocking_point = None
	SIZE = 1024
	while True:
		result = ex1(SIZE)
		if result is None:
			return ",".join([str(x) for x in blocking_point])
		_ind = min([i for i, point in enumerate(VALUES) if point in result[1]])
		SIZE = _ind + 1
		blocking_point = VALUES[_ind]

print(f'D18 Task 1 answer: {ex1(SIZE)[0]}')
print(f'D18 Task 2 answer: {ex2()}')