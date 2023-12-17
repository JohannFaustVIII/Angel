from heapq import heappop, heappush

def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(inp):
   return [[int(l) for l in line] for line in inp]

directions = { 0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1)}

def part_1(map, min_steps = 1, max_steps = 3):
   height = len(map)
   width = len(map[0])

   next_points = []
   history = {}
   seen = set()

   start = (0, 0)
   end = (height - 1, width - 1)

   heappush(next_points, (0, start, -1))

   while next_points:
      loss, pos, d = heappop(next_points)

      if pos == end:
         return loss
      
      if (pos, d) in seen:
         continue
      seen.add((pos, d))
      
      dirs = [dir for dir in range(4) if dir != d and (dir + 2) % 4 != d]

      for dir in dirs:
         next_loss = loss
         v = directions[dir]
         ny = pos[0]
         nx = pos[1]
         for i in range(1, max_steps + 1):
            ny += v[0]
            nx += v[1]
            if 0 <= ny < height and 0 <= nx < width:
               next_loss += map[ny][nx]
               if i < min_steps:
                  continue
               np = (ny, nx)
               if next_loss >= history.get((np, dir), 1e100):
                  continue
               if (np, dir) not in history or next_loss < history.get((np, dir)):
                  history[(np, dir)] = next_loss
                  heappush(next_points, (next_loss, np, dir))

def part_2(map):
   return part_1(map, min_steps=4, max_steps=10)

inp = get_input(17)
inp = parse_input(inp)


print(part_1(inp))
print(part_2(inp))