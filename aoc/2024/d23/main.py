import itertools
from collections import defaultdict

CONNECTIONS = defaultdict(list)

with open("data.txt", "r") as f:
	for l in f.readlines():
		left = l[:2]
		right = l[3:5]

		CONNECTIONS[left].append(right)
		CONNECTIONS[right].append(left)


def ex1():
	trios = []
	for k in CONNECTIONS.keys():
		if k[0] != 't':
			continue
		for i, c1 in enumerate(CONNECTIONS[k]):
			for c2 in CONNECTIONS[k][i+1:]:
				if c2 in CONNECTIONS[c1]:
					trio = [k, c1, c2]
					trio.sort()
					trios.append(tuple(trio))

	return len(set(trios))

def ex2():
	largest = []
	visited = []
	isolation_levels = {k: sum([1 for c in CONNECTIONS if c != k and k not in CONNECTIONS[c]]) for k in CONNECTIONS.keys()}
	keys_to_check = list(CONNECTIONS.keys())
	keys_to_check.sort(key = lambda x: CONNECTIONS[x], reverse = True)
	possible_starts = []
	
	for k in keys_to_check:
		is_unique = True
		for c in possible_starts:
			if k in CONNECTIONS[c]:
				is_unique = False
		if is_unique:
			possible_starts.append(k)

	for k in possible_starts:
		big_lan = search_biggest_party([k], k, possible_starts)
		if len(big_lan) > len(largest):
			largest = [o for o in big_lan]
	largest.sort()
	return ','.join(largest)


def search_biggest_party(visited, key, starts):
	largest = [o for o in visited]
	for _next in CONNECTIONS[key]:
		if _next in starts:
			continue
		if _next in visited:
			continue
		if _next in largest:
			continue
		part_of_lan = True
		for v in visited:
			if v not in CONNECTIONS[_next]:
				part_of_lan = False
		if part_of_lan:
			visited.append(_next)
			big_lan = search_biggest_party(visited, _next, starts)
			visited.pop()
			if len(big_lan) > len(largest):
				largest = [o for o in big_lan]
	return largest


print(f'D23 Task 1 answer: {ex1()}')
print(f'D23 Task 2 answer: {ex2()}')