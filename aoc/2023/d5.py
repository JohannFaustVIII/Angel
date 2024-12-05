def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(input):
   seeds = input[0].split(":")[1].strip()
   seeds = [int(x.strip()) for x in seeds.split(" ")]
   
   maps = []

   for line in input[2:]:
      if line == "":
         maps.append(map)
      elif ":" in line:
         map = []
      else:
         map.append(tuple([int(x) for x in line.split(" ")]))
   maps.append(map)

   return seeds, maps

def map_position(pos, map):
   for m in map:
      if pos in range(m[1], m[1]+m[2]):
         return m[0] + pos - m[1]
   return pos

def map_range(seed_range, map):
   result = []

   start_seed = seed_range[0]
   end_seed = seed_range[0] + seed_range[1] - 1

   for m in map:
      map_start = m[1]
      map_end = m[1] + m[2] - 1
      
      if start_seed >= map_start and start_seed <= map_end:
         # begin inside
         if end_seed <= map_end:
           #end inside too
           result.append((m[0] + start_seed - map_start, seed_range[1]))
           return result
         else:
           # end is outside
           new_range = map_end - start_seed + 1
           next_seed = start_seed + new_range
           result.append((m[0] + start_seed - map_start, new_range))
           result.extend(map_range((next_seed, end_seed - next_seed + 1), map))
           return result
      elif end_seed >= map_start and end_seed <= map_end:
         # begin outside, end inside
         new_range = start_seed - map_start
         result.append((m[0], end_seed - map_start + 1))
         result.extend(map_range((start_seed, map_start - start_seed), map))
         return result
      elif start_seed < map_start and end_seed > map_end:
         # two new ranges then
         left_range = (start_seed, map_start - start_seed)
         right_range = (map_end + 1, end_seed - map_end)
         result.append((m[0], m[2]))
         result.extend(map_range(left_range, map))
         result.extend(map_range(right_range, map))
         return result

   return [seed_range]

def part_1(seeds, maps):
   result = [s for s in seeds]
   for map in maps:
      result = [map_position(s, map) for s in result]
      
   print(result)
   return min(result)

def part_2(seeds, maps):
   seed_ranges = []
   for i in range(0, len(seeds), 2):
      seed_ranges.append((seeds[i], seeds[i+1]))
   for map in maps:
      new_seed_ranges = []
      for s in seed_ranges:
         new_seed_ranges.extend(map_range(s, map))
      seed_ranges = new_seed_ranges
      
   return min([s[0] for s in seed_ranges])

input = get_input(5)

seeds, maps = parse_input(input)

print(part_1(seeds, maps))
print(part_2(seeds, maps))