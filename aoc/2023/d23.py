def get_input(day: int):
    
  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines


def get_start_and_end(inp):
   start = (0, 1)
   end = (len(inp) - 1, len(inp[0]) - 2)

   return start, end


def get_corner_points(inp):
   directions = ( (-1, 0), (0, 1), (1, 0), (0, -1))

   result = []

   for y, line in enumerate(inp):
      for x, l in enumerate(line):
         if l != '#':
            next = [(y + d[0], x + d[1]) for d in directions if 0 <= y+d[0] < len(inp) and 0 <= x+d[1] < len(inp[0]) and inp[y+d[0]][x+d[1]] != '#']
            if len(next) > 2:
               result.append((y, x))

   return result

def get_path_to_others(start_point, corner_points):
   directions = ( (-1, 0, '^'), (0, 1, '>'), (1, 0, 'v'), (0, -1, '<'))

   next = [(start_point, 0, [start_point])]

   result = {}

   while next:
      n = next.pop(0)
      p = n[0]
      path = n[1]
      visited = n[2]

      if p != start_point and p in corner_points:
         if p not in result:
            result[p] = path
         else:
            result[p] = max(path, result[p])
         continue

      nd = [(p[0] + d[0], p[1] + d[1]) for d in directions if 0 <= p[0]+d[0] < len(inp) and 0 <= p[1]+d[1] < len(inp[0]) and inp[p[0]+d[0]][p[1]+d[1]] in ['.', d[2]]]

      for np in nd:
         if np not in visited:
            next_visited = [v for v in visited]
            next_visited.append(np)
            next.append((np, path + 1, next_visited))

   return result

def find_longest_path(start, end, paths):

   next = []
   next.append((start, 0, [start]))

   result = 0

   while next:
      next.sort(key= lambda x: x[1])
      next.reverse()
      n = next.pop(0)

      point = n[0]
      path = n[1]
      visited = n[2]

      if point == end:
         result = max(result, path)
         continue

      for k in paths[point].keys():
         if k not in visited:
            next_visited = [v for v in visited]
            next_visited.append(k)

            next_path = path + paths[point][k]

            next.append((k, next_path, next_visited))

   return result

def get_path_to_others_p2(start_point, corner_points):
   directions = ( (-1, 0), (0, 1), (1, 0), (0, -1))

   next = [(start_point, 0, [start_point])]

   result = {}

   while next:
      n = next.pop(0)
      p = n[0]
      path = n[1]
      visited = n[2]

      if p != start_point and p in corner_points:
         if p not in result:
            result[p] = path
         else:
            result[p] = max(path, result[p])
         continue

      nd = [(p[0] + d[0], p[1] + d[1]) for d in directions if 0 <= p[0]+d[0] < len(inp) and 0 <= p[1]+d[1] < len(inp[0]) and inp[p[0]+d[0]][p[1]+d[1]] != '#']

      for np in nd:
         if np not in visited:
            next_visited = [v for v in visited]
            next_visited.append(np)
            next.append((np, path + 1, next_visited))

   return result


def part_1(inp):
   start, end = get_start_and_end(inp)

   corner_points = get_corner_points(inp)

   corner_points.append(start)
   corner_points.append(end)

   paths = {}
   for c in corner_points:
      paths[c] = get_path_to_others(c, corner_points)

   return find_longest_path(start, end, paths)

def part_2(inp):
   start, end = get_start_and_end(inp)

   corner_points = get_corner_points(inp)

   corner_points.append(start)
   corner_points.append(end)

   paths = {}
   for c in corner_points:
      paths[c] = get_path_to_others_p2(c, corner_points)

   return find_longest_path(start, end, paths)

inp = get_input(23)

print(part_1(inp))
print(part_2(inp))

# for y, line in enumerate(inp):
#    for x, l in enumerate(line):
#       if (y, x) in corner_points:
#          print("$", end = '')
#       else:
#          print(l, end = '')
#    print('')
