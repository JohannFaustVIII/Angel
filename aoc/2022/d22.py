with open("aoc/2022/d22.input") as file:
    lines = file.readlines()

    is_moving = False

    maze = []
    moves = []

    for line in lines:
        if is_moving:
            line = line.strip()
            value = 0
            for c in line:
                if c.isnumeric():
                    value = 10*value + int(c)
                else:
                    moves.append(value)
                    moves.append(c)
                    value = 0
            moves.append(value)
        else:
            if not line.strip():
                is_moving = True
            else:
                line = [-1 if len(p.strip()) == 0 else 1 if p == "#" else 0 for p in line]
                maze.append(line)

def part_1(maze: list[list[int]], moves : list) -> int:
    position = (0, 0) # y, x
    facing = 0

    face_vectors = {
        0: (0, 1),
        1: (1, 0),
        2 : (0, -1),
        3 : (-1, 0)
    }

    for index, p in enumerate(maze[0]):
        if p != -1:
            position = (0, index)
            break

    for move in moves:
        if isinstance(move, int):
            for _ in range(move):
                vector = face_vectors[facing]
                next_y = position[0] + vector[0]
                next_x = position[1] + vector[1]
                if next_y < 0 or next_y >= len(maze) or next_x < 0 or next_x >= len(maze[next_y]) or maze[next_y][next_x] == -1:
                    
                    while True:
                        previous_y = next_y - vector[0]
                        previous_x = next_x - vector[1]
                        if previous_y < 0 or previous_y >= len(maze) or previous_x < 0 or previous_x >= len(maze[previous_y]) or maze[previous_y][previous_x] == -1:
                            break
                        else:
                            next_y = previous_y
                            next_x = previous_x
                if maze[next_y][next_x] == 1:
                    break
                else:
                    position = (next_y, next_x)
        else:
            if move == "R":
                facing += 1
                facing %= 4
            else:
                facing += 3
                facing %= 4

    return 1000 * (position[0] + 1) + 4 * (position[1] + 1) + facing

def part_2(maze: list[list[int]], moves : list) -> int:
    position = (0, 50) # y, x
    facing = 0

    for index, p in enumerate(maze[0]):
        if p != -1:
            position = (0, index)
            break

    face_vectors = {
        0: (0, 1),
        1: (1, 0),
        2 : (0, -1),
        3 : (-1, 0)
    }

    sectors = set()
    sector_connections = {}

    for i in range(0, len(maze), 50):
        for j in range(0, len(maze[i]), 50):
            if maze[i][j] != -1:
                sectors.add((i, j))
                sector_connections[(i, j)] = {}

    connect_vectors = {
        0 : (0, 50),
        1 : (50, 0),
        2 : (0, -50),
        3 : (-50, 0)
    }

    for sector in sectors:
        for face, vec in connect_vectors.items():
            n_y = sector[0] + vec[0]
            n_x = sector[1] + vec[1]
            if (n_y, n_x) in sectors:
                sector_connections[sector][face] = ((n_y, n_x), face)

    while any([len(connects) != 4 for _, connects in sector_connections.items()]):
        for sector in sectors:
            if len(sector_connections[sector]) != 4:
                for i in range(4):
                    if i not in sector_connections[sector].keys():
                        if (i+1)%4 in sector_connections[sector].keys():
                            next_sector, next_face = sector_connections[sector][(i+1)%4]
                            if (next_face+3)%4 in sector_connections[next_sector].keys():
                                next_sector, next_face = sector_connections[next_sector][(next_face+3)%4]
                                next_face = (next_face+3)%4

                                sector_connections[next_sector][next_face] = sector, (i+2)%4
                                sector_connections[sector][i] = next_sector, (next_face+2)%4

                        if (i+3)%4 in sector_connections[sector].keys():
                            next_sector, next_face = sector_connections[sector][(i+3)%4]
                            if (next_face+1)%4 in sector_connections[next_sector].keys():
                                next_sector, next_face = sector_connections[next_sector][(next_face+1)%4]
                                next_face = (next_face+1)%4

                                sector_connections[next_sector][next_face] = sector, (i+2)%4
                                sector_connections[sector][i] = next_sector, (next_face+2)%4

    def get_sector(coords : tuple[int, int]) -> tuple[int, int]:
        y = coords[0]
        x = coords[1]
        c_y = 0
        c_x = 0

        while y >= 50:
            y -= 50
            c_y += 1
        while x >= 50:
            x -= 50
            c_x += 1

        return (50*c_y, 50*c_x)

    transitions = {
        0 : {
            0 : lambda osy, osx, nsy, nsx, x, y: (nsy + (y - osy), nsx),
            1 : lambda osy, osx, nsy, nsx, x, y: (nsy, nsx + 49 - (y - osy)),
            2 : lambda osy, osx, nsy, nsx, x, y: (nsy + 49 - (y - osy),nsx + 49),
            3 : lambda osy, osx, nsy, nsx, x, y: (nsy + 49,nsx + y - osy), 
        },
        1 : {
            0 : lambda osy, osx, nsy, nsx, x, y: (nsy + 49 - (x - osx), nsx),
            1 : lambda osy, osx, nsy, nsx, x, y: (nsy, nsx + (x - osx)),
            2 : lambda osy, osx, nsy, nsx, x, y: (nsy + x - osx, nsx + 49),
            3 : lambda osy, osx, nsy, nsx, x, y: (nsy + 49, nsx + 49 - (x - osx))
        },
        2 : {
            0 : lambda osy, osx, nsy, nsx, x, y: (nsy + 49 - (y - osy), nsx),
            1 : lambda osy, osx, nsy, nsx, x, y: (nsy, nsx + y - osy),
            2 : lambda osy, osx, nsy, nsx, x, y: (nsy + (y - osy), nsx + 49),
            3 : lambda osy, osx, nsy, nsx, x, y: (nsy + 49, nsx + 49 - (y - osy))
        },
        3 : {
            0 : lambda osy, osx, nsy, nsx, x, y: (nsy + x - osx, nsx),
            1 : lambda osy, osx, nsy, nsx, x, y: (nsy, nsx + 49 - (x - osx)),
            2 : lambda osy, osx, nsy, nsx, x, y: (nsy + 49 - (x - osx), nsx + 49),
            3 : lambda osy, osx, nsy, nsx, x, y: (nsy + 49, nsx + (x - osx))
        }
    }

    for move in moves:
        if isinstance(move, int):
            for _ in range(move):
                vector = face_vectors[facing]
                next_y = position[0] + vector[0]
                next_x = position[1] + vector[1]
                if next_y < 0 or next_y >= len(maze) or next_x < 0 or next_x >= len(maze[next_y]) or maze[next_y][next_x] == -1:
                    sector = get_sector(position)
                    new_sector, new_facing = sector_connections[sector][facing]

                    pos = transitions[facing][new_facing](sector[0], sector[1], new_sector[0], new_sector[1], position[1], position[0])

                    next_y = pos[0]
                    next_x = pos[1]
                    facing = new_facing

                if maze[next_y][next_x] == 1:
                    break
                else:
                    position = (next_y, next_x)
        else:
            if move == "R":
                facing += 1
                facing %= 4
            else:
                facing += 3
                facing %= 4

    return 1000 * (position[0] + 1) + 4 * (position[1] + 1) + facing

print(part_1(maze, moves))
print(part_2(maze, moves))