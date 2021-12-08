import numpy as np
import pandas as pd


def load_crabs():
    f = open("input")
    crabs = [int(x) for x in f.read().rstrip().split(",")]
    crab_np = np.array(crabs)
    crab_counts = list()
    for i in range(max(crabs) + 1):
        crab_counts.append(len(np.where(crab_np == i)[0]))
    return crab_counts


def calculate_fuel(distance):
    fuel_counter = 0
    for i in range(1, abs(distance) + 1):
        fuel_counter += i
    return fuel_counter


# original: 1.01 seconds on non-compounding distances
if __name__ == "__main__":
    crab_counts = load_crabs()
    results = list()
    for i in range(len(crab_counts)):
        print(i)
        fuel_count = 0
        for position, count in enumerate(crab_counts):
            # fuel_count += abs(i - position) * count
            fuel_count += calculate_fuel(i - position) * count
        results.append(fuel_count)
    best_line = results.index(min(results))
    print(min(results))
