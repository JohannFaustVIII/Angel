with open("aoc/2022/d1.input") as file:
    lines = file.readlines()
    
    

def part1(lines : list[str]) -> tuple[int, int]:
    calories = []
    count = 0
    for line in lines:
        line = line.strip()
        if line:
            count += int(line)
        else:
            calories.append(count)
            count = 0

    if count != 0:
        calories.append(count)

    max_calories = max(calories)
    calories.sort()
    max_three = sum(calories[-3:])
    return (max_calories, max_three)

print(part1(lines))