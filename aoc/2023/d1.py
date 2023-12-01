
def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def get_number(line: str) -> int:
   only_numbers = ''.join([l if l.isnumeric() else '' for l in line])

   return int(only_numbers[0] + only_numbers[-1])

def part_1(input):
   numbers = [get_number(line) for line in input]
   return sum(numbers)

def get_all_number(line:str) -> int:
   only_numbers = [l if l.isnumeric() else '' for l in line]

   names = {'one' : 1,
            'two' : 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9}
   
   for key, value in names.items():
      for x in range(0, len(line) - len(key) + 1):
         if line[x: x + len(key)] == key:
            only_numbers[x] = str(value)

   only_numbers = ''.join(only_numbers)
   return int(only_numbers[0] + only_numbers[-1])

def part_2(input):
   numbers = [get_all_number(line) for line in input]
   return sum(numbers)

input = get_input(1)

print(part_1(input))
print(part_2(input))