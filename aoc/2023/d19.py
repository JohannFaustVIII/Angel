def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(inp):
   rules = {}
   vals = []

   parsing_vals = False

   for l in inp:

      if len(l) == 0:
         parsing_vals = True
         continue

      if parsing_vals:
         new_val = {}
         l = l[1:-1]
         l = l.split(',')
         for v in l:
            name, value = v.split('=')
            new_val[name] = int(value)
         vals.append(new_val)
      else:
         new_rule = []
         name, conditions = l.split('{')
         conditions = conditions[:-1]
         conditions = conditions.split(',')
         for c in conditions:
            if ':' in c:
               k = c.split(':')
               c = k[0]
               next_state = k[1]
               n = c[0]
               s = c[1]
               value = int(c[2:])
               new_rule.append((n, s, value, next_state))
            else:
               new_rule.append((c,))
         rules[name] = new_rule
   
   return rules, vals

def part_1(rules, vals):
   accepted = 0
   for v in vals:
      state = 'in'

      while state in rules:
         state_rules = rules[state]

         for rule in state_rules:
            if len(rule) == 1:
               state = rule[0]
            else:
               value_to_check = v[rule[0]]
               value_to_compare = rule[2]

               if rule[1] == '<':
                  if value_to_check < value_to_compare:
                     state = rule[3]
                     break
               else:
                  if value_to_check > value_to_compare:
                     state = rule[3]
                     break


      if state == 'A':
         for k in v.keys():
            accepted += v[k]
   
   return accepted

def get_combinations(rules, state, ratings):

   __rating_copy = {}

   for k in ratings.keys():
      __rating_copy[k] = [l for l in ratings[k]]

   for k in __rating_copy.keys():
      if __rating_copy[k][1] < __rating_copy[k][0]:
         return 0

   if state == 'A':
      return (__rating_copy['x'][1] - __rating_copy['x'][0] + 1) * (__rating_copy['m'][1] - __rating_copy['m'][0] + 1) * (__rating_copy['a'][1] - __rating_copy['a'][0] + 1) * (__rating_copy['s'][1] - __rating_copy['s'][0] + 1)
   
   if state == 'R':
      return 0

   result = 0

   rule_to_check = rules[state]

   for rule in rule_to_check:
      if len(rule) == 1:
         result += get_combinations(rules, rule[0], __rating_copy)
      else:
         name = rule[0]
         cond = rule[1]
         value = rule[2]
         n_state = rule[3]

         if cond == '<':
            previous_value = __rating_copy[name][1]
            __rating_copy[name][1] = min(value - 1, previous_value)
            result += get_combinations(rules, n_state, __rating_copy)
            __rating_copy[name][1] = previous_value
            __rating_copy[name][0] = max(value, __rating_copy[name][0])
         else:
            previous_value = __rating_copy[name][0]
            __rating_copy[name][0] = max(value + 1, previous_value)
            result += get_combinations(rules, n_state, __rating_copy)
            __rating_copy[name][0] = previous_value
            __rating_copy[name][1] = min(value, __rating_copy[name][1])

   return result

def part_2(rules):
   start_rating = ({'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]})

   return get_combinations(rules, 'in', start_rating)


rules, vals = parse_input(get_input(19))

print(part_1(rules, vals))
print(part_2(rules))