with open("aoc/2021/d17.input") as file:
    line = file.readline()
    line = line.strip().split(":")[1]
    coords = line.strip().split(",")
    x_min, x_max = [int(x.strip()) for x in coords[0].split("=")[1].split("..")]
    y_min, y_max = [int(y.strip()) for y in coords[1].split("=")[1].split("..")]

print(f"X_min={x_min} X_max={x_max} Y_min={y_min} Y_max={y_max}")

def chech_velocity(x_vel : int, y_vel : int, x_area : tuple[int, int], y_area : tuple[int, int]) -> tuple[bool, int]:
    x_position = 0
    y_position = 0
    max_y = 0

    while True:
        x_position += x_vel
        y_position += y_vel
        if y_position > max_y:
            max_y = y_position

        if x_area[0] <= x_position <= x_area[1] and y_area[0] <= y_position <= y_area[1]:
            return True, max_y
        
        if y_position < y_area[0] or x_position > x_area[1]:
            return False, 0
        
        if x_vel == 0 and x_position < x_area[0]:
            return False, 0

        if x_vel > 0:
            x_vel -= 1
        if x_vel < 0:
            x_vel += 1
        y_vel -= 1

def find_velocities(x_area: tuple[int, int], y_area: tuple[int, int]) -> tuple[int, int]:

    min_x_velocity = 0
    max_x_velocity = x_area[1]

    min_y_velocity = y_area[0]
    max_y_velocity = 200 # totally random number

    max_heights = []

    for x in range(min_x_velocity, max_x_velocity + 1):
        for y in range(min_y_velocity, max_y_velocity + 1):
            correct, height = chech_velocity(x, y, x_area, y_area)
            if correct:
                max_heights.append(height)

    return max(max_heights), len(max_heights)

print(find_velocities((x_min, x_max), (y_min, y_max)))