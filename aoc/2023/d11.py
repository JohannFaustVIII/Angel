def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def expand_universe(inp):
   empty_rows = [all([x == '.' for x in l])for l in inp]
   empty_columns = [all([l[i] == '.' for l in inp]) for i in range(len(inp))]

   new_universe = []

   for y, line in enumerate(inp):
      row = []
      for x, l in enumerate(line):
         row.append(l)
         if empty_columns[x]:
            row.append(l)

      new_universe.append(row)
      if empty_rows[y]:
         new_universe.append(row)
   
   return new_universe

def find_galaxies(universe):
   galaxies = []
   for y, line in enumerate(universe):
      for x, l in enumerate(line):
         if l == '#':
            galaxies.append((y, x))
   
   return galaxies


def part_1(inp):
   universe = expand_universe(inp)

   galaxies = find_galaxies(universe)

   sum = 0

   for i, g in enumerate(galaxies):
      for ni in range(i+1, len(galaxies)):
         ng = galaxies[ni]
         sum += abs(g[0] - ng[0]) + abs(g[1] - ng[1])

   return sum

def find_expanded_galaxies(inp):
   empty_rows = [all([x == '.' for x in l])for l in inp]
   empty_columns = [all([l[i] == '.' for l in inp]) for i in range(len(inp))]

   galaxies = []
   for y, line in enumerate(inp):
      for x, l in enumerate(line):
         if l == '#':
            galaxies.append([y, x, y, x])

   increase = 1000000 - 1

   for y, row in enumerate(empty_rows):
      if row:
         for g in galaxies:
            if g[0] > y:
               g[2] += increase
   
   for x, column in enumerate(empty_columns):
      if column:
         for g in galaxies:
            if g[1] > x:
               g[3] += increase

   return [(g[2], g[3]) for g in galaxies]

def part_2(inp):
   galaxies = find_expanded_galaxies(inp)

   sum = 0

   for i, g in enumerate(galaxies):
      for ni in range(i+1, len(galaxies)):
         ng = galaxies[ni]
         sum += abs(g[0] - ng[0]) + abs(g[1] - ng[1])

   return sum

inp = get_input(11)

print(part_1(inp))
print(part_2(inp))