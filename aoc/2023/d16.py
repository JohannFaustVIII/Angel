def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def part_1(map, start = (0, 0, 1)):
   movement = { 0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1)}
   obstacles = {
      '.' : {
         0 : [0],
         1 : [1],
         2 : [2],
         3 : [3]
      },
      '-' : {
         0: [1, 3],
         1: [1],
         2: [1, 3],
         3: [3]
      },
      '|' : {
         0 : [0],
         1 : [0, 2],
         2 : [2],
         3 : [0, 2]
      },
      '/' : {
          0 : [1],
          1 : [0],
          2 : [3],
          3 : [2]
      },
      '\\' : {
         0 : [3],
         1 : [2],
         2 : [1],
         3 : [0]
      }
   }

   history = []
   current = [start]

   while len(current) > 0:
      c = current.pop(0)

      if c in history:
         continue
      if not(-1 < c[0] < len(map) and -1 < c[1] < len(map[0])):
         continue

      obs = map[c[0]][c[1]]
      for direction in obstacles[obs][c[2]]:
         move = movement[direction]
         new_y = c[0] + move[0]
         new_x = c[1] + move[1]
         next = (new_y, new_x, direction)
         current.append(next)

      history.append(c)

   result = len(set([(x[0], x[1]) for x in history]))
   return result

def part_2(map):
   results = []

   for x in range(len(map[0])):
      results.append(part_1(map, start=(0, x, 2)))
      results.append(part_1(map, start=(len(map) - 1, x, 0)))
   
   for y in range(len(map)):
      results.append(part_1(map, start=(y, 0, 1)))
      results.append(part_1(map, start=(y, len(map[0])-1, 3)))

   return max(results)

inp = get_input(16)
print(part_1(inp))
print(part_2(inp))