import functools



def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(inp):
   lines = [line.split(' ') for line in inp]
   lines = [(line[0], tuple([int(x) for x in line[1].split(',')])) for line in lines]
   return lines

def is_correct(row, arr):
   row_arr = tuple([len(r) for r in row.split('.') if len(r) > 0])
   return row_arr == arr

@functools.cache
def is_actual_correct(row, arr):
   ind = row.find('?')
   sub_row = row[:ind]
   sub_arr = tuple([len(r) for r in sub_row.split('.') if len(r) > 0])

   if len(sub_arr) > 0:
      if len(sub_arr) > len(arr):
         return False
      for i in range(0, len(sub_arr) - 1):
         if sub_arr[i] != arr[i]:
            return False
      if sub_arr[-1] > arr[len(sub_arr) - 1]:
         return False
   return True

@functools.cache
def compute_outcomes(row, arr):
   if '?' not in row:
      return 1 if is_correct(row, arr) else 0
   if row[0] == '.':
      return compute_outcomes(row[1:], arr)
   
   if len(arr) == 0:
      return 1 if all([r != '#' for r in row]) else 0

   ind = row.find('?')
   dot_ind = row.find('.')
   if ind > 0 and dot_ind > 0 and dot_ind < ind:
      sub_row = row[:dot_ind]
      if len(sub_row) != arr[0]:
         return 0
      else:
         return compute_outcomes(row[dot_ind:], arr[1:])
   if not is_actual_correct(row, arr):
      return 0
   outcomes = 0
   outcomes += compute_outcomes(row.replace('?', '.', 1), arr)
   outcomes += compute_outcomes(row.replace('?', '#', 1), arr)
   return outcomes

def part_1(lines):
   sum = 0
   for i, line in enumerate(lines):
      row = line[0]
      arr = line[1]

      possible_outcomes = compute_outcomes(row, arr)
      sum += possible_outcomes

   return sum

def part_2(lines):
   extended_lines = [
      (
      l[0] + '?' + l[0] + '?' + l[0] + '?' + l[0] + '?' + l[0],
      l[1]*5
      )
      for l in lines
   ]
   return part_1(extended_lines)

inp = get_input(12)
lines = parse_input(inp)
print('Part 1 result:', part_1(lines))
print('Part 2 result:', part_2(lines))