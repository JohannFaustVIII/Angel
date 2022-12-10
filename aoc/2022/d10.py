with open("aoc/2022/d10.input") as file:
    lines = file.readlines()

    instructions = []

    for line in lines:
        parts = line.strip().split()
        instructions.append(parts)

def part_1(instructions: list[list[str]]) -> int:
    x = 1
    cycle = 1
    check_points = [20, 60, 100, 140, 180, 220]
    sum = 0

    for inst in instructions:
        move = inst[0]
        if move == "noop":
            if cycle in check_points:
                sum += x * cycle
            cycle += 1
        else:
            value = int(inst[1])
            for _ in range(2):
                if cycle in check_points:
                    sum += x * cycle
                cycle += 1
            x += value

    return sum

def part_2(instructions: list[list[str]]) -> int:
    x = 1
    cycle = 1

    for inst in instructions:
        move = inst[0]
        if cycle % 40 == 1:
            print("")

        if move == "noop":
            if abs(x - ((cycle - 1) % 40)) <= 1:
                print("#", end="")
            else:
                print(".", end="")
            cycle += 1
        else:
            for i in range(2):
                # if (cycle < 15):
                #     print(cycle, x, abs(x - (cycle % 40)))
                if abs(x - ((cycle - 1)% 40)) <= 1:
                    print("#", end="")
                else:
                    print(".", end="")
                if i == 1:
                    value = int(inst[1])
                    x += value
                cycle += 1
                if i == 0 and cycle % 40 == 1:
                    print("")
print(part_1(instructions))
part_2(instructions)