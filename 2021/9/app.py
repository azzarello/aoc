# import numpy as np
# import pandas as pd
from pprint import pprint


f = open("input")
input = f.readlines()
heightmap = list()
for line in input:
    heightmap.append([int(x) for x in line.rstrip()])
# print(heightmap)
height = len(heightmap)
width = len(heightmap[0])


def traverse_heightmap(heightmap):
    risk_level = 0
    low_points = list()
    for i in range(height):
        for j in range(width):
            # print(i, j, type(heightmap[i][j]))
            current_cell = heightmap[i][j]
            try:
                if (
                    current_cell < heightmap[i + 1][j]
                    and current_cell < heightmap[i - 1][j]
                    and current_cell < heightmap[i][j + 1]
                    and current_cell < heightmap[i][j - 1]
                ):
                    print(i, j)
                    low_points.append((i, j))
                    risk_level += current_cell + 1
            except:
                if i == 0 and j == 0:
                    if (
                        current_cell < heightmap[i + 1][j]
                        and current_cell < heightmap[i][j + 1]
                    ):
                        low_points.append((i, j))
                        risk_level += current_cell + 1
                elif i == 0 and j == width - 1:
                    if (
                        current_cell < heightmap[i + 1][j]
                        and current_cell < heightmap[i][j - 1]
                    ):
                        low_points.append((i, j))
                        risk_level += current_cell + 1
                elif i == height - 1 and j == 0:
                    if (
                        current_cell < heightmap[i - 1][j]
                        and current_cell < heightmap[i][j + 1]
                    ):
                        low_points.append((i, j))
                        risk_level += current_cell + 1
                elif i == height - 1 and j == width - 1:
                    if (
                        current_cell < heightmap[i - 1][j]
                        and current_cell < heightmap[i][j - 1]
                    ):
                        low_points.append((i, j))
                        risk_level += current_cell + 1
                elif i == 0:
                    if (
                        current_cell < heightmap[i + 1][j]
                        and current_cell < heightmap[i][j + 1]
                        and current_cell < heightmap[i][j - 1]
                    ):
                        low_points.append((i, j))
                        risk_level += current_cell + 1
                elif j == 0:
                    if (
                        current_cell < heightmap[i + 1][j]
                        and current_cell < heightmap[i][j + 1]
                        and current_cell < heightmap[i - 1][j]
                    ):
                        low_points.append((i, j))
                        risk_level += current_cell + 1
                elif i == height - 1:
                    if (
                        current_cell < heightmap[i - 1][j]
                        and current_cell < heightmap[i][j + 1]
                        and current_cell < heightmap[i][j - 1]
                    ):
                        low_points.append((i, j))
                        risk_level += current_cell + 1
                elif j == width - 1:
                    if (
                        current_cell < heightmap[i + 1][j]
                        and current_cell < heightmap[i - 1][j]
                        and current_cell < heightmap[i][j - 1]
                    ):
                        low_points.append((i, j))
                        risk_level += current_cell + 1

                # print(i, j)
    print(f"Risk level is {risk_level}")
    return low_points


def traverse_basin(point, heightmap, count):
    if heightmap[point[0]][point[1]] == 9:
        return count
    else:
        heightmap[point[0]][point[1]] = 9
    if point[0] < height - 1:
        count = traverse_basin((point[0] + 1, point[1]), heightmap, count)
    if point[0] > 0:
        count = traverse_basin((point[0] - 1, point[1]), heightmap, count)
    if point[1] < width - 1:
        count = traverse_basin((point[0], point[1] + 1), heightmap, count)
    if point[1] > 0:
        count = traverse_basin((point[0], point[1] - 1), heightmap, count)
    return count + 1


if __name__ == "__main__":
    low_points = traverse_heightmap(heightmap)
    product_of_large_basins = 1
    basin_sizes = list()
    for point in low_points:
        copy_of_heightmap = list(heightmap)
        basin_size = traverse_basin(point, heightmap, 0)
        print(point, basin_size)
        basin_sizes.append(basin_size)
    basin_sizes.sort()
    print(basin_sizes)
    three_largest = basin_sizes[-3:]
    print(three_largest)
    for value in three_largest:
        product_of_large_basins *= value
    print(product_of_large_basins)
