MAP = []
moves = ""
read_map = True
with open("data.txt", "r") as f:
	for line in f.readlines():
		if line.strip():
			if read_map:
				MAP.append(line.strip())
			else:
				moves += line.strip()
		else:
			read_map = False

DIRS = {'^' : (0, -1), 'v': (0, 1), '>': (1, 0), '<':(-1, 0)}

def ex1():
	_map = [[l for l in line] for line in MAP]
	pos = find_pos(_map)
	for sign in moves:
		_, pos = move(_map, pos, DIRS[sign])
	result = compute_crates(_map)
	return result

def find_pos(_map):
	for y, line in enumerate(_map):
		for x, sign in enumerate(line):
			if sign == '@':
				return (x, y)

def move(_map, pos, _dir):
	new_pos = (pos[0] + _dir[0], pos[1] + _dir[1])
	sign = _map[new_pos[1]][new_pos[0]]
	move_possible = False
	if sign == '#':
		move_possible = False
	elif sign == '.':
		move_possible = True
	else:
		move_possible, _ = move(_map, new_pos, _dir)

	if move_possible:
		_map[new_pos[1]][new_pos[0]] = _map[pos[1]][pos[0]]
		_map[pos[1]][pos[0]] = '.'
		return True, new_pos
	else:
		return False, pos

def compute_crates(_map):
	_sum = 0
	for y, line in enumerate(_map):
		for x, sign in enumerate(line):
			if sign == 'O':
				_sum += y*100 + x
	return _sum


def ex2():
	_map = get_wider_map(MAP)
	pos = find_pos(_map)
	bcrates = count_crates(_map)
	for sign in moves:
		# print(f'Move {sign}')
		_, pos = move_2(_map, pos, DIRS[sign])
	result = compute_crates_2(_map)
	# for l in _map:
	# 	print(''.join(l))
	acrates = count_crates(_map)
	print(f'{bcrates} -> {acrates}')
	return result

def count_crates(_map):
	r = 0
	for line in _map:
		for s in line:
			if s == '[':
				r += 1
	return r

def move_2(_map, pos, _dir):
	new_pos = (pos[0] + _dir[0], pos[1] + _dir[1])
	old_sign = _map[pos[1]][pos[0]]
	sign = _map[new_pos[1]][new_pos[0]]
	move_possible = False
	if old_sign == '.':
		return True, pos
	if old_sign == '#':
		print(f'Try to move #!!!')
		return False, pos
	if _dir[1] == 0 or old_sign not in '[]':
		if sign == '#':
			move_possible = False
		elif sign == '.':
			move_possible = True
		else:
			move_possible, _ = move_2(_map, new_pos, _dir)

		if move_possible:
			_map[new_pos[1]][new_pos[0]] = _map[pos[1]][pos[0]]
			_map[pos[1]][pos[0]] = '.'
			return True, new_pos
		else:
			return False, pos
	else:
		# we are moving a crate now, and up or down
		positions = []
		if old_sign == ']':
			positions = [(pos[0] - 1, pos[1]), pos]
		else:
			positions = [pos, (pos[0] + 1, pos[1])]
		new_positions = [(p[0] + _dir[0], p[1] + _dir[1]) for p in positions]
		move_possible = False
		if any([_map[p[1]][p[0]] == '#' for p in new_positions]):
			move_possible = False
		elif all([_map[p[1]][p[0]] == '.' for p in new_positions]):
			move_possible = True
		else:
			move_left = possible_to_move_2(_map, new_positions[0], _dir)
			move_right = possible_to_move_2(_map, new_positions[1], _dir)
			move_possible = move_left and move_right
			if move_possible:
				move_2(_map, new_positions[0], _dir)
				move_2(_map, new_positions[1], _dir)

		if move_possible:
			_map[new_positions[0][1]][new_positions[0][0]] = '['
			_map[new_positions[1][1]][new_positions[1][0]] = ']'
			_map[positions[0][1]][positions[0][0]] = '.'
			_map[positions[1][1]][positions[1][0]] = '.'

			return True, None
		else:
			return False, pos

def possible_to_move_2(_map, pos, _dir): # TODO: could be optimized
	new_pos = (pos[0] + _dir[0], pos[1] + _dir[1])
	old_sign = _map[pos[1]][pos[0]]
	sign = _map[new_pos[1]][new_pos[0]]
	move_possible = False
	if old_sign == '.':
		return True
	if old_sign == '#':
		return False
	if _dir[1] == 0 or old_sign not in '[]':
		if sign == '#':
			move_possible = False
		elif sign == '.':
			move_possible = True
		else:
			move_possible = possible_to_move_2(_map, new_pos, _dir)

		return move_possible

	else:
		# we are moving a crate now, and up or down
		positions = []
		if old_sign == ']':
			positions = [(pos[0] - 1, pos[1]), pos]
		else:
			positions = [pos, (pos[0] + 1, pos[1])]
		new_positions = [(p[0] + _dir[0], p[1] + _dir[1]) for p in positions]
		move_possible = False
		if any([_map[p[1]][p[0]] == '#' for p in new_positions]):
			move_possible = False
		elif all([_map[p[1]][p[0]] == '.' for p in new_positions]):
			move_possible = True
		else:
			move_left = possible_to_move_2(_map, new_positions[0], _dir)
			move_right = possible_to_move_2(_map, new_positions[1], _dir)
			move_possible = move_left and move_right
		return move_possible

def get_wider_map(_map):
	result = []
	for line in _map:
		new_line = []
		for sign in line:
			if sign == '.':
				new_line += ['.', '.']
			elif sign == '#':
				new_line += ['#', '#']
			elif sign == '@':
				new_line += ['@', '.']
			else:
				new_line += ['[', ']']
		result.append(new_line)
	return result

def compute_crates_2(_map):
	_sum = 0
	for y, line in enumerate(_map):
		for x, sign in enumerate(line):
			if sign == '[':
				_sum += y*100 + x
	return _sum


print(f'D15 Task 1 answer: {ex1()}')
print(f'D15 Task 2 answer: {ex2()}')