from collections import Counter
from pathlib import Path

current_directory = Path('.')
with open(current_directory / 'day_3'/ 'input.txt', 'r') as input_file:
    input_data = input_file.read().split('\n')


def calculate_power_consumption():
    gamma = ''
    epsilon = ''
    for i in range(len(input_data[0])):
        common = Counter([binary[i] for binary in input_data])
        if common['0'] > common['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma, 2) * int(epsilon, 2)

def calculate_life_support_rating():
    filtered_binaries = input_data
    for i in range(len(filtered_binaries[0])):
        common = Counter([binary[i] for binary in filtered_binaries])
        if common['0'] > common['1']:
            filtered_binaries = [binary for binary in filtered_binaries if binary[i] == '0']
        else:
            filtered_binaries = [binary for binary in filtered_binaries if binary[i] == '1']
        oxygen_generator_rating = filtered_binaries[0]
    filtered_binaries = input_data
    for i in range(len(filtered_binaries[0])):
        common = Counter([binary[i] for binary in filtered_binaries])
        if common['0'] > common['1']:
            filtered_binaries = [binary for binary in filtered_binaries if binary[i] == '1']
        else:
            filtered_binaries = [binary for binary in filtered_binaries if binary[i] == '0']
        if filtered_binaries:
            co2_scrubbing_rating = filtered_binaries[0]
    return int(oxygen_generator_rating, 2) * int(co2_scrubbing_rating, 2)

print(calculate_power_consumption())
print(calculate_life_support_rating())