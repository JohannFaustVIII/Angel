with open("aoc/2022/d6.input") as file:
    line = file.readline()

def part_1(line : str) -> int:
    for i in range(len(line)):
        subline = line[i:i+4]
        list_subline = [s for s in subline]
        set_subline = set(list_subline)
        if len(list_subline) == len(set_subline):
            return i+4

def part_2(line : str) -> int:
    for i in range(len(line)):
        subline = line[i:i+14]
        list_subline = [s for s in subline]
        set_subline = set(list_subline)
        if len(list_subline) == len(set_subline):
            return i+14

print(part_1(line))
print(part_2(line))