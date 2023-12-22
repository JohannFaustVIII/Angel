def get_input(day: int):
    
  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(inp):
   result = []
   
   for l in inp:
      vals = l.split('~')
      start = tuple([int(v) for v in vals[0].split(',')])
      end = tuple([int(v) for v in vals[1].split(',')])

      result.append((start, end))

   result.sort(key= lambda x: x[0][2])

   return result

def generate_area_map(brick):
   result = []

   for x in range(brick[0][0], brick[1][0] + 1):
      for y in range(brick[0][1], brick[1][1] + 1):
         result.append((x, y))
   
   return tuple(result)

def find_bricks_below(brick, area_map, stable_bricks):
   result = []

   for b in stable_bricks:
      if b[1][2] != brick[0][2] - 1:
         continue
      
      if any([p in b[3] for p in area_map]):
         result.append((b[0], b[1]))

   return result

def part_1(bricks):
   actual_bricks = [] # start, end, below_bricks, area_map

   for b in bricks:
      start = list(b[0])
      end = list(b[1])
      bricks_below = []
      area_map = generate_area_map(b)

      while True:
         if start[2] == 1:
            break
         bricks_below = find_bricks_below((start, end), area_map, actual_bricks)
         if bricks_below:
            break

         start[2] -= 1
         end[2] -= 1
      
      actual_bricks.append((tuple(start), tuple(end), bricks_below, area_map))

   brick_set = set([(b[0], b[1]) for b in actual_bricks])
   constant_bricks = set([b for b in brick_set if any([len(a[2]) == 1 and b in a[2] for a in actual_bricks])])

   part_1_answer = len(brick_set) - len(constant_bricks)

   chain_counter = {}

   reverse_bricks = [b for b in actual_bricks]
   reverse_bricks.reverse()

   for b in reverse_bricks:
      _b = (b[0], b[1])
      if _b not in constant_bricks:
         chain_counter[_b] = [_b]
      else:
         _res = [_b]
         for a in actual_bricks:
            if len(a[2]) > 0 and all([k in _res for k in a[2]]):
               _res.append((a[0], a[1]))
         chain_counter[_b] = list(set(_res))

   part_2_answer = sum([len(v) - 1 for v in chain_counter.values()])

   # print(actual_bricks)
   # for b in actual_bricks:
   #    print(b)

   return part_1_answer, part_2_answer
inp = get_input(22)

bricks = parse_input(inp)

print(part_1(bricks))