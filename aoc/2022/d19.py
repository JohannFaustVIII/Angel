#requires more optimization

import math

with open("aoc/2022/d19.input") as file:
    lines = file.readlines()

    blueprints = []

    for line in lines:
        parts = line.strip().split()
        ore_robot_cost = int(parts[6])
        clay_robot_cost = int(parts[12])
        obsidian_robot_cost = (int(parts[18]), int(parts[21]))
        geode_robot_cost = (int(parts[27]), int(parts[30]))

        blueprints.append((ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost))

def max_geodes(max_turns : int, blueprint : tuple[int, int, tuple[int, int], tuple[int, int]], state : tuple[int, int, int, int, int, int, int, int], turn : int = 0, best : int = 0) -> int:
    bests = [best]

    ore_robots = state[0]
    ore = state[1]
    clay_robots = state[2]
    clay = state[3]
    obsidiation_robots = state[4]
    obsidian = state[5]
    geode_robots = state[6]
    geode = state[7]

    ore_robot_cost = blueprint[0]
    clay_robot_cost = blueprint[1]
    obsidian_robot_cost = blueprint[2]
    geode_robot_cost = blueprint[3]

    max_ore = max(clay_robot_cost, obsidian_robot_cost[0], geode_robot_cost[1])
    max_clay = obsidian_robot_cost[1]
    max_obsidian = geode_robot_cost[1]
    
    if turn >= max_turns:
        return best

    achievable_best = geode
    sim_turn = turn
    sim_robots = geode_robots
    while sim_turn < max_turns:
        achievable_best += sim_robots
        sim_robots += 1
        sim_turn += 1

    if achievable_best <= best:
        return best


    # wait for new geode robot
    if ore_robots > 0 and obsidiation_robots > 0:
        turns_to_gather_ore = math.ceil((geode_robot_cost[0] - ore)/ore_robots) + 1
        if turns_to_gather_ore <= 0:
            turns_to_gather_ore = 1
        turns_to_gather_obsidian = math.ceil((geode_robot_cost[1] - obsidian)/obsidiation_robots) + 1
        if turns_to_gather_obsidian <= 0:
            turns_to_gather_obsidian = 1
        delta = max(turns_to_gather_ore, turns_to_gather_obsidian)
        if turn + delta >= max_turns:
            bests.append(geode + (max_turns - turn) * geode_robots)
        else:
            next_state = (
                ore_robots, 
                ore + delta * ore_robots - geode_robot_cost[0], 
                clay_robots, 
                clay + delta * clay_robots, 
                obsidiation_robots, 
                obsidian + delta * obsidiation_robots - geode_robot_cost[1],
                geode_robots + 1,
                geode + delta * geode_robots)
            bests.append(max_geodes(max_turns, blueprint, next_state, turn + delta, best))
    
    best = max(bests)

    # wait for new obsidian robot
    if ore_robots > 0 and clay_robots > 0 and obsidiation_robots < max_obsidian:
        turns_to_gather_ore = math.ceil((obsidian_robot_cost[0] - ore)/ore_robots) + 1
        if turns_to_gather_ore <= 0:
            turns_to_gather_ore = 1
        turns_to_gather_clay = math.ceil((obsidian_robot_cost[1] - clay)/clay_robots) + 1
        if turns_to_gather_clay <= 0:
            turns_to_gather_clay = 1
        delta = max(turns_to_gather_ore, turns_to_gather_clay)
        if turn + delta >= max_turns:
            bests.append(geode + (max_turns - turn) * geode_robots)
        else:
            next_state = (
                ore_robots, 
                ore + delta * ore_robots - obsidian_robot_cost[0], 
                clay_robots, 
                clay + delta * clay_robots - obsidian_robot_cost[1], 
                obsidiation_robots + 1, 
                obsidian + delta * obsidiation_robots,
                geode_robots,
                geode + delta * geode_robots)
            bests.append(max_geodes(max_turns, blueprint, next_state, turn + delta, best))

    best = max(bests)

    # wait for new clay robot
    if ore_robots > 0 and clay_robots < max_clay:
        delta = math.ceil((clay_robot_cost - ore)/ore_robots) + 1
        if delta <= 0:
            delta = 1
        if turn + delta >= max_turns:
            bests.append(geode + (max_turns - turn) * geode_robots)
        else:
            next_state = (
                ore_robots, 
                ore + delta * ore_robots - clay_robot_cost, 
                clay_robots + 1, 
                clay + delta * clay_robots, 
                obsidiation_robots, 
                obsidian + delta * obsidiation_robots,
                geode_robots,
                geode + delta * geode_robots)
            bests.append(max_geodes(max_turns, blueprint, next_state, turn + delta, best))

    best = max(bests)

    # wait for new ore robot
    if ore_robots > 0 and ore_robots < max_ore and turn < max_turns-2:
        delta = math.ceil((ore_robot_cost - ore)/ore_robots) + 1
        if delta <= 0:
            delta = 1
        if turn + delta >= max_turns:
            bests.append(geode + (max_turns - turn) * geode_robots)
        else:
            next_state = (
                ore_robots + 1, 
                ore + delta * ore_robots - ore_robot_cost, 
                clay_robots, 
                clay + delta * clay_robots, 
                obsidiation_robots, 
                obsidian + delta * obsidiation_robots,
                geode_robots,
                geode + delta * geode_robots)
            bests.append(max_geodes(max_turns, blueprint, next_state, turn + delta, best))

    return max(bests)

def part_1(blueprints : list[tuple[int, int, tuple[int, int], tuple[int, int]]]) -> int:

    counter = 0
    sum = 0
    TURNS = 24
    for blueprint in blueprints:
        counter += 1
        geodes = max_geodes(TURNS, blueprint, (1, 0, 0, 0, 0, 0, 0, 0))
        sum += counter * geodes
    return sum

def part_2(blueprints : list[tuple[int, int, tuple[int, int], tuple[int, int]]]) -> int:

    TURNS = 32
    mult = 1
    for blueprint in blueprints[0:3]:
        geodes = max_geodes(TURNS, blueprint, (1, 0, 0, 0, 0, 0, 0, 0))
        mult *= geodes
    return mult

print(part_1(blueprints))
print(part_2(blueprints))