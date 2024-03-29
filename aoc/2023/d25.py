def get_input(day: int):
    
  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(inp):
   result = {l.split(':')[0] : set() for l in inp}

   for line in inp:
      vals = line.split(':')
      main = vals[0]
      others = [v.strip() for v in vals[1].strip().split(' ')]

      for o in others:
         if o not in result.keys():
            result[o] = set()
         result[main].add(o)
         result[o].add(main)
      
   return result

def get_distances(connections):
   distances = {k : {k : 0} for k in connections.keys()}

def part_1(connections):

   first_group = set(connections)
   first_group.remove('spb') # to avoid failing because of removing neighbour node

   count = lambda v: len(connections[v] - first_group)

   while sum(map(count, first_group)) != 3:
      first_group.remove(max(first_group, key=count))

   return len(first_group) * len(set(connections) - first_group)

inp = get_input(25)

connections = parse_input(inp)

print(part_1(connections))