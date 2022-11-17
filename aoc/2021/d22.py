with open("aoc/2021/d22.input") as file:
    lines = file.readlines()

    operations = []

    for line in lines:
        operation, coords = line.strip().split()
        x, y, z = coords.strip().split(",")
        to_range = lambda a : (int(a.split("..")[0].split("=")[1]), int(a.split("..")[1]))
        x = to_range(x)
        y = to_range(y)
        z = to_range(z)

        operations.append((operation, x, y, z))

print(operations)

def is_in_part_1_range(operation : tuple[str, tuple[int, int], tuple[int, int], tuple[int, int]]) -> bool:
    _, x, y, z = operation
    # assumption: bigger area doesn't cover the whole initialization area
    if x[0] < -50 or x[1] > 50:
        return False
    if y[0] < -50 or y[1] > 50:
        return False
    if z[0] < -50 or z[1] > 50:
        return False
    return True

def get_subrange(area_1 : tuple[int, int], area_2 : tuple[int, int]):
    if area_1[1] < area_2[0]:
        return None
    if area_1[0] > area_2[1]:
        return None

    start = max([area_1[0], area_2[0]])
    end = max([area_1[1], area_2[0]])
    start = min([start, area_2[1]])
    end = min([end, area_2[1]])

    return (start, end)

def get_uninterrupted(ranges : list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]], index : int) -> int:
    x, y, z = ranges[index]

    index += 1

    area = (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)

    conflictRanges = []

    if (index < len(ranges)):
        for i in range(index, len(ranges)):
            delta_x = get_subrange(ranges[i][0], x)
            delta_y = get_subrange(ranges[i][1], y)
            delta_z = get_subrange(ranges[i][2], z)

            if delta_x is None or delta_y is None or delta_z is None:
                continue
            
            conflictRanges.append((delta_x, delta_y, delta_z))
    
    if len(conflictRanges) != 0:
        for i in range(0, len(conflictRanges)):
            area -= get_uninterrupted(conflictRanges, i)
    
    return area



def get_turned_on_part_1(operations : list[tuple[str, tuple[int, int], tuple[int, int], tuple[int, int]]]) -> int:
    count = 0

    ranges = [(x, y, z) for _, x, y, z in operations]

    for index, operation in enumerate(operations):
        if operation[0] == "on":
            if is_in_part_1_range(operation):
                count += get_uninterrupted(ranges, index)
        
    return count

def get_turned_on_part_2(operations : list[tuple[str, tuple[int, int], tuple[int, int], tuple[int, int]]]) -> int:
    count = 0

    ranges = [(x, y, z) for _, x, y, z in operations]

    for index, operation in enumerate(operations):
        if operation[0] == "on":
            count += get_uninterrupted(ranges, index)
        
    return count


print(get_turned_on_part_1(operations))
print(get_turned_on_part_2(operations))