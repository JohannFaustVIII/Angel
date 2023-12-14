import functools

def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def part_1(inp):
   rocks = [0] * len(inp[0])
   sum = 0
   for y, line in enumerate(inp):
      for x, l in enumerate(line):
         if l == '.':
            sum += rocks[x]
         elif l == 'O':
            sum += y + 1
            rocks[x] += 1
         else:
            rocks[x] = 0
   return sum

def move_state(state):
   rocks = [None] * len(state[0])

   for y, line in enumerate(state):
      for x, l in enumerate(line):

         if l == '.':
            if rocks[x] is None:
               rocks[x] = y
         elif l == 'O':
            if rocks[x] is not None:
               state[rocks[x]][x] = 'O'
               state[y][x] = '.'
               rocks[x] += 1
         else:
            rocks[x] = None
   
   return state

def rotate_state(state):
   new_state = [[state[y][x] for y in range(len(state))] for x in range(len(state[0]))]
   for line in new_state:
      line.reverse()
   return new_state

@functools.cache
def cycle(state):
   state = [list(line) for line in state]
   for _ in range(4):
      state = move_state(state)
      state = rotate_state(state)
   state = tuple([tuple(x) for x in state])
   return state

   # move up (north)
   state = rotate_state()
   # move left (west)
   # move down (south)
   # move right (east)

def count_load(state):
   state = [list(line) for line in state]
   state.reverse()
   result = 0
   for y, line in enumerate(state):
      result += sum([y + 1 for l in line if l == 'O'])
   return result

def part_2(inp):
   inp = tuple([tuple(x) for x in inp])
   state = inp
   prev_states = [state]

   for i in range(1000000000):
      state = cycle(state)
      if state in prev_states:
         prev_states_length = len(prev_states)
         cycle_index = prev_states.index(state)
         cycle_size = prev_states_length - cycle_index
         final_index = cycle_index + (1000000000 - cycle_index) % cycle_size
         state = prev_states[final_index]
         break
      else:
         prev_states.append(state)
   
   return count_load(state)


inp = get_input(14)
inp.reverse()

print(part_1(inp))

inp.reverse()

for i in range(len(inp)):
   inp[i] = [x for x in inp[i]]

print(part_2(inp))

