def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(input):
   moves = tuple([m for m in input[0]])
   ways = dict()

   for line in input[2:]:
      vals = line.split("=")
      start = vals[0].strip()
      roads = vals[1].split(",")
      left = roads[0].strip()[1:]
      right = roads[1].strip()[:-1]

      ways[start] = (left, right)
   
   return moves, ways

def get_way(way):
   return 0 if way == 'L' else 1

def part_1(moves, ways):
   count = 0
   position = 'AAA'

   while position != 'ZZZ':
      index = count % len(moves)
      way = get_way(moves[index])
      position = ways[position][way]

      count += 1

   return count

def lcm(a, b):
   if a > b:
      greater = a
      divider = b
   else:
      greater = b
      divider = a
   
   result = greater

   while (result % divider) != 0:
      result += greater

   return result

def part_2(moves, ways):
   count = 0
   positions = list(filter(lambda s: s[-1] == 'A', ways.keys()))

   steps = []

   for pos in positions:
      start = 0
      offset = 0

      for _ in range(2):

         while pos[-1] != 'Z': # in my case, paths were always to the same end point, so it is version for 'easier' case, sometimes it can go through multiple end points
            index = count % len(moves)
            way = get_way(moves[index])
            count += 1

            pos = ways[pos][way]

         if start == 0:
            start = count

         offset = count - start
         index = count % len(moves)
         way = get_way(moves[index])
         count += 1
         pos = ways[pos][way]

      steps.append((start, offset))

      start = 0
      offset = 0
      count = 0

   paths = [s[0] for s in steps]

   result = 1

   for path in paths: # as start == offset, it works for my case, it requires better solution for complex cases
      result = lcm(result, path)

   return result

input = get_input(8)
moves, ways = parse_input(input)
print(part_1(moves, ways))
print(part_2(moves, ways))