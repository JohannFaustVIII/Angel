with open("aoc/2022/d20.input") as file:
    lines = file.readlines()

    numbers = [(int(line.strip()), index) for index, line in enumerate(lines)]

def part_1(numbers : list[tuple[int, int]]) -> int:
    numbers = numbers.copy()

    for i in range(len(numbers)):
        element_to_move = [n for n in numbers if n[1] == i][0]

        actual_index = numbers.index(element_to_move)
        new_index = actual_index + element_to_move[0]
        while new_index < 0:
            new_index += len(numbers) - 1
        while new_index > (len(numbers) - 1):
            new_index -= (len(numbers) - 1)

        if new_index < actual_index:
            numbers.pop(actual_index)
            numbers.insert(new_index, element_to_move)
        elif new_index > actual_index:
            numbers.pop(actual_index)
            if new_index == len(numbers) - 1:
                numbers.append(element_to_move)
            else:
                numbers.insert(new_index, element_to_move)
    
    sum = 0
    element_zero = [n for n in numbers if n[0] == 0][0]
    index_zero = numbers.index(element_zero)


    for i in range(1000, 4000, 1000):
        index = (index_zero + i) % len(numbers)
        sum += numbers[index][0]
    return sum

def part_2(numbers : list[tuple[int, int]], times : int = 1) -> int:
    original_numbers = numbers
    numbers = numbers.copy()
    decrypt_key = 811589153
    numbers = [((n[0] * decrypt_key) % (len(numbers) - 1), n[1]) for n in numbers]
    for _ in range(times):
        for i in range(len(numbers)):
            element_to_move = [n for n in numbers if n[1] == i][0]

            actual_index = numbers.index(element_to_move)
            numbers.pop(actual_index)
            value = element_to_move[0]
            new_index = (actual_index + value) % (len(numbers))
            numbers.insert(new_index, element_to_move)
    
    sum = 0
    element_zero = [n for n in numbers if n[0] == 0][0]
    index_zero = numbers.index(element_zero)


    for i in range(1000, 4000, 1000):
        index = (index_zero + i) % len(numbers)
        element = [n for n in original_numbers if n[1] == numbers[index][1]][0]
        sum += 811589153 * element[0]

    return sum

print(part_1(numbers))
print(part_2(numbers, 10))