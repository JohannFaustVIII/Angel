with open("data.txt", "r") as f:
	MAP = [s.strip() for s in f.readlines()]

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def ex1():
	return len(get_visited_places()[0])

def find_start():
	position = None
	facing = None

	for y, s in enumerate(MAP):
		for x, sign in enumerate(s):
			if sign not in ['#', '.']:
				position = (x, y)
				if sign == '^':
					facing = 0
				elif sign == '>':
					facing = 1
				elif sign == 'v':
					facing = 2
				else:
					facing = 3

	return position, facing

def get_visited_places():
	position, facing = find_start()

	visited = set()
	looped = False
	while position is not None:
		if (position, facing) in visited:
			looped = True
			break
		visited.add((position, facing))
		new_position = (position[0] + DIRECTIONS[facing][0], position[1] + DIRECTIONS[facing][1])
		if new_position[0] < 0 or new_position[0] >= len(MAP[0]):
			position = None
		elif new_position[1] < 0 or new_position[1] >= len(MAP):
			position = None
		elif MAP[new_position[1]][new_position[0]] == '#':
			facing = (facing + 1) % 4
		else:
			position = new_position

	return set([v[0] for v in visited]), looped


def ex2():
	position, facing = find_start()
	visited_places = get_visited_places()[0]

	visited_places.remove(position)

	loops = 0

	for p in visited_places:
		MAP[p[1]] = MAP[p[1]][:p[0]] + '#' + MAP[p[1]][p[0] + 1:]
		looped = get_visited_places()[1]
		if looped:
			loops += 1
		MAP[p[1]] = MAP[p[1]][:p[0]] + '.' + MAP[p[1]][p[0] + 1:]
	return loops


print(f'D06 Task 1 answer: {ex1()}')
print(f'D06 Task 2 answer: {ex2()}')