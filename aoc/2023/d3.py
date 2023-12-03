
def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def make_maps(input):
  neigh_map = []
  symbol_positions = []

  for y, line in enumerate(input):
    n_line = []
    for x, l in enumerate(line):
      if l.isnumeric():
        n_line.append(1)
      elif l == '.':
        n_line.append(0)
      else:
        n_line.append(2)
        symbol_positions.append((y,x))
    neigh_map.append(n_line)
  
  return (neigh_map, symbol_positions)

def parse_n_map(n_map, positions):
  vectors = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))

  while len(positions) > 0:
    y, x = positions.pop(0)

    for o_y, o_x in vectors:
      d_y = y + o_y
      d_x = x + o_x

      if d_y >= 0 and d_y < len(n_map) and d_x >= 0 and d_x < len(n_map[0]):
        if n_map[d_y][d_x] == 1:
          n_map[d_y][d_x] = 2
          positions.append((d_y, d_x))
  
  return n_map


def part_1(input) -> int:
  n_map, positions = make_maps(input)
  real_n_map = parse_n_map(n_map, positions)

  val = 0
  sum = 0
  for y, line in enumerate(input):
    for x, l in enumerate(line):
      if l.isnumeric() and real_n_map[y][x] == 2:
        val = val * 10 + int(l)
      else:
        sum += val
        val = 0
  
  return sum


def part_2(input) -> int:
  n_map, positions = make_maps(input)
  real_n_map = parse_n_map(n_map, positions)

  val = 0
  prev = []
  vals = []
  for y, line in enumerate(input):
    val_line = []
    for x, l in enumerate(line):
      if l.isnumeric() and real_n_map[y][x] == 2:
        val = val * 10 + int(l)
        prev.append((y, x))
      else:
        for py, px in prev:
          val_line.append(val)
        val = 0
        prev = []
        val_line.append(val)
    
    if len(prev) > 0:
      for py, px in prev:
        val_line.append(val)
      val = 0
      prev = []

    vals.append(val_line)
  
  result = 0
  # up_vector = ((1, 1), (1, 0), (1, -1))
  # middle_vector = ((0, 1), (0, -1))
  # down_vector = ((-1, 1), (-1, 0), (-1, -1))
  vectors = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))
  for y, line in enumerate(input):
    for x, l in enumerate(line):
      if l == '*':
        count = 0
        middle_sum = 0
        numbers = set()

        for vy, vx in vectors:
          d_y = y + vy
          d_x = x + vx
          if d_y >= 0 and d_y < len(n_map) and d_x >= 0 and d_x < len(n_map[0]):
            if vals[d_y][d_x] != 0:
              numbers.add(vals[d_y][d_x]) # assumption: no repeating numbers

        numbers = list(numbers)

        if len(numbers) == 2:
          result += numbers[0]*numbers[1]


  return result

input = get_input(3)

print(part_1(input))
print(part_2(input))