from copy import deepcopy
from pathlib import Path

current_directory = Path('.')
with open(current_directory / 'day_one' / 'input.txt', 'r') as input_file:
    measurements = input_file.read().split('\n')

measurements = [int(measurement) for measurement in measurements]

def get_times_measurement_increased():
    times_measurement_increased = 0
    previous_measurement = measurements[0]
    for measurement in measurements[1:]:
        if measurement > previous_measurement:
            times_measurement_increased += 1
        previous_measurement = measurement
    return times_measurement_increased

def get_times_measurement_window_increased():
    window_size = 3
    times_measurement_window_increased = 0
    window_a = measurements[:window_size]
    window_b = measurements[1:window_size]
    for measurement in measurements[3:]:
        window_b.append(measurement)
        if sum(window_b) > sum(window_a):
            times_measurement_window_increased += 1   
        window_a = deepcopy(window_b)
        window_b.pop(0)
    return times_measurement_window_increased

assert get_times_measurement_increased() == 1502
assert get_times_measurement_window_increased() == 1538