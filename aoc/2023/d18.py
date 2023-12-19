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

def draw_lines(vals):
   y = 0
   x = 0
   lines = []

   for v in vals:
      d = v[0]
      length = v[1]

      if d in ['U', 'D']:
         y += length * (-1 if d == 'U' else 1)
      else:
         start_x = x
         x += length * (-1 if d == 'L' else 1)

         left_side = min(start_x, x)
         right_side = max(start_x, x)

         lines.append((left_side, right_side, y))
   
   return lines

def compute_area(lines):
   min_x = min([l[0] for l in lines])
   max_x = max([l[1] for l in lines])

   max_y = max([l[2] for l in lines])

   lines.sort(key = lambda line: line[2])

   added_areas = []

   result = 0

   for line in lines:
      start_x = line[0]
      end_x = line[1]
      y = line[2]

      negative = False

      for i, a in enumerate(added_areas):
         if a[0] <= start_x < a[1]:
            negative = True

            left_border_exists = a[0] != start_x
            right_border_exists = a[1] != end_x

            area = (end_x - start_x + 1 - (1 if left_border_exists else 0) - (1 if right_border_exists else 0)) * (max_y - y)

            result -= area

            added_areas.pop(i)

            if left_border_exists or right_border_exists:
               if left_border_exists:
                  added_areas.append((a[0], start_x))
               if right_border_exists:
                  added_areas.append((end_x, a[1]))
            break

      if not negative:
         left_border_exists = False
         right_border_exists = False

         for a in added_areas:
            if a[1] == start_x:
               left_border_exists = True
            if a[0] == end_x:
               right_border_exists = True

         area = (end_x - start_x + 1 - (1 if left_border_exists else 0) - (1 if right_border_exists else 0)) * (max_y - y + 1)
         result += area

         left_side = start_x
         right_side = end_x

         if left_border_exists:
            for i, a in enumerate(added_areas):
               if a[1] == start_x:
                  added_areas.pop(i)
                  left_side = a[0]
                  break

         if right_border_exists:
            for i, a in enumerate(added_areas):
               if a[0] == end_x:
                  added_areas.pop(i)
                  right_side = a[1]
                  break

         added_areas.append((left_side, right_side))

   return result


def part_1(vals):
   lines = draw_lines(vals)
   result = compute_area(lines)

   return result   

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