def part1():
    data = ["2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678"]
    f = open("09data", "r")
    data = []
    for row in f:
        data.append(row.split("\n")[0])
    lowpoints = find_lowpoint(data)
    total = 0
    for point in lowpoints:
        total += (int(point) + 1)
    print(lowpoints)
    print(total)


def find_lowpoint(data):
    lowpoints = []
    for row in range(len(data)):
        for pos in range(len(data[row])):
            if (pos == 0 or data[row][pos] < data[row][pos - 1]) and \
                    (pos == (len(data[row]) - 1) or data[row][pos] < data[row][pos + 1]) and \
                    (row == 0 or data[row][pos] < data[row - 1][pos]) and \
                    (row == (len(data) - 1) or data[row][pos] < data[row + 1][pos]):
                print(f"Lowpoint {data[row][pos]}, row:{row}, pos{pos}")
                lowpoints.append(data[row][pos])
    return lowpoints


# ------------------------------------------------------------------------------------------------------#


def part2():
    data = ["2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678"]
    f = open("09data", "r")
    data = []
    for row in f:
        data.append(row.split("\n")[0])
    lowpoints = find_lowpoint_coordinates(data)
    find_basins(data, lowpoints)


def find_lowpoint_coordinates(data):
    lowpoints = []
    for row in range(len(data)):
        for pos in range(len(data[row])):
            if (pos == 0 or data[row][pos] < data[row][pos - 1]) and \
                    (pos == (len(data[row]) - 1) or data[row][pos] < data[row][pos + 1]) and \
                    (row == 0 or data[row][pos] < data[row - 1][pos]) and \
                    (row == (len(data) - 1) or data[row][pos] < data[row + 1][pos]):
                lowpoints.append([row, pos])
    return lowpoints


def find_basins(data, lowpoints):
    basins = []
    x_min = 0
    x_max = len(data[0]) - 1
    y_min = 0
    y_max = len(data) - 1
    for lowpoint in lowpoints:
        basin = neighbours(data, lowpoint, x_min, x_max, y_min, y_max)
        basin_size = len(basin)
        basins.append(basin_size)
    basins.sort(reverse=True)
    print(int(basins[0]) * int(basins[1]) * int(basins[2]))


def neighbours(data, start, x_min, x_max, y_min, y_max):
    higher = [start]
    lowpoint = data[start[0]][start[1]]
    if start[1] > x_min:
        if data[start[0]][start[1] - 1] != "9" and data[start[0]][start[1] - 1] > lowpoint:
            only_unique(neighbours(data, [start[0], start[1] - 1], x_min, x_max, y_min, y_max), higher)

    if start[1] < x_max:
        if data[start[0]][start[1] + 1] != "9" and data[start[0]][start[1] + 1] > lowpoint:
            only_unique(neighbours(data, [start[0], start[1] + 1], x_min, x_max, y_min, y_max), higher)

    if start[0] > y_min:
        if data[start[0] - 1][start[1]] != "9" and data[start[0] - 1][start[1]] > lowpoint:
            only_unique(neighbours(data, [start[0] - 1, start[1]], x_min, x_max, y_min, y_max), higher)

    if start[0] < y_max:
        if data[start[0] + 1][start[1]] != "9" and data[start[0] + 1][start[1]] > lowpoint:
            only_unique(neighbours(data, [start[0] + 1, start[1]], x_min, x_max, y_min, y_max), higher)
    return higher


def only_unique(tmp, higher):
    for i in tmp:
        if i not in higher:
            higher.append(i)


# part1()
# 431 low

part2()
