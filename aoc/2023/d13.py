
def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(inp):
   maps = []

   current_map = []
   for l in inp:
      if l == '':
         if len(current_map) > 0:
          maps.append(current_map)
          current_map = []
      else:
         current_map.append(l)
   
   if len(current_map) > 0:
      maps.append(current_map)
   
   return maps
  
def is_correct_mirror(i, lines, max_smudges):   
   left_index = i
   right_index = i + 1
   smudges = 0
   while left_index >= 0 and right_index < len(lines):
      smudges += sum([1 for i in range(len(lines[left_index])) if lines[left_index][i] != lines[right_index][i]])
      if smudges > max_smudges:
         return False
      left_index -= 1
      right_index += 1
   return smudges == max_smudges


def find_mirrors(map, max_smudges):
   vertical_mirror = None

   vertical_lines = [tuple([l[i] for l in map]) for i in range(len(map[0]))]

   for i in range(len(vertical_lines) - 1):
      if is_correct_mirror(i, vertical_lines, max_smudges):
         vertical_mirror = i
         break;

   horizontal_mirror = None

   horizontal_lines = [l for l in map]

   for i in range(len(horizontal_lines) - 1):
      if is_correct_mirror(i, horizontal_lines, max_smudges):
         horizontal_mirror = i
         break;

   return (vertical_mirror, horizontal_mirror)
      
def part_1(maps, max_smudges = 0):
   sum = 0
   for map in maps:
      coords = find_mirrors(map, max_smudges)
      if coords[0] is not None:
         sum += coords[0] + 1
      if coords[1] is not None:
         sum += (coords[1] + 1) * 100
      
   return sum

def part_2(maps):
   return part_1(maps, 1)

inp = get_input(13)
maps = parse_input(inp)

print(part_1(maps))
print(part_2(maps))