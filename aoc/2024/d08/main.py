with open("data.txt", "r") as f:
	MAP = [k.strip() for k in f.readlines()]
	ANTENNAS = {}
	for y, line in enumerate(MAP):
		for x, sign in enumerate(line):
			if sign == ".":
				continue
			if sign in ANTENNAS.keys():
				ANTENNAS[sign].append((x, y))
			else:
				ANTENNAS[sign] = [(x, y)]

def ex1():
	antinodes = get_antinodes()
	antinodes = remove_out_of_bounds(antinodes)
	return len(antinodes)

def get_antinodes():
	result = []
	for k, v in ANTENNAS.items():
		for A1 in v:
			for A2 in v:
				if A1 == A2:
					continue
				dx = A1[0] - A2[0]
				dy = A1[1] - A2[1]
				lx = A1[0] + dx
				ly = A1[1] + dy
				rx = A2[0] - dx
				ry = A2[1] - dy
				result.append((lx, ly))
				result.append((rx, ry))
	return result

def remove_out_of_bounds(antinodes):
	return [a for a in set(antinodes) if check_bounds(a)]

def check_bounds(antinode):
	return antinode[0] >= 0 and antinode[0] < len(MAP[0]) and antinode[1] >= 0 and antinode[1] < len(MAP)

def ex2():
	antinodes = get_antinodes_2()
	antinodes = set(antinodes)
	return len(antinodes)

def get_antinodes_2():
	result = []
	for k, v in ANTENNAS.items():
		for A1 in v:
			for A2 in v:
				if A1 == A2:
					continue
				dx = A1[0] - A2[0]
				dy = A1[1] - A2[1]

				pos = (A1[0], A1[1])
				while check_bounds(pos):
					result.append(pos)
					pos = (pos[0] + dx, pos[1] + dy)

				pos = (A2[0], A2[1])
				while check_bounds(pos):
					result.append(pos)
					pos = (pos[0] - dx, pos[1] - dy)
	return result

print(f'D08 Task 1 answer: {ex1()}')
print(f'D08 Task 2 answer: {ex2()}')