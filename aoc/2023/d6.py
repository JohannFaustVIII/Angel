def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(input):
  times = []
  distances = []

  for t in input[0].split(":")[1].split(" "):
    if t != '':
      times.append(int(t))
  
  for d in input[1].split(":")[1].split(" "):
    if d != '':
      distances.append(int(d))
  
  return times, distances
    
def part_1(times, distances):
  result = 1
  for i in range(len(times)):
    time = times[i]
    distance = distances[i]

    for t in range(1, time):
      d = t * (time - t)
      if d > distance:
        result *= (time - t - t + 1)
        break

  return result 

def part_2(times, distances):
  time = int(''.join([str(t) for t in times]))
  distance = int(''.join([str(d) for d in distances]))

  return part_1([time], [distance])


input = get_input(6)

time, distances = parse_input(input)

print(part_1(time, distances))
print(part_2(time, distances))