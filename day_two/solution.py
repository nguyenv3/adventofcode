from pathlib import Path

current_directory = Path('.')
with open(current_directory / 'day_two'/ 'input.txt', 'r') as input_file:
    moves = input_file.read().split('\n')

def perform_moves():
    horizontal = 0
    depth = 0
    for move in moves:
        direction, units = move.split(' ')
        if direction == 'forward':
            horizontal += int(units)
        elif direction == 'down':
            depth += int(units)
        elif direction == 'up':
            depth -= int(units)
    return horizontal, depth

def perform_moves_with_aim():
    horizontal = 0
    depth = 0
    aim = 0
    for move in moves:
        direction, units = move.split(' ')
        if direction == 'forward':
            horizontal += int(units)
            depth += int(units) * aim
        elif direction == 'down':
            aim += int(units)
        elif direction == 'up':
            aim -= int(units)
    return horizontal, depth

print(perform_moves())
print(perform_moves_with_aim())