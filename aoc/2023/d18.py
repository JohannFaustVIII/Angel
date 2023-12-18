def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(inp):
   result = []
   for line in inp:
      x = line.split(' ')
      result.append((x[0], int(x[1]), x[2]))
   return result

def part_1(vals):
   y, x = 0, 0
   movement = { 'U' : (-1, 0), 'R' : (0, 1), 'D' : (1, 0), 'L' : (0, -1)}
   history = set()
   directions = {}

   for v in vals:
      vector = movement[v[0]]
      if (y, x) not in directions:
         directions[(y, x)] = v[0]
      else:
         directions[(y, x)] += v[0]
      history.add((y, x))
      for _ in range(v[1]):
         y, x = y + vector[0], x + vector[1]
         if (y, x) not in directions:
            directions[(y, x)] = v[0]
         else:
            if (y, x) == (0, 0):
               directions[(y, x)] = v[0] + directions[(y, x)]
            else:
               directions[(y, x)] += v[0]
         history.add((y, x))         

   ys = [p[0] for p in list(history)]
   xs = [p[1] for p in list(history)]

   min_y = min(ys)
   max_y = max(ys)
   min_x = min(xs)
   max_x = max(xs)

   # for y in range(min_y, max_y + 1):
   #    for x in range(min_x, max_x + 1):
   #       if (y, x) in history:
   #          print('#', end = '')
   #       else:
   #          print('.', end = '')
   #    print('')

   sum = 0
   inside = set()
   for y in range(min_y, max_y + 1):
      for x in range(min_x, max_x + 1):
         if (y,x) in history:
            inside.add((y,x))
            sum += 1
            continue

         left_full = 0
         left_ups = 0

         for dx in range(min_x, x):
            if (y, dx) in directions:
               dirs = directions[(y, dx)]
               if len(dirs) == 1:
                  if dirs in ['U', 'D']:
                     left_full += 1
               else:
                  if dirs in ['RU', 'DL', 'LU', 'DR']:
                     left_ups += 1
         
         if left_ups != 0 and left_ups % 2 == 1:
            left_full += 1

         if left_full % 2 == 1:
            inside.add((y,x))
            sum += 1
   

   # for y in range(min_y, max_y + 1):
   #    for x in range(min_x, max_x + 1):
   #       if (y, x) in inside:
   #          if (y,x) in directions and directions[(y, x)] in ['RU', 'DL', 'LU', 'DR']:
   #             print('$', end = '')
   #          else:
   #             print('#', end = '')
   #       else:
   #          print('.', end = '')
   #    print('')
   return sum

def parse_hex(hex):
   hex = hex[2:-1]
   value = hex[:5]
   direction = hex[5]
   dirs = {'0' : 'R', '1' : 'D', '2' : 'L', '3' : 'U'}
   return (dirs[direction], int(value, 16))

def part_2(vals):
   new_vals = [parse_hex(v[2]) for v in vals]
   return part_1(new_vals)

vals = parse_input(get_input(18))
print(part_1(vals))
print(part_2(vals))