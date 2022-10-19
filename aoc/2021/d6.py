from numpy import zeros


with open("aoc/2021/d6.input") as file:
    line = file.readline()

    lanternfishes = [int(x) for x in line.strip().split(",")]

def compute_lanternfishes(lanternfishes : list[int], days : int):
    begin_number = len(lanternfishes)
    days_increase = zeros(days + 10, int)

    for lanternfish in lanternfishes:
        days_increase[lanternfish] += 1

    for day in range(days):
        begin_number += days_increase[day]
        days_increase[day+7] += days_increase[day]
        days_increase[day+9] += days_increase[day]
    
    return begin_number


print(f"After 80 days: {compute_lanternfishes(lanternfishes, 80)}")
print(f"After 80 days: {compute_lanternfishes(lanternfishes, 256)}")