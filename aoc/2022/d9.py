with open("aoc/2022/d9.input") as file:
    lines = file.readlines()

    moves = []

    for line in lines:
        parts = line.strip().split()
        moves.append((parts[0], int(parts[1])))

def part_1(moves : list[tuple[str, int]]) -> int:

    hy, hx = 0, 0
    ty, tx = 0, 0

    move_vectors = {
        "R" : (0, 1),
        "L" : (0, -1),
        "U" : (1, 0),
        "D" : (-1, 0)
    }

    positions = {(0, 0)}

    for move in moves:
        move_vector = move_vectors[move[0]]

        hy += move_vector[0] * move[1]
        hx += move_vector[1] * move[1]

        while abs(ty - hy) > 1 or abs(tx - hx) > 1:
            delta_y = 0 if abs(hy - ty) <= 0 else (hy - ty)/abs(hy - ty)
            delta_x = 0 if abs(hx - tx) <= 0 else (hx - tx)/abs(hx - tx)

            ty += delta_y
            tx += delta_x

            positions.add((ty, tx))

    return len(positions)

def part_2(moves : list[tuple[str, int]]) -> int:

    parts = [[0, 0] for _ in range(10)]

    move_vectors = {
        "R" : (0, 1),
        "L" : (0, -1),
        "U" : (1, 0),
        "D" : (-1, 0)
    }

    positions_9 = {(0, 0)}

    for move in moves:
        move_vector = move_vectors[move[0]]

        for _ in range(move[1]):
            
            parts[0][0] += move_vector[0]
            parts[0][1] += move_vector[1]

            for i in range(9):

                while abs(parts[i][0] - parts[i+1][0]) > 1 or abs(parts[i][1] - parts[i+1][1]) > 1:
                    delta_y = 0 if abs(parts[i][0] - parts[i+1][0]) <= 0 else (parts[i][0] - parts[i+1][0])/abs(parts[i][0] - parts[i+1][0])
                    delta_x = 0 if abs(parts[i][1] - parts[i+1][1]) <= 0 else (parts[i][1] - parts[i+1][1])/abs(parts[i][1] - parts[i+1][1])

                    parts[i+1][0] += delta_y
                    parts[i+1][1] += delta_x

                    if i+1 == 9:
                        positions_9.add((parts[i+1][0], parts[i+1][1]))

    return len(positions_9)


print(part_1(moves))
print(part_2(moves))