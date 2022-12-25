def to_dec(val : str) -> int:
    value = 0
    for v in val:
        next = 0
        if v == "-":
            next = -1
        elif v == "=":
            next = -2
        else:
            next = int(v)
        value = value * 5 + next
    return value

def to_snafu(val : int) -> str:
    parts = []
    position = -1
    while val > 0:
        position += 1
        if position == len(parts):
            parts.append(0)
        parts[position] += val % 5
        val = int(val/5)

        if parts[position] > 2:
            parts[position] -= 5
            parts.append(1)
        
    parts.reverse()

    snafu_val = ""
    for v in parts:
        if v == -2:
            snafu_val += "="
        elif v == -1:
            snafu_val += "-"
        else:
            snafu_val += str(v)
    return snafu_val


with open("aoc/2022/d25.input") as file:
    lines = file.readlines()

    vals = [to_dec(line.strip()) for line in lines]

sum = sum(vals)
print(sum)
print(to_snafu(sum))