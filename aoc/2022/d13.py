from functools import cmp_to_key

class ValueList():

    def __init__(self, values) -> None:
        self.values = values

    def get_values(self):
        return self.values

class Value(ValueList):

    def __init__(self, value : int) -> None:
        super().__init__([self])
        self.value = value

    def get_value(self):
        return self.value

def parse_line(line : str, start_index : int = 1) -> tuple[ValueList, int]:
    index = start_index

    vals = []
    val = 0
    while line[index] != "]":
        if line[index] == ",":
            pass
        elif line[index] == "[":
            val, index = parse_line(line, index + 1)
            vals.append(val)
        else:
            sub_index = index
            while line[sub_index] not in [",", "[", "]"]:
                sub_index += 1
            vals.append(Value(int(line[index:sub_index])))
            index = sub_index - 1
        index += 1
    
    return ValueList(vals), index

def compare(left : ValueList, right : ValueList) -> bool:
    if isinstance(left, Value) and isinstance(right, Value):
        l_value = left.get_value()
        r_value = right.get_value()

        return True if l_value < r_value else False if r_value < l_value else None
    else:
        l_values = left.get_values()
        r_values = right.get_values()

        for i in range(max(len(l_values), len(r_values))):
            if i >= len(l_values):
                return True
            if i >= len(r_values):
                return False
            comparison = compare(l_values[i], r_values[i])
            if comparison is not None:
                return comparison
    return None

def part_1(pairs : list[tuple[ValueList, ValueList]]) -> int:

    indexes = [index + 1 for index, vals in enumerate(pairs) if compare(vals[0], vals[1])]

    return sum(indexes)

def part_2(pairs : list[tuple[ValueList, ValueList]]) -> int:

    lists = []

    first_packet = ValueList([ValueList([Value(2)])])
    second_packet = ValueList([ValueList([Value(6)])])

    for pair in pairs:
        lists.append(pair[0])
        lists.append(pair[1])

    lists.append(first_packet)
    lists.append(second_packet)

    lists.sort(key = cmp_to_key(lambda x, y : -1 if compare(x, y) == True else 1 if compare(x, y) == False else 0))

    first_index = lists.index(first_packet) + 1
    second_index = lists.index(second_packet) + 1

    return first_index * second_index

with open("aoc/2022/d13.input") as file:
    lines = file.readlines()

    pairs = []

    for i in range(0, len(lines), 3):
        first_value = parse_line(lines[i].strip())[0]
        second_value = parse_line(lines[i+1].strip())[0]

        pairs.append((first_value, second_value))

print(part_1(pairs))
print(part_2(pairs))