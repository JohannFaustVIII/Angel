MAP = []

with open("data.txt", "r") as f:
	MAP = [line for line in f.readlines()]

def ex1and2():
	start = find_pos("S")
	end = find_pos("E")
	direction = 1
	DIRS = {0 : (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
	min_vals = {}
	to_visit = [(start[0], start[1], 1, 0, [[start]])] # x, y, direction, value, paths
	found_exit = False
	found_value = -1
	best_spots = []
	while to_visit:
		x, y, direction, value, paths = to_visit.pop(0)
		if (x, y, direction) in min_vals.keys():
			continue
		min_vals[(x, y, direction)] = value
		if (x, y) == end and (found_value == -1 or found_value == value):
			found_value = value
			for path in paths:
				best_spots += path
			found_exit = True
		elif found_exit and found_value != value:
			break
		for _d, _dp in DIRS.items():
			new_x = x + _dp[0]
			new_y = y + _dp[1]
			if MAP[new_y][new_x] == '#':
				continue
			diff = abs(_d - direction) if abs(_d - direction) < 3 else 1
			new_value = value + diff * 1000 + 1
			if (new_x, new_y, _d) not in min_vals.keys():
				_found = False
				for i, item in enumerate(to_visit):
					_x, _y, _dd, _v, _ = item
					if (_x, _y, _dd, _v) == (new_x, new_y, _d, new_value):
						_found = True
						new_paths = [p for p in to_visit[i][4]]
						for p in paths:
							new_paths.append(p + [(new_x, new_y)])
						to_visit[i][4] = new_paths
				if not _found:
					new_paths = []
					for path in paths:
						new_paths.append(path + [(new_x, new_y)])
					to_visit.append([new_x, new_y, _d, new_value, new_paths])

		to_visit.sort(key=lambda x : x[3])

	return found_value, len(set(best_spots))



def find_pos(sign):
	for y, line in enumerate(MAP):
		for x, _s in enumerate(line):
			if _s == sign:
				return (x, y)

a1, a2 = ex1and2()

print(f'D16 Task 1 answer: {a1}')
print(f'D16 Task 2 answer: {a2}')