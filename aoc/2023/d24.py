import numpy as np
from scipy.optimize import fsolve

def get_input(day: int):
    
  with open(f"aoc/2023/d{day}.input") as file:
      lines = file.readlines()
      lines = [line.strip() for line in lines]
  
  return lines

def parse_input(inp):

   result = []

   for line in inp:
      vals = line.split('@')

      position = [int(k.strip()) for k in vals[0].strip().split(',')]
      velocity = [int(k.strip()) for k in vals[1].strip().split(',')]

      result.append((tuple(position), tuple(velocity)))

   return result


def compute_times(px1, px2, py1, py2, vx1, vx2, vy1, vy2):
   left = vx2*vy1 - vy2 * vx1
   if left == 0:
      return None, None
   
   right = py2*vx1 - py1*vx1 - px2*vy1 + px1*vy1

   t2 = right/left
   t1 = (t2 * vx2 + px2 - px1)/vx1

   return t1, t2

def compute_position(a, b, x):
   return a * x + b

def part_1(hailstones):

   counter = 0

   for i1, h1 in enumerate(hailstones):
      for i2 in range(i1 + 1, len(hailstones)):
         h2 = hailstones[i2]

         px1 = h1[0][0]
         px2 = h2[0][0]
         py1 = h1[0][1]
         py2 = h2[0][1]

         vx1 = h1[1][0]
         vx2 = h2[1][0]
         vy1 = h1[1][1]
         vy2 = h2[1][1]

         t1, t2 = compute_times(px1, px2, py1, py2, vx1, vx2, vy1, vy2)
         if t1 is None:
            continue
         if t2 is None:
            continue
         if t1 < 0:
            continue
         if t2 < 0:
            continue

         x_position = compute_position(h1[1][0], h1[0][0], t1)
         y_position = compute_position(h1[1][1], h1[0][1], t1)

         if 200000000000000 <= x_position <= 400000000000000:
            if 200000000000000 <= y_position <= 400000000000000:
               counter += 1
   
   return counter

def generate_solver(hailstones):

   def eq_solver(z):
      Ax = z[0]
      Ay = z[1]
      Az = z[2]
      Bx = z[3]
      By = z[4]
      Bz = z[5]

      f = np.empty(600)

      index = 0
      for h in hailstones:
         px = h[0][0]
         py = h[0][1]
         pz = h[0][2]

         vx = h[1][0]
         vy = h[1][1]
         vz = h[1][2]

         f[index] = Ay * vx - Ax * vy - Ay * Bx + Ax * By + Bx * py - By * px - py * vx + px * vy
         index += 1
         f[index] = Ay * vz - Az * vy - Ay * Bz + Az * By + Bz * py - By * pz - py * vz + pz * vy
         index += 1

         # if index == 6:
         #    return f

      return f

   return eq_solver


def part_2(hailstones):
   solver = generate_solver(hailstones)

   zGuess = np.array([1]*600)
   z = fsolve(solver, zGuess)

   result = 0
   for i in z[:3]:
      result += int(i)
   return result

inp = get_input(24)

hailstones = parse_input(inp)

print(part_1(hailstones))
print(part_2(hailstones))