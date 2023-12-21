def get_input(day: int):
    
  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def get_starting_set(inp):
   result = [[(y, x) for x, k in enumerate(l) if k == 'S'] for y, l in enumerate(inp)]
   result = [l for l in result if l]
   result = result[0]
   return set(result)

def is_valid(step):
   height = len(inp)
   width = len(inp[0])

   return 0 <= step[0] < height and 0 <= step[1] < width

def is_empty_slot(step):
   return inp[step[0]][step[1]] != '#'

def move(step):
   directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

   result = [(step[0] + d[0], step[1] + d[1]) for d in directions if is_valid((step[0] + d[0], step[1] + d[1])) and is_empty_slot((step[0] + d[0], step[1] + d[1]))]

   return result


def make_next_steps(steps):
   result = [move(step) for step in steps]
   result = [item for sublist in result for item in sublist]
   return set(result)


def part_1(inp):

   steps = get_starting_set(inp)

   for i in range(64):
      steps = make_next_steps(steps)
   return len(steps)

def generate_correct_position(step):
   height = len(inp)
   width = len(inp[0])

   return (step[0] % height, step[1] % width)


def move_infinite(step):
   directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

   next_steps = [(step[0] + d[0], step[1] + d[1]) for d in directions]
   next_steps = [s for s in next_steps if is_empty_slot(generate_correct_position(s))]

   return next_steps



def make_infinite_steps(steps):
   result = [move_infinite(step) for step in steps]
   result = [item for sublist in result for item in sublist]
   return set(result)

def part_2(inp):
   steps = get_starting_set(inp)

   a = []

   for i in range(26501365):
      steps = make_infinite_steps(steps)
      if (i - 64) % 131 == 0:
         a.append(len(steps))
      
      if len(a) == 3:

         end_value = 202300

         equation = lambda x: a[0] + x * (a[1] - a[0]) + x * (x - 1) * (a[2] - a[1] - a[1] + a[0])/2

         return equation(end_value)

   return sum([v for v in steps.values()])

inp = get_input(21)

print(part_1(inp))
print(part_2(inp))