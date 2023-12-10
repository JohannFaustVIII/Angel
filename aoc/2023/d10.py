def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(inp):
   c_to = {}
   c_from = {}
   start = ()

   vectors = {
      '|' : [(-1, 0), (1, 0)],
      '-' : [(0, -1), (0, 1)],
      'L' : [(-1, 0), (0, 1)],
      'J' : [(-1, 0), (0, -1)],
      '7' : [(1, 0), (0, -1)],
      'F' : [(1, 0), (0, 1)],
      '.' : [],
      'S' : []
   }

   for y, line in enumerate(inp):
      for x, l in enumerate(line):
         p = (y, x)
         for v in vectors[l]:
            np = (y + v[0], x + v[1])

            if p not in c_to:
               c_to[p] = []

            c_to[p].append(np)

            if np not in c_from:
               c_from[np] = []

            c_from[np].append(p)

         if l == 'S':
            start = p
   
   return c_to, c_from, start
         
def part_1_and_2(c_to, c_from, start, input):
   distance = {}

   distance[start] = 0

   next_to_check = []

   for p in c_from[start]:
      distance[p] = 1
      next_to_check.append(p)

   while len(next_to_check) > 0:
      p = next_to_check.pop(0)

      next_val = distance[p] + 1

      if p not in c_to:
         continue

      for np in c_to[p]:
         if p in c_from[np]:
            if np not in distance:
               distance[np] = next_val
               next_to_check.append(np)
            if np in distance and distance[np] > next_val:
               distance[np] = next_val
               next_to_check.append(np)

   result_p1 = max(list(distance.values()))
   
   result_p2 = 0

   pipes = list(distance.keys())
   max_y = max([k[0] for k in list(c_to.keys())]) + 1
   max_x = max([k[1] for k in list(c_to.keys())]) + 1

   closed = []

   hor = [p for p in pipes if input[p[0]][p[1]] == '|']
   up_hor = [p for p in pipes if input[p[0]][p[1]] in ['L', 'J']]

   for y in range(max_y):
      for x in range(max_x):
         p = (y, x)
         if p not in pipes:
            straight = 0
            up_degreed = 0

            for lx in range(0, x):
               if (y, lx) in hor:
                  straight += 1

               if (y, lx) in up_hor:
                  up_degreed += 1

            if up_degreed != 0 and up_degreed % 2 == 1:
               straight += 1

            if straight != 0 and straight % 2 == 1:
               result_p2 += 1
               closed.append(p)

   for y in range(max_y):
      for x in range(max_x):
         p = (y, x)
         if p in pipes:
            print(input[y][x], end='')
         elif p in closed:
            print('$', end='')
         else:
            print('.', end='')
      print('')

   return result_p1, result_p2

inp = get_input(10)
c_to, c_from, start = parse_input(inp)

print(part_1_and_2(c_to, c_from, start, inp))