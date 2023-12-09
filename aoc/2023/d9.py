def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(inp: int):
   return [[int(val) for val in l.split(" ")] for l in inp]

def compute_next(seq):
   seqs = [seq]

   while not all([n == 0 for n in seqs[-1]]):
      new_seq = []

      for i in range(0, len(seqs[-1])-1):
         value = seqs[-1][i+1] - seqs[-1][i]
         new_seq.append(value)
      
      seqs.append(new_seq)
   
   val = 0
   prev_val = 0
   for k in range(len(seqs) - 1, -1, -1):
      val += seqs[k][-1]
      prev_val = seqs[k][0] - prev_val
   
   return val, prev_val

def part_1(numbers):
   return sum([compute_next(seq)[0] for seq in numbers])

def part_2(numbers):
   return sum([compute_next(seq)[1] for seq in numbers])

def part_1_and_2(numbers):
   vals = [compute_next(seq) for seq in numbers]
   p1 = sum([v[0] for v in vals])
   p2 = sum([v[1] for v in vals])

   return p1, p2

inp = get_input(9)
numbers = parse_input(inp)

print(part_1_and_2(numbers))