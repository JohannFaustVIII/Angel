with open("aoc/2021/d19.input") as file:
    lines = file.readlines()

    scanners = []
    beacons = []

    for line in lines:
        if line.startswith("---"):
            beacons = []
        elif len(line.strip()) == 0:
            scanners.append(beacons)
            beacons = []
        else:
            x, y, z = line.strip().split(",")
            beacons.append((int(x), int(y), int(z)))

    if beacons:
        scanners.append(beacons)

print(scanners)

rotations = [
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, 1),
    (1, -1, -1),
    (-1, 1, 1),
    (-1, 1, -1),
    (-1, -1, 1),
    (-1, -1, -1)
]
positions = [
    (0, 1, 2),
    (0, 2, 1),
    (1, 0, 2),
    (1, 2, 0),
    (2, 1, 0),
    (2, 0, 1)
]

def check_scanner(main_beacons : list[tuple[int, int, int]], beacons_to_check : list[tuple[int, int, int]]):
    for rx, ry, rz in rotations:
        for px, py, pz in positions:
            possible_positions = {}
            for beacon in beacons_to_check:
                x = beacon[0] if px == 0 else beacon[1] if px == 1 else beacon[2]
                y = beacon[0] if py == 0 else beacon[1] if py == 1 else beacon[2]
                z = beacon[0] if pz == 0 else beacon[1] if pz == 1 else beacon[2]

                x *= rx
                y *= ry
                z *= rz

                for main in main_beacons:
                    real_position = (x - main[0], y - main[1], z - main[2])
                    if real_position not in possible_positions:
                        possible_positions[real_position] = 1
                    else:
                        possible_positions[real_position] += 1
            
            for position, count in possible_positions.items():
                if count >= 12:
                    true_beacons = []
                    for beacon in beacons_to_check:
                        x = beacon[0] if px == 0 else beacon[1] if px == 1 else beacon[2]
                        y = beacon[0] if py == 0 else beacon[1] if py == 1 else beacon[2]
                        z = beacon[0] if pz == 0 else beacon[1] if pz == 1 else beacon[2]

                        x *= rx
                        y *= ry
                        z *= rz

                        true_beacons.append((x - position[0], y - position[1], z - position[2]))

                    return True, position, true_beacons

    return False, (), []



def part_1_and_2(scanners : list[tuple[int, int, int]]) -> tuple[int, int]:
    scanners_positions = [(0, 0, 0)]
    found_beacons = []
    found_beacons.extend(scanners[0])
    scanners.pop(0)

    while scanners:
        scanners_to_remove = []
        for index, scanner in enumerate(scanners): 
            correct, true_scanner_position, beacons = check_scanner(found_beacons, scanner)
            if correct:
                for beacon in beacons:
                    if beacon not in found_beacons:
                        found_beacons.append(beacon)
                scanners_positions.append(true_scanner_position)
                scanners_to_remove.append(index)

        scanners_to_remove.reverse()
        for index in scanners_to_remove:
            scanners.pop(index) 

    max = 0

    for scanner_1 in scanners_positions:
        for scanner_2 in scanners_positions:
            x = abs(scanner_1[0] - scanner_2[0])
            y = abs(scanner_1[1] - scanner_2[1])
            z = abs(scanner_1[2] - scanner_2[2])

            length = x + y + z
            if length > max:
                max = length

    return len(found_beacons), max

print(part_1_and_2(scanners))