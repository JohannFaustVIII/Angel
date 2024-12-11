def add_stone(res, key, val):
	if key in res:
		res[key] += val
	else:
		res[key] = val
	return res

with open("data.txt", "r") as f:
	STONES = [int(s) for s in f.readlines()[0].strip().split(" ")]
	_init = {}
	for s in STONES:
		add_stone(_init, s, 1)
	STONES = _init


def ex1(blinks = 25):
	_actual = STONES
	_next = {}
	for blink in range(blinks):
		_next = get_new_stones(_actual)
		_actual = _next
		_next = {}

	result = 0
	for k,v in _actual.items():
		result += v

	return result

def get_new_stones(_stones):
	_new_stones = {}
	for k, v in _stones.items():
		for item in handle_stone(k):
			add_stone(_new_stones, item, v)

	return _new_stones

def handle_stone(val):
	res = {}
	if val == 0:
		return [1]
	if len(str(val)) % 2 == 0:
		left = int(str(val)[:int(len(str(val))/2)])
		right = int(str(val)[int(len(str(val))/2):])
		return [left, right]
	return [val * 2024]



def ex2():
	return ex1(75)

res = {}


print(f'D11 Task 1 answer: {ex1(25)}')
print(f'D11 Task 2 answer: {ex2()}')