from functools import reduce

with open("aoc/2022/d11.input") as file:
    lines = file.readlines()

    monkeys = []

    for i in range(0, len(lines), 7):
        
        start_items = [int(item.strip()) for item in lines[i+1].strip().split(":")[1].strip().split(",")]
        operation = [item.strip() for item in lines[i+2].strip().split("=")[1].strip().split()]
        division = int(lines[i+3].strip().split()[3].strip())
        condition = {line.strip().split()[1][:-1]:int(line.strip().split()[5]) for line in lines[i+4:i+6]}
        
        monkeys.append((start_items, operation, division, condition))
    
def part_1(monkeys : list[tuple[list[int], list[str], int, dict[str, int]]]) -> int:
    checks = [0 for _ in range(len(monkeys))]
    
    for turn in range(20):
        
        for index, monkey in enumerate(monkeys):
            for item in monkey[0]:
                checks[index] += 1
                part1 = item if monkey[1][0] == "old" else int(monkey[1][0])
                part2 = item if monkey[1][2] == "old" else int(monkey[1][2])
                new_value = part1*part2 if monkey[1][1] == "*" else part1+part2
                
                new_value = int(new_value/3)
                if new_value % monkey[2] == 0:
                    monkeys[monkey[3]["true"]][0].append(new_value)
                else:
                    monkeys[monkey[3]["false"]][0].append(new_value)
            monkey[0].clear()

    checks.sort(reverse=True)    
    return(checks[0]*checks[1])
    
def part_2_diff(monkeys : list[tuple[list[int], list[str], int, dict[str, int]]]) -> int:
    reduce_number = reduce(lambda x,y : x*y, [monkey[2] for monkey in monkeys], 1)

    checks = [0 for _ in range(len(monkeys))]

    for index, monkey in enumerate(monkeys):
        for item in monkey[0]:
            turn = 0
            process_index = index
            while turn < 10000:
                checks[process_index] += 1
                part1 = item if monkeys[process_index][1][0] == "old" else int(monkeys[process_index][1][0])
                part2 = item if monkeys[process_index][1][2] == "old" else int(monkeys[process_index][1][2])
                new_value = part1*part2 if monkeys[process_index][1][1] == "*" else part1+part2
                
                if new_value % monkeys[process_index][2] == 0:
                    new_index = monkeys[process_index][3]["true"]
                else:
                    new_index = monkeys[process_index][3]["false"]

                if new_index < process_index:
                    turn += 1

                process_index = new_index
                item = new_value % reduce_number

    checks.sort(reverse=True)    
    return(checks[0]*checks[1])
                

# print(part_1(monkeys))
print(part_2_diff(monkeys))