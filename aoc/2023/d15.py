def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(inp):
   return inp[0].split(',')

def prepare_hashes():
   lut = {}
   for i in range(0, 513):
      lut[i] = (i*17)%256
   return lut

def compute_hash(lut, seq):
   start = 0

   for l in seq:
      start += ord(l)
      start = lut[start]
   
   return start

def part_1(inp):
   lut = prepare_hashes()

   sum = 0
   for seq in inp:
      sum += compute_hash(lut, seq)

   return sum

def parse_seq(seq):
   if '=' in seq:
      vals = seq.split('=')
      return vals[0], '=', int(vals[1])
   else:
      return seq[:-1], '-', None

def part_2(inp):
   lut = prepare_hashes()
   boxes = [[] for _ in range(256)]

   for seq in inp:
      label, operation, value = parse_seq(seq)
      hash = compute_hash(lut, label)

      box = boxes[hash]
      if operation == '=':
         found = False
         for lens in box:
            if lens[0] == label:
               lens[1] = value
               found = True
               break
         if not found:
            box.append([label, value])
      else:
         index = -1
         for i, lens in enumerate(box):
            if lens[0] == label:
               index = i
         if index != -1:
            box.pop(index)
   
   sum = 0
   for b, box in enumerate(boxes):
      for slot, lens in enumerate(box):
         sum += (b + 1) * (slot + 1) * lens[1]
   
   return sum



inp = get_input(15)
inp = parse_input(inp)


print(part_1(inp))
print(part_2(inp))