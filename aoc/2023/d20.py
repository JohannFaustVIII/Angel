def get_input(day: int):

  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(inp):
   result = {}
   conjuction_modules_inputs = {}

   for line in inp:
      left, right = line.split("->")
      left = left.strip()

      name = None
      module_type = None

      if left == 'broadcaster':
         name = left
      else:
         name = left[1:]
         module_type = left[0]

      next_modules = [r.strip() for r in right.strip().split(",")]

      result[name] = (module_type, next_modules)

   conjuction_modules = [k for k in result.keys() if result[k][0] == '&']

   for cm in conjuction_modules:
      inputs = []

      for k in result.keys():
         if cm in result[k][1]:
            inputs.append(k)
      
      conjuction_modules_inputs[cm] = inputs

   return result, conjuction_modules_inputs

def process_signal(module_map, ff_state, cm_state, signal_queue, observed_modules):

   low_signals = 0
   high_signals = 0

   min_rx = False
   logged = []

   while signal_queue:
      _to, is_high, _from = signal_queue.pop(0)

      low_signals += 0 if is_high else 1
      high_signals += 1 if is_high else 0

      if _to in observed_modules and is_high:
         logged.append(_from)

      if _to == 'rx' and not is_high:
         min_rx = True

      if _to not in module_map.keys():
         continue

      module_type = module_map[_to][0]
      next_modules = module_map[_to][1]

      if _to == 'broadcaster':
         for m in next_modules:
            signal_queue.append((m, is_high, _to))
      elif module_type == '%':
         if not is_high:
            ff_state[_to] = not ff_state[_to]

            for m in next_modules:
               signal_queue.append((m, ff_state[_to], _to))
      else:
         cm_state[_to][_from] = is_high
         next_pulse_type = not all([cm_state[_to][k] == True for k in cm_state[_to].keys()])

         for m in next_modules:
            signal_queue.append((m, next_pulse_type, _to))

   return low_signals, high_signals, ff_state, cm_state, min_rx, logged

def are_all_equal(vals):
   _min = None
   _max = None

   for v in vals.keys():
      if _min is None:
         _min = vals[v]
         _max = vals[v]
      _min = min(_min, vals[v])
      _max = max(_max, vals[v])

   return _min == _max

def part_1_and_2(module_map, cm_inputs):
   low = 0
   high = 0
   rx_result = None

   observed_modules = [m for m in module_map.keys() if 'rx' in module_map[m][1]]

   starters = {}
   offsets = {}

   ff_state = {}
   cm_state = {}

   for k in [k for k in module_map.keys() if module_map[k][0] == '%']:
      ff_state[k] = False

   for k in cm_inputs.keys():
      cm_s = {}
      for m in cm_inputs[k]:
         cm_s[m] = False
      cm_state[k] = cm_s

   for i in range(1000):
      _low, _high, ff_state, cm_state, min_rx, logged = process_signal(module_map, ff_state, cm_state, [('broadcaster', False, None)], observed_modules)

      if logged:
         for l in logged:
            if l not in starters:
               starters[l] = i
            else:
               offsets[l] = starters[l] - i

      if min_rx and rx_result is None:
         rx_result = i + 1

      low += _low
      high += _high

   part_1_result = low * high

   while rx_result is None:
      if len(offsets) == len(cm_inputs[observed_modules[0]]):
         rx_result = 1
         for k in starters.keys():
            rx_result *= offsets[k] # that is lucky solution, because first loop doesn't have to be the same as offset, and it would require a different solution

         return part_1_result, rx_result

      i += 1
      
      _low, _high, ff_state, cm_state, min_rx, logged = process_signal(module_map, ff_state, cm_state, [('broadcaster', False, None)], observed_modules)

      if logged:
         for l in logged:
            if l not in starters:
               starters[l] = i
            else:
               offsets[l] = i - starters[l]

      if min_rx and rx_result is None:
         rx_result = i + 1

   return part_1_result, rx_result

inp = get_input(20)
module_map, cm_inputs = parse_input(inp)

print(part_1_and_2(module_map, cm_inputs))