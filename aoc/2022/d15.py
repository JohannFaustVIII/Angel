with open("aoc/2022/d15.input") as file:
    lines = file.readlines()

    positions = []

    for line in lines:
        parts = line.strip().split(":")
        sensor_parts = parts[0].strip().split(",")
        sensor_coords = [int(part.strip().split("=")[1].strip()) for part in sensor_parts]
        sensor = (sensor_coords[0], sensor_coords[1])

        beacon_parts = parts[1].strip().split(",")
        beacon_coords = [int(part.strip().split("=")[1].strip()) for part in beacon_parts]
        beacon = (beacon_coords[0], beacon_coords[1])

        positions.append((sensor, beacon))

print(positions)

def part_1(positions : list[tuple[tuple[int, int], tuple[int, int]]], row : int) -> int:
    occupied = set()

    beacons = [position[1] for position in positions]

    for sensor, beacon in positions:
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        row_distance = abs(sensor[1] - row)
        diff = distance - row_distance

        if diff >= 0:
            for i in range(0, diff + 1):
                occupy = (sensor[0] + i, row)
                if occupy not in beacons:
                    occupied.add(occupy)
                occupy = (sensor[0] - i, row)
                if occupy not in beacons:
                    occupied.add(occupy)

    return len(occupied)

def part_2(positions : list[tuple[tuple[int, int], tuple[int, int]]]) -> tuple[int, int]:

    distances = [abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]) for sensor, beacon in positions]

    vectors = (
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    )

    for index, (sensor, beacon) in enumerate(positions):
        possible_border_beacons = set()
        for i in range(0, distances[index] + 2):
            x_vector = distances[index] + 1 - i
            y_vector = i
            
            for vector in vectors:
                x = sensor[0] + vector[0] * x_vector
                y = sensor[1] + vector[1] * y_vector

                if 0 <= x <= 4000000 and 0 <= y <= 4000000:
                    possible_border_beacons.add((x, y))

        for possible in possible_border_beacons:
        
            is_correct = True

            for c_index, (c_sensor, beacon) in enumerate(positions):
                if c_index == index:
                    continue
                distance = abs(c_sensor[0] - possible[0]) + abs(c_sensor[1] - possible[1])
                if distance < distances[c_index]:
                    is_correct = False
                    break

            if is_correct:
                return possible, possible[0] * 4000000 + possible[1]
        

    pass

# both can be optimized, probably

# print(part_1(positions, 2000000))
print(part_2(positions))
