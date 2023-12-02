
def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_line(line: str):
   values = line.split(":")
   id = int(values[0].split(" ")[1])

   games = []

   for val in values[1].split(";"):
      red = 0
      green = 0
      blue = 0

      for v in val.split(","):
         v = v.strip()

         number, color = v.split(" ")
         number = int(number)

         if color == 'red':
            red = number
         elif color == 'green':
            green = number
         else:
            blue = number

      games.append((red, green, blue))

   return (id, games)

def part_1(input: list[str]):
   games = [parse_line(i) for i in input]

   sum = 0
   for id, attempt in games:
      val = id
      for a in attempt:
         if a[0] > 12 or a[1] > 13 or a[2] > 14:
            val = 0
      sum += val
   return sum
      

def part_2(input: list[str]):
   games = [parse_line(i) for i in input]

   sum = 0
   for id, attempt in games:
      r = 0
      g = 0
      b = 0

      for a in attempt:
         r = max(r, a[0])
         g = max(g, a[1])
         b = max(b, a[2])

      sum += r*g*b
   return sum

input = get_input(2)


print(part_1(input))
print(part_2(input))