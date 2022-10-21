with open("aoc/2021/d8.input") as file:
    lines = file.readlines()

    input = [(line.strip().split("|")[0].strip().split(), line.strip().split("|")[1].strip().split()) for line in lines]

def part1(input : list[tuple[list[str], list[str]]]) -> int:
    sum = 0
    for numbers, digits in input:
        for digit in digits:
            if len(digit) in [2, 4, 3, 7]:
                sum += 1

    return sum

print(part1(input))

def part2(input : list[tuple[list[str], list[str]]]) -> int:
    sum = 0

    for numbers, digits in input:

        possible_values = {
            "a" : ["a", "b", "c", "d", "e", "f", "g"],
            "b" : ["a", "b", "c", "d", "e", "f", "g"],
            "c" : ["a", "b", "c", "d", "e", "f", "g"],
            "d" : ["a", "b", "c", "d", "e", "f", "g"],
            "e" : ["a", "b", "c", "d", "e", "f", "g"],
            "f" : ["a", "b", "c", "d", "e", "f", "g"],
            "g" : ["a", "b", "c", "d", "e", "f", "g"],
        }

        real_mapping = {}

        order_list = (1, 7, 4, 2, 3, 5, 6, 9, 0, 8)
        
        display_mapping = {
            "a" : [0, 2, 3, 5, 6, 7, 8, 9],
            "b" : [0, 4, 5, 6, 8, 9],
            "c" : [0, 1, 2, 3, 4, 7, 8, 9],
            "d" : [2, 3, 4, 5, 6, 8, 9],
            "e" : [0, 2, 6, 8],
            "f" : [0, 1, 3, 4, 5, 6, 7, 8, 9],
            "g" : [0, 2, 3, 5, 6, 8, 9]
        }

        for number in numbers:
                chars = [n for n in number]
                if len(number) == 2:
                    possible_values["c"] = list(set(chars).intersection(possible_values["c"]))
                    possible_values["f"] = list(set(chars).intersection(possible_values["f"]))
                elif len(number) == 3:
                    possible_values["a"] = list(set(chars).intersection(possible_values["a"]))
                    possible_values["c"] = list(set(chars).intersection(possible_values["c"]))
                    possible_values["f"] = list(set(chars).intersection(possible_values["f"]))
                    pass
                elif len(number) == 4:
                    possible_values["b"] = list(set(chars).intersection(possible_values["b"]))
                    possible_values["c"] = list(set(chars).intersection(possible_values["c"]))
                    possible_values["d"] = list(set(chars).intersection(possible_values["d"]))
                    possible_values["f"] = list(set(chars).intersection(possible_values["f"]))
                    pass
                elif len(number) == 5:
                    possible_values["a"] = list(set(chars).intersection(possible_values["a"]))
                    possible_values["d"] = list(set(chars).intersection(possible_values["d"]))
                    possible_values["g"] = list(set(chars).intersection(possible_values["g"]))
                    pass
                elif len(number) == 6:
                    possible_values["a"] = list(set(chars).intersection(possible_values["a"]))
                    possible_values["b"] = list(set(chars).intersection(possible_values["b"]))
                    possible_values["f"] = list(set(chars).intersection(possible_values["f"]))
                    possible_values["g"] = list(set(chars).intersection(possible_values["g"]))
                    pass
        
                
        while len(real_mapping) != 7:
            for key, value in possible_values.items():
                if len(value) == 1:
                    real_mapping[value[0]] = key
            
            for key, value in real_mapping.items():
                for p_key, p_value in possible_values.items():
                    if key in p_value:
                        p_value.remove(key)
        
        value = 0
        for digit in digits:
            val = [i for i in order_list if all(i in display_mapping[real_mapping[d]] for d in digit)][0]
            value = value*10 + val

        sum += value

    return sum


print(part2(input))