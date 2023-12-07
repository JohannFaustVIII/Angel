def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_line(line):
   vals = line.split(" ")
   return (vals[0], int(vals[1]))

def parse_input(input):
   return [parse_line(x) for x in input]

def get_hand_strength(hand):
   cards = {}

   for c in hand:
      if c in cards:
         cards[c] = cards[c] + 1
      else:
         cards[c] = 1
   
   if len(cards) == 1:
      return 7 # five of a kind
   elif len(cards) == 2:
      for c, count in cards.items():
         if count == 4 or count == 1:
            return 6 # four of a king
         else:
            return 5 # full house
   elif len(cards) == 3:
      for c, count in cards.items():
         if count == 3:
            return 4 # three of a kind
         elif count == 2:
            return 3 # two pairs
   elif len(cards) == 4:
      return 2 # one pair
   else:
      return 1 # high card
  
def get_card_strength(card):
   card_value = {
      'T' : 10,
      'J' : 11,
      'Q' : 12,
      'K' : 13,
      'A' : 14
   }

   if card in card_value:
      return card_value[card]
   else:
      return int(card)

def get_total_hand_strength(hand_with_bind):
   hand = hand_with_bind[0]
   value = get_hand_strength(hand)
   for h in hand:
      value <<= 4
      value += get_card_strength(h)
   return value

def part_1(hands):
   hands_to_sort = [h for h in hands]
   hands_to_sort.sort(key=get_total_hand_strength)

   sum = 0
   for index, value in enumerate(hands_to_sort):
      bid = value[1]
      sum += (index + 1) * bid

   return sum


def p2_get_hand_strength(hand):
   cards = {}
   jokers = 0

   for c in hand:
      if c == 'J':
         jokers += 1
      elif c in cards:
         cards[c] = cards[c] + 1
      else:
         cards[c] = 1
   
   if len(cards) <= 1:
      return 7 # five of a kind
   elif len(cards) == 2:
      for c, count in cards.items():
         if count + jokers == 4:
            return 6 # four of a kind
      for c, count in cards.items():
         if count + jokers == 3:
            return 5 # full house
   elif len(cards) == 3:
      for c, count in cards.items():
         if count + jokers == 3:
            return 4 # three of a kind
      for c, count in cards.items():
         if count + jokers == 2:
            return 3 # two pairs
   elif len(cards) == 4:
      return 2 # one pair
   else:
      return 1 # high card

def p2_get_card_strength(card):
   card_value = {
      'T' : 10,
      'J' : 1,
      'Q' : 12,
      'K' : 13,
      'A' : 14
   }

   if card in card_value:
      return card_value[card]
   else:
      return int(card)
   
def p2_get_total_hand_strength(hand_with_bind):
   hand = hand_with_bind[0]
   value = p2_get_hand_strength(hand)
   for h in hand:
      value <<= 4
      value += p2_get_card_strength(h)
   return value

def part_2(hands):
   hands_to_sort = [h for h in hands]
   hands_to_sort.sort(key=p2_get_total_hand_strength)

   sum = 0
   for index, value in enumerate(hands_to_sort):
      bid = value[1]
      sum += (index + 1) * bid

   return sum

input = get_input(7)
input = parse_input(input)

print(part_1(input))
print(part_2(input))
