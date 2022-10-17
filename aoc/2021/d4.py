from functools import reduce

def map_input(lines : list[str]) -> tuple[list[int], list[list[int]]]:
    numbers = list(map(lambda x : int(x), lines[0].strip().split(",")))

    lines_with_boards = lines[1:]
    boards = []
    number_of_boards = int(len(lines_with_boards)/6)

    for i in range(0, number_of_boards):
        board_lines = []

        for line in lines_with_boards[i*6:i*6+6][1:]:
            board_lines.extend(list(map(lambda x : int(x), line.strip().split())))

        boards.append(board_lines)

    return numbers, boards

def is_board_winning(active_numbers : list[int], board : list[int]):
    for i in range(0, 5):
        if all(value in active_numbers for value in board[i::5]):
            return True

    for i in range(0,len(board), 5):
        if all(value in active_numbers for value in board[i:i+5]):
            return True
    
    return False

def compute_winning_score(winning_number : int, active_numbers: list[int], board: list[int]) -> int:
    last_numbers = [value for value in board if value not in active_numbers]
    sum = reduce(lambda x,y : x + y, last_numbers, 0)
    return winning_number * sum


with open("aoc/2021/d4.input") as file:
    lines = file.readlines()
    numbers, boards = map_input(lines)

for index, num in enumerate(numbers):
    boards_to_remove = []

    for b_index, board in enumerate(boards):
        if (is_board_winning(numbers[0:index+1], board)):
            boards_to_remove.append(b_index)
            print(compute_winning_score(num, numbers[0:index+1], board))

    if boards_to_remove:
        boards_to_remove.reverse()
        for value in boards_to_remove:
            boards.pop(value)
