left_list = []
right_list = []

with open("data.txt", "r") as f:
	for f in f.readlines():
		left, right = f.strip().split("   ")
		left_list.append(int(left))
		right_list.append(int(right))

def ex1(left_list, right_list):
	left_list = left_list.copy()
	right_list = right_list.copy()
	left_list.sort()
	right_list.sort()
	sum = 0

	for i in range(len(left_list)):
		sum += abs(right_list[i] - left_list[i])

	return sum

def ex2(left_list, right_list):
	sum = 0
	for i in range(len(left_list)):
		sum += left_list[i] * right_list.count(left_list[i])

	return sum

print(f'D01 Task 1 answer: {ex1(left_list, right_list)}')
print(f'D01 Task 2 answer: {ex2(left_list, right_list)}')
