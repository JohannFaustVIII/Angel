import itertools

with open("data.txt", "r") as f:
	LINES = [l.strip() for l in f.readlines()]

NUMPAD = {"7" : (0,0), "8" : (0, 1), "9" : (0, 2), "4" : (1, 0), "5" : (1, 1), "6" : (1, 2), "1" : (2, 0), "2" : (2, 1), "3" : (2, 2), "0" : (3, 1), "A" : (3,2), None : (3, 0)}
ROBOTPAD = {"^" : (0, 1), "A": (0, 2), "<" : (1, 0), "v" : (1, 1), ">" : (1, 2), None : (0, 0)}

def is_safe(seq, start, wrong_point):
	pad = ROBOTPAD
	none_point = pad[None]
	DIRS = {"^" : (-1, 0), "v" : (1, 0), ">" : (0, 1), "<" : (0, -1)}
	for s in seq:
		start = (start[0] + DIRS[s][0], start[1] + DIRS[s][1])
		if start == wrong_point:
			return False
	return True

def ex1():
	_sum = 0
	for seq in LINES:
		_sum += int(seq[:-1]) * fast_seq(seq, 3)
	return _sum

BIG_MEM = {}

def fast_seq(seq, depth):
	if depth == 26:
		pad = NUMPAD
	else:
		pas = ROBOTPAD
		
	if depth == 0:
		return len(seq)
	if (seq, depth) not in BIG_MEM:
		_sum = 0
		_seq = 'A' + seq
		for i in range(len(_seq) - 1):
			_ns = ""
			dy = pad[_seq[i+1]][0] - pad[_seq[i]][0]
			dx = pad[_seq[i+1]][1] - pad[_seq[i]][1]
			if dy > 0:
				_ns += "v" * dy
			if dy < 0:
				_ns += "^" * abs(dy)
			if dx < 0:
				_ns += "<" * abs(dx)
			if dx > 0:
				_ns += ">" * dx
			best = None
			for p in itertools.permutations(_ns):
				if is_safe(p, pad[_seq[i]], pad[None]):
					_nseq = "".join(p) + "A"
					size = fast_seq(_nseq, depth - 1)
					if best is None or size < best:
						best = size
			_sum += best
		BIG_MEM[(seq, depth)] = _sum
	return BIG_MEM[(seq, depth)]

def ex2():
	_sum = 0
	for seq in LINES:
		_sum += int(seq[:-1]) * fast_seq(seq, 26)
	return _sum

print(f'D21 Task 1 answer: {ex1()}')
print(f'D21 Task 2 answer: {ex2()}')