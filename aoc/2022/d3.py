with open("aoc/2022/d3.input") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


def part1(lines : list[str]) -> int:
    rucksacks = [[line[:int(len(line)/2)], line[int(len(line)/2):]] for line in lines]

    score = 0

    for rucksack in rucksacks:
        r1 = set(rucksack[0])
        r2 = set(rucksack[1])
        
        elements = list(r1.intersection(r2))

        for element in elements:
            print(element)
            if ord(element) < ord('a'):
                value = ord(element) - ord('A') + 1 + 26
            else:
                value = ord(element) - ord('a') + 1
        
            score += value
    
    return score

def part2(lines : list[str]) -> int:
    score = 0

    for i in range(0, int(len(lines)/3)):

        a,b,c = lines[3*i:3*i+3]
        a,b,c = set(a),set(b),set(c)

        elements = list(a.intersection(b).intersection(c))

        for element in elements:
            if ord(element) < ord('a'):
                value = ord(element) - ord('A') + 1 + 26
            else:
                value = ord(element) - ord('a') + 1
            
            score += value

    return score


    
print(part1(lines))
print(part2(lines))