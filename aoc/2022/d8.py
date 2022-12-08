from functools import reduce

with open("aoc/2022/d8.input") as file:
    lines = file.readlines()

    forest = [[int(c) for c in line.strip()] for line in lines]

def part1(forest : list[list[int]]):
    count = 0
    vectors = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for my, line in enumerate(forest):
        for mx, tree in enumerate(line):
            for vector in vectors:
                x = mx
                y = my

                while 0 <= x < len(line) and 0 <= y < len(forest):
                    x += vector[0]
                    y += vector[1]

                    if x < 0 or x >= len(line) or y < 0 or y >= len(forest):
                        break

                    if forest[y][x] >= tree:
                        break
                
                if x < 0 or x >= len(line) or y < 0 or y >= len(forest):
                    count += 1
                    break
    
    return count


def part2(forest : list[list[int]]):
    
    vectors = ((0, 1), (0, -1), (1, 0), (-1, 0))
    max_score = 0
    for my, line in enumerate(forest):
        for mx, tree in enumerate(line):

            scores = []
            for vector in vectors:
                x = mx
                y = my
                count = 0

                while 0 <= x < len(line) and 0 <= y < len(forest):
                    x += vector[0]
                    y += vector[1]

                    if x < 0 or x >= len(line) or y < 0 or y >= len(forest):
                        scores.append(count)
                        break
                    
                    count += 1
                    if forest[y][x] >= tree:
                        scores.append(count)
                        break
            
            tree_score = reduce(lambda x,y : x * y, scores, 1)
            if tree_score > max_score:
                max_score = tree_score
    
    return max_score

print(part1(forest))
print(part2(forest))
                 