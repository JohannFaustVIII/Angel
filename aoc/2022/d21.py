with open("aoc/2022/d21.input") as file:
    lines = file.readlines()

    monkeys = {line.strip().split(":")[0] : line.strip().split(":")[1].strip().split() for line in lines}

def part_1(monkeys : dict[str, list[str]]) -> int:
    checked_monkeys = {}
    
    while monkeys:
        if "root" in checked_monkeys.keys():
            return checked_monkeys["root"]
        
        next_monkeys = {}

        for index, value in monkeys.items():
            if len(value) == 1:
                checked_monkeys[index] = int(value[0])
            else:
                var1 = value[0]
                var2 = value[2]
                if var1 in checked_monkeys.keys() and var2 in checked_monkeys.keys():
                    var1 = checked_monkeys[var1]
                    var2 = checked_monkeys[var2]
                    operation = value[1]
                    if operation == "+":
                        value = var1 + var2
                    elif operation == "-":
                        value = var1 - var2
                    elif operation == "*":
                        value = var1 * var2
                    else:
                        value = int(var1/var2)
                    checked_monkeys[index] = value
                else:
                    next_monkeys[index] = value


        monkeys = next_monkeys

    return checked_monkeys["root"]

def get_value(monkeys : dict[str, list[str]], name : str, known : dict = {}) -> int:
    if name == "humn":
        return None
    if name in known.keys():
        return known[name]
    
    index = name
    value = monkeys[name]

    if len(value) == 1:
        known[index] = int(value[0])
    else:
        var1 = value[0]
        var2 = value[2]
        if var1 in known.keys() and var2 in known.keys():
            var1 = known[var1]
            var2 = known[var2]
        else:
            var1 = get_value(monkeys, var1, known)
            var2 = get_value(monkeys, var2, known)
            if var1 is None or var2 is None:
                known[index] = None
                return None
        operation = value[1]
        if operation == "+":
            value = var1 + var2
        elif operation == "-":
            value = var1 - var2
        elif operation == "*":
            value = var1 * var2
        else:
            value = int(var1/var2)
        known[index] = value

    return known[name]


def compute_expected(value : int, monkeys : dict[str, list[str]], name : str, known : dict = {}) -> int:

    if name == "humn":
        return value
    
    left, op, right = monkeys[name]
    left_val = get_value(monkeys, left, known)
    right_val = get_value(monkeys, right, known)

    if left_val is None:
        if op == "+":
            return compute_expected(value - right_val, monkeys, left, known)
        elif op == "-":
            return compute_expected(value + right_val, monkeys, left, known)
        elif op == "*":
            return compute_expected(int(value/right_val), monkeys, left, known)
        else:
            return compute_expected(int(value*right_val), monkeys, left, known)
    else:
        if op == "+":
            return compute_expected(value - left_val, monkeys, right, known)
        elif op == "-":
            return compute_expected(left_val - value, monkeys, right, known)
        elif op == "*":
            return compute_expected(int(value/left_val), monkeys, right, known)
        else:
            return compute_expected(int(left_val/value), monkeys, right, known)


def part_2(monkeys : dict[str, list[str]]) -> int:

    left, _, right = monkeys["root"]

    known = {}
    left_val = get_value(monkeys, left, known)
    right_val = get_value(monkeys, right, known)
    val = left_val if right is None else right_val
    name = right if right is None else left

    return compute_expected(val, monkeys, name, known)

print(part_1(monkeys))
print(part_2(monkeys))