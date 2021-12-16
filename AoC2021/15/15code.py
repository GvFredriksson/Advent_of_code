def part1():
    f = open("15test_data", "r")
    # f = open("15data", "r")
    square_weights = {}
    y = 0
    for row in f:
        for x in range(len(row.split("\n")[0])):
            square_weights[(y, x)] = int(row[x])
        y += 1
        x_max = len(row) - 1
    start = [0, 0]
    goal = (y - 1, x_max)
    path_weights = {}
    calculate_weights_simple(square_weights, path_weights, start, goal)
    calculate_weights(square_weights, path_weights, start, goal)
    print(path_weights[goal])


def calculate_weights_simple(square_weights, path_weights, start, end):
    for y in range(start[1], end[1] + 1, 1):
        for x in range(start[0], end[0] + 1, 1):
            if (y, x) == (0, 0):
                path_weight = 0
            else:
                path_weight = path_weights[y, x]
            try:
                path_weights[y + 1, x] = path_weight + square_weights[y + 1, x]
            except KeyError:
                pass

            try:
                path_weights[y, x + 1] = path_weight + square_weights[y, x + 1]
            except KeyError:
                pass


def calculate_weights(square_weights, path_weights, start, end):
    for y in range(start[1], end[1] + 1, 1):
        for x in range(start[0], end[0] + 1, 1):
            if (y, x) == (0, 0):
                path_weight = 0
            else:
                path_weight = path_weights[y, x]
            try:
                if (path_weight + square_weights[y + 1, x]) < path_weights[y + 1, x]:
                    path_weights[y + 1, x] = path_weight + square_weights[y + 1, x]
            except KeyError:
                pass
            try:
                if path_weight + square_weights[y - 1, x] < path_weights[y - 1, x]:
                    path_weights[y - 1, x] = path_weight + square_weights[y - 1, x]
            except KeyError:
                pass
            try:
                if path_weight + square_weights[y, x + 1] < path_weights[y, x + 1]:
                    path_weights[y, x + 1] = path_weight + square_weights[y, x + 1]
            except KeyError:
                pass
            try:
                if path_weight + square_weights[y, x - 1] < path_weights[y, x - 1]:
                    path_weights[y, x - 1] = path_weight + square_weights[y, x - 1]
            except KeyError:
                pass


# ---------------------------------------------------------------------------------------


def part2():
    # f = open("15test_data", "r")
    f = open("15data", "r")
    square_weights = {}
    y = 0
    for row in f:
        for x in range(len(row.split("\n")[0])):
            square_weights[(y, x)] = int(row[x])
        y += 1
        x_max = len(row) - 1
    start = [0, 0]
    goal = (y - 1, x_max)
    path_weights = {}
    expand_map(4, start, goal, square_weights)

    goal = max(square_weights.__iter__())
    calculate_weights_simple(square_weights, path_weights, start, goal)
    calculate_weights(square_weights, path_weights, start, goal)
    calculate_weights(square_weights, path_weights, start, goal)
    calculate_weights(square_weights, path_weights, start, goal)
    calculate_weights(square_weights, path_weights, start, goal)
    calculate_weights(square_weights, path_weights, start, goal)

    print(path_weights[goal])


def expand_map(times, left_top, right_bot, square_weights):
    width = (right_bot[1] - left_top[1]) + 1
    height = (right_bot[0] - left_top[0]) + 1
    # Widen the map
    for x_step in range(1, times + 1, 1):
        for y in range(0, height, 1):
            for x in range(0, width, 1):
                new_weight = square_weights[(y, x + (x_step - 1) * width)] + 1
                if new_weight > 9:
                    new_weight = 1
                square_weights[(y, x + (x_step * width))] = new_weight
    width = width * (times + 1)
    # Increase the height of the map
    for y_step in range(1, times + 1, 1):
        for y in range(0, height, 1):
            for x in range(0, width, 1):
                new_weight = square_weights[(y + (y_step - 1) * height), x] + 1
                if new_weight > 9:
                    new_weight = 1
                square_weights[(y + y_step * height, x)] = new_weight


#

part1()
part2()
