with open("aoc/2021/d1.input") as file:
    lines = file.readlines()
    lines = [int(line) for line in lines]

count = 0

# part 1

for i in range(1, len(lines)):
    if lines[i-1] < lines[i]:
        count += 1

print(count)

# part 2

count = 0

for i in range(0, len(lines) - 3):
    prev = sum(lines[i:i+3])
    next = sum(lines[i+1:i+4])
    if  prev < next:
        count += 1

print(count)