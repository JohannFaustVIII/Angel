from pyparsing import col


with open("aoc/2021/d9.input") as file:
    lines = file.readlines()
    
    values = [[int(i) for i in value] for value in [[c for c in line.strip()] for line in lines]]

def part1(values: list[list[int]]):
    count = 0
    for x, line in enumerate(values):
        for y, value in enumerate(line):
            correct = True
            if x != 0:
                if values[x-1][y] <= value:
                    correct = False
            
            if x != len(values) - 1:
                if values[x+1][y] <= value:
                    correct = False

            if y != 0:
                if values[x][y-1] <= value:
                    correct = False
            
            if y != len(line) - 1:
                if values[x][y+1] <= value:
                    correct = False
            
            if correct:
                count += value + 1

    return count

color_map = [[-1 for _ in line] for line in lines]

def paint_cell(color, x, y, values) -> int:
    if color_map[x][y] != -1:
        return 0
    if values[x][y] == 9:
        color_map[x][y] = 0
        return 0
    color_map[x][y] = color
    size = 1
    if x != 0:
        size += paint_cell(color, x-1, y, values)
            
    if x != len(values) - 1:
        size += paint_cell(color, x+1, y, values)

    if y != 0:
        size += paint_cell(color, x, y-1, values)
            
    if y != len(values[x]) - 1:
        size += paint_cell(color, x, y+1, values)

    return size

def part2(values: list[list[int]]):
    colors = 0

    sizes = []
    for x, line in enumerate(values):
        for y, value in enumerate(line):
            if color_map[x][y] == -1:
                colors += 1
                sizes.append(paint_cell(colors, x, y, values))
            
    
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

print(part1(values))
print(part2(values))