import time

ROBOTS = []

with open("data.txt", "r") as f:
	for l in f.readlines():
		left, right = l.strip().split(" ")
		left, right = left[2:], right[2:]
		p = tuple(int(k) for k in left.split(","))
		v = tuple(int(k) for k in right.split(","))
		ROBOTS.append((p, v))

WIDTH = 101
HEIGHT = 103

def ex1():
	TIMES = 100
	new_cords = get_position_after_times(ROBOTS, TIMES)

	middle_x = WIDTH // 2
	middle_y = HEIGHT // 2

	tl = len([r for r in new_cords if r[0] < middle_x and r[1] < middle_y])
	tr = len([r for r in new_cords if r[0] > middle_x and r[1] < middle_y])
	dl = len([r for r in new_cords if r[0] < middle_x and r[1] > middle_y])
	dr = len([r for r in new_cords if r[0] > middle_x and r[1] > middle_y])

	return tl * tr * dl * dr

def get_position_after_times(robots, times):
	new_cords = []
	for r in robots:
		_nx = (r[0][0] + times*r[1][0]) % WIDTH
		_ny = (r[0][1] + times*r[1][1]) % HEIGHT
		new_cords.append((_nx, _ny))
	return new_cords

def ex2():
	i = 0
	while True:
		i += 1
		new_cords = get_position_after_times(ROBOTS, i)
		if len(new_cords) == len(set(new_cords)):
			print(f'Seconds = {i}')
			for y in range(HEIGHT):
				for x in range(WIDTH):
					print('X' if (x, y) in new_cords else '.', end = '')
				print('')
			return i


print(f'D14 Task 1 answer: {ex1()}')
print(f'D14 Task 2 answer: {ex2()}')