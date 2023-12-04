def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(input):
   games = []
   for line in input:
      game = line.split(":")[1]
      win, my = game.split(" | ")
      winning_games = tuple([int(win[x:x+3].strip()) for x in range(0, len(win), 3)])
      my_games = tuple([int(my[x:x+3].strip()) for x in range(0, len(my), 3)])
      games.append((winning_games, my_games))
   return games

def part_1(input):
   games = parse_input(input)
   result = 0
   for winning_numbers, my_numbers in games:
      wins = sum([1 if m in winning_numbers else 0 for m in my_numbers])

      if wins > 0:
         result += 2**(wins-1)
   return result

def part_2(input):
    games = parse_input(input)
    cards = [1 for _ in games]
    index = 0
    for winning_numbers, my_numbers in games:
      wins = sum([1 if m in winning_numbers else 0 for m in my_numbers])

      if wins > 0:
        for i in range(index + 1, index + wins + 1):
           cards[i] += cards[index]
      index += 1
    
    return sum(cards)
          
      
      

input = get_input(4)

print(part_1(input))
print(part_2(input))