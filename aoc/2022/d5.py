import re

with open("aoc/2022/d5.input") as file:
    lines = file.readlines()

    stacks = []
    moves = []

    for _ in range(int(len(lines[0])/4)):
        stacks.append([])
    
    read_moves = False

    for line in lines:
        if not line.split():
            read_moves = True
        else:
            if not read_moves:
                line = re.findall("."*4+"?", line)
                for index, s in enumerate(line):
                    s = s.strip()
                    if s:
                        if s.startswith("["):
                            stacks[index].append(s[1])
            else:
                line = line.strip().split(" ")
                moves.append((int(line[1]), int(line[3]) - 1, int(line[5]) - 1))
    
    for stack in stacks:
        stack.reverse()
    
    print(stacks)
    print(moves)

def part1(stacks : list[list[str]], moves : list[tuple[int, int, int]]):
    for move in moves:
        quantity = move[0]
        from_stack = move[1]
        to_stack = move[2]

        to_move = stacks[from_stack][-quantity:]
        to_move.reverse()
        del stacks[from_stack][-quantity:]
        stacks[to_stack].extend(to_move)

    for stack in stacks:
        print(stack[-1], end="")
    print("")

def part2(stacks : list[list[str]], moves : list[tuple[int, int, int]]):
    for move in moves:
        quantity = move[0]
        from_stack = move[1]
        to_stack = move[2]

        to_move = stacks[from_stack][-quantity:]
        del stacks[from_stack][-quantity:]
        stacks[to_stack].extend(to_move)

    for stack in stacks:
        print(stack[-1], end="")
    print("")

# use only one of below, both won't work as they operate on the same list
# part1(stacks,moves)
part2(stacks,moves)

