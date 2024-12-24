operation_read = False
VALS = {}
OPERATIONS = {}

with open("data.txt", "r") as f:
	for l in f.readlines():
		l = l.strip()
		if not l:
			operation_read = True
		elif operation_read:
			op, val = l.split("->")
			OPERATIONS[val.strip()] = op.strip().split(" ")
		else:
			VALS[l[:3]] = int(l[-1])

N_VALS = {}
def ex1():
	to_compute = {}
	keys_to_check = [k for k in OPERATIONS.keys() if k[0] == 'z']
	keys_to_check.sort()
	for k in keys_to_check:
		to_compute[k] = compute_key(k)
	return get_from_bin(to_compute)

def compute_key(k):
	if k in VALS:
		return VALS[k]
	if k in N_VALS:
		return N_VALS[k]
	val = 0
	left, op, right = OPERATIONS[k]
	if op == "AND":
		val = compute_key(left) & compute_key(right)
	elif op == "OR":
		val = compute_key(left) | compute_key(right)
	else:
		val = compute_key(left) ^ compute_key(right)
	N_VALS[k] = val
	return val

def get_from_bin(vals):
	_vals = [(k, v) for k, v in vals.items()]
	_vals.sort(key = lambda x : x[0], reverse = True)
	_vals = [str(v[1]) for v in _vals]
	return int(''.join(_vals), 2)

def ex2():
	_zs = [k for k in OPERATIONS.keys() if k[0] == 'z']
	max_z = max([int(k[1:]) for k in _zs])
	max_z = 'z' + str(max_z)


	bad_gates = set()
	ios = ['x', 'y', 'z']
	for k, items in OPERATIONS.items():
		left, op, right = items
		if k[0] == 'z' and op != "XOR"and k != max_z:
			bad_gates.add(k)
		if op == "XOR" and k[0] not in ios and left[0] not in ios and right[0] not in ios:
			bad_gates.add(k)
		if op == "AND" and "x00" not in [left, right]:
			for sk, sitems in OPERATIONS.items():
				sleft, sop, sright = sitems
				if (k == sleft or k == sright) and sop != "OR":
					bad_gates.add(k)
		if op == "XOR":
			for sk, sitems in OPERATIONS.items():
				sleft, sop, sright = sitems
				if (k == sleft or k == sright) and sop == "OR":
					bad_gates.add(k)
	return ','.join(sorted(bad_gates))

print(f'D24 Task 1 answer: {ex1()}')
print(f'D24 Task 2 answer: {ex2()}')