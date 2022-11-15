def to_bit(c : str) -> int:
    return 1 if c == "#" else 0

def line_to_bits(line : str) -> list[int]:
    return [to_bit(s) for s in line.strip()]

with open("aoc/2021/d20.input") as file:
    lines = file.readlines()

    algorithm = line_to_bits(lines[0])

    image = [line_to_bits(line) for line in lines[2:]]


def enchance(algorithm : list[int], image : list[list[int]], iterations : int) -> int:
    invisible_pixel = 0

    vectors = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    )

    for _ in range(iterations):
        new_image = []
        for index_y in range(-1, len(image) + 1):
            new_line = []
            for index_x in range(-1, len(image[0]) + 1):
                new_bit_value = ""

                for vector in vectors:
                    y = index_y + vector[0]
                    x = index_x + vector[1]

                    if 0 <= y < len(image) and 0 <= x < len(image[0]):
                        new_bit_value += str(image[y][x])
                    else:
                        new_bit_value += str(invisible_pixel)
                
                bit_value = int(new_bit_value, 2)
                new_line.append(algorithm[bit_value])
            new_image.append(new_line)
        image = new_image

        if invisible_pixel == 0:
            invisible_pixel = algorithm[0]
        else:
            invisible_pixel = algorithm[-1]

    return sum([sum(line) for line in image])

print(enchance(algorithm, image, 2))
print(enchance(algorithm, image, 50))


                