with open("aoc/2022/d16.input") as file:
    lines = file.readlines()

    caves = {}

    for line in lines:
        parts = line.strip().split()
        cave_name = parts[1]
        value = int(parts[4].strip().split("=")[1][:-1])
        next_caves = [cave[0:2] for cave in parts[9:]]

        caves[cave_name] = (value, next_caves)

    cave_to_num = {}

    for cave in caves.keys():
        if cave not in cave_to_num:
            cave_to_num[cave] = 1 << len(cave_to_num)

    new_caves = {}

    for key, item in caves.items():
        print(item)
        print(cave_to_num)
        new_caves[cave_to_num[key]] = (item[0], [cave_to_num[cave] for cave in item[1]])
        
    caves = new_caves

def part_1(caves : dict[int, tuple[int, list[str]]], cave_to_num : dict[str, int]):

    actual_states = [(cave_to_num["AA"], 0, 0)] # cave_num, opened, pressure

    best = {}

    MINUTES = 30

    for i in range(1, MINUTES + 1):
        new_states = []

        for location, opened, pressure in actual_states:
            best_key = (location, opened)

            if best_key in best and pressure <= best[best_key]:
                continue
                
            best[best_key] = pressure

            is_closed = (location & opened) == 0
            flow_rate = caves[location][0]
            if is_closed and flow_rate > 0:
                new_states.append((location, location | opened, flow_rate * (MINUTES - i) + pressure))
            for new_location in caves[location][1]:
                new_states.append((new_location, opened, pressure))
        
        actual_states = new_states

    return max([state[2] for state in actual_states])

def part_2(caves : dict[int, tuple[int, list[str]]], cave_to_num : dict[str, int]):

    actual_states = [(cave_to_num["AA"], cave_to_num["AA"], 0, 0)] # my_location, elephant_location, opened, pressure

    best = {}

    MINUTES = 26

    for i in range(1, MINUTES + 1):
        new_states = []

        # my_move
        for location, elephant, opened, pressure in actual_states:
            is_closed = (location & opened) == 0
            flow_rate = caves[location][0]
            if is_closed and flow_rate > 0:
                open_location = location | opened
                new_pressure = flow_rate * (MINUTES - i) + pressure

                key = (location | elephant, open_location)
                if key in best and new_pressure <= best[key]:
                    continue

                best[key] = new_pressure

                new_states.append((location, elephant, open_location, new_pressure))
            for new_location in caves[location][1]:
                key = (new_location | elephant, opened)
                if key in best and pressure <= best[key]:
                    continue
                best[key] = pressure

                new_states.append((new_location, elephant, opened, pressure))
        
        new_new_states = []

        # elephant_move
        for location, elephant, opened, pressure in new_states:
            is_closed = (elephant & opened) == 0
            flow_rate = caves[elephant][0]
            if is_closed and flow_rate > 0:
                open_location = elephant | opened
                new_pressure = flow_rate * (MINUTES - i) + pressure

                key = (location | elephant, open_location)
                if key in best and new_pressure <= best[key]:
                    continue

                best[key] = new_pressure

                new_new_states.append((location, elephant, open_location, new_pressure))
            for new_location in caves[elephant][1]:
                key = (location | new_location, opened)
                if key in best and pressure <= best[key]:
                    continue
                best[key] = pressure

                new_new_states.append((location, new_location, opened, pressure))

        actual_states = new_new_states

    return max([state[3] for state in actual_states])

print(part_1(caves, cave_to_num))
print(part_2(caves, cave_to_num))