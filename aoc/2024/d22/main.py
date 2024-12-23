import itertools
from collections import defaultdict

with open("data.txt", "r") as f:
	NUMBERS = [int(l.strip()) for l in f.readlines() if l.strip()]

def ex1():
	_sum = 0
	for n in NUMBERS:
		for i in range(2000):
			n = gen_next(n)
		_sum += n
	return _sum 

def ex2():
	best = 0
	bananas = []
	for n in NUMBERS:
		bananas.append(gen_whole_seq(n))
	count_sequences(bananas)
	return max(MEM.values())

def gen_next(secret):
	result = secret << 6
	secret = prune(mix(result, secret))
	result = secret >> 5
	secret = prune(mix(result, secret))
	result = secret << 11
	secret = prune(mix(result, secret))
	return secret

def gen_whole_seq(secret):
	result = [secret]
	for i in range(2000):
		result.append(gen_next(result[-1]))
	vals = [s%10 for s in result]
	changes = [(vals[i+1] - vals[i]) for i in range(len(vals) - 1)]
	return vals[1:], changes

MEM = defaultdict(int)

def count_sequences(bananas):
	for banana, changes in bananas:
		seen = set()
		for i in range(3, len(banana)):
			seq = tuple(changes[i-3:i+1])
			if seq not in seen:
				MEM[seq] += banana[i]
				seen.add(seq)

def mix(n, secret):
	return n ^ secret

def prune(n):
	return n & (2 ** 24 - 1)

print(f'D22 Task 1 answer: {ex1()}')
print(f'D22 Task 2 answer: {ex2()}')