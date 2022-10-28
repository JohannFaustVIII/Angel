with open("aoc/2021/d13.input") as file:
    lines = file.readlines()

    dots = []
    folds = []

    read_dots = True
    for line in lines:
        if not line.strip():
            read_dots = False
        else:
            if read_dots:
                x, y = line.strip().split(",")
                dots.append([int(x), int(y)])
            else:
                axis, index = line.strip().split(" ")[2].split("=")
                folds.append((axis, int(index)))

def part1(dots : list[list[int]], folds : list[tuple], number_of_folds : int) -> int:
    for i in range(number_of_folds):
        fold = folds[i]
        axis = fold[0]
        index = fold[1]
        for dot in dots:
            if axis == "x":
                dot[0] = index - abs(index - dot[0])
            else:
                dot[1] = index - abs(index - dot[1])
    return len(set([(dot[0], dot[1]) for dot in dots]))

def part2(dots : list[list[int]], folds : list[tuple]) -> int:
    for fold in folds:
        axis = fold[0]
        index = fold[1]
        for dot in dots:
            if axis == "x":
                dot[0] = index - abs(index - dot[0])
            else:
                dot[1] = index - abs(index - dot[1])

    max_x = max([dot[0] for dot in dots]) + 1
    max_y = max([dot[1] for dot in dots]) + 1

    dots = set([(dot[0], dot[1]) for dot in dots])

    for y in range(max_y):
        for x in range(max_x):
            if (x, y) in dots:
                print("#", end="")
            else:
                print(".", end="")
        print()



print(part1(dots,folds, 1))
part2(dots,folds)