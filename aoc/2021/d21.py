with open("aoc/2021/d21.input") as file:
    lines = file.readlines()

    first_player_position = int(lines[0].strip().split(":")[1].strip())
    second_player_position = int(lines[1].strip().split(":")[1].strip())

def part1(first : int, second : int) -> int:
    first_score = 0
    second_score = 0

    class Dice:

        def __init__(self) -> None:
            self.dice = 100

        def roll(self) -> int:
            self.dice += 1
            if self.dice > 100:
                self.dice = 1
            return self.dice
    
    class Position:

        def __init__(self, start) -> None:
            self.position = start

        def move(self, move : int) -> int:
            self.position += move
            while self.position > 10:
                self.position -= 10
            return self.position
    
    dice = Dice()
    first_player = Position(first)
    second_player = Position(second)

    first_score = 0
    second_score = 0

    first_move = True
    rolls = 0

    while first_score < 1000 and second_score < 1000:
        move = dice.roll() + dice.roll() + dice.roll()
        rolls += 3

        if first_move:
            first_score += first_player.move(move)
        else:
            second_score += second_player.move(move)
        
        first_move = not first_move

    return rolls * (second_score if first_score >= 1000 else first_score)


def part2(first : int, second : int) -> int:
    first_player_wins = 0
    second_player_wins = 0

    situations = {(first, 0, second, 0) : 1}
    first_player_move = True
    while situations:
        new_situations = {}
        for r1 in range(1,4):
            for r2 in range(1,4):
                for r3 in range(1, 4):
                    move = r1 + r2 + r3

                    for key, value in situations.items():
                        f_position = key[0]
                        f_score = key[1]
                        s_position = key[2]
                        s_score = key[3]

                        count = value

                        if first_player_move:
                            f_position += move
                            while f_position > 10:
                                f_position -= 10
                            f_score += f_position
                            if f_score >= 21:
                                first_player_wins += count
                            else:
                                new = (f_position, f_score, s_position, s_score)
                                if new not in new_situations:
                                    new_situations[new] = count
                                else:
                                    new_situations[new] += count
                        else:
                            s_position += move
                            while s_position > 10:
                                s_position -= 10
                            s_score += s_position
                            if s_score >= 21:
                                second_player_wins += count
                            else:
                                new = (f_position, f_score, s_position, s_score)
                                if new not in new_situations:
                                    new_situations[new] = count
                                else:
                                    new_situations[new] += count
                            

        situations = new_situations
        first_player_move = not first_player_move
    
    return max([first_player_wins, second_player_wins])


print(part1(first_player_position, second_player_position))
print(part2(first_player_position, second_player_position))
