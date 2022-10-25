with open("aoc/2021/d10.input") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

starting_characters = ["(", "[", "{", "<"]
closing_characters = [")", "]", "}", ">"]

char_points = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

pairs = {
    "(" : ")",
    ")" : "(",
    "[" : "]",
    "]" : "[",
    "{" : "}",
    "}" : "{",
    "<" : ">",
    ">" : "<"
}

def compute_points(line : str) -> int:
    openings = []
    for c in line:
        if c in starting_characters:
            openings.append(c)
        else:
            if c == pairs[openings[-1]]:
                openings.pop()
            else:
                return char_points[c]
    return 0

def part1(lines : list[str]) -> int:
    points = [compute_points(line) for line in lines]
    return sum(points)

def compute_points_2(line : str) -> int:
    openings = []
    for c in line:
        if c in starting_characters:
            openings.append(c)
        else:
            if c == pairs[openings[-1]]:
                openings.pop()
            else:
                return 0
    
    openings.reverse()
    value = 0
    closing_values = {
        ")" : 1,
        "]" : 2,
        "}" : 3,
        ">" : 4
    }
    for opening in openings:
        value *= 5
        value += closing_values[pairs[opening]]
    return value

def part2(lines : list[str]) -> int:
    points = [compute_points_2(line) for line in lines]
    points = [point for point in points if point != 0]
    points.sort()
    return points[int(len(points)/2)]

print(part1(lines))
print(part2(lines))