def write_start_matrix(x_values, y_values):
    x_min, x_max = find_min_max(x_values)
    y_min, y_max = find_min_max(y_values)
    sea_floor = []
    base_row = [0] * (x_max + 1)
    print(f"X {x_max}, Y {y_max}")
    for i in range(0, y_max + 1):
        sea_floor.append(base_row[:])
    return sea_floor


def find_min_max(data):
    min_x = min(data)
    max_x = max(data)
    return min_x, max_x


def paint_x(sea_floor, y, x_start, x_end):
    for x in range(x_start, x_end + 1, 1):
        sea_floor[y][x] += 1


def paint_y(sea_floor, x, y_start, y_end):
    for y in range(y_start, y_end + 1, 1):
        sea_floor[y][x] += 1


def paint_diagonal(sea_floor, start, end):
    if start[0] < end[0]:
        direction_x = 1
    else:
        direction_x = -1
    if start[1] < end[1]:
        direction_y = 1
    else:
        direction_y = -1
    coordinates_x = []
    coordinates_y = []
    for x in range(start[0], end[0]+direction_x, direction_x):
        coordinates_x.append(x)
    for y in range(start[1], end[1]+direction_y, direction_y):
        coordinates_y.append(y)
    for cord_pos in range(0, len(coordinates_x)):
        sea_floor[coordinates_y[cord_pos]][coordinates_x[cord_pos]] += 1


def paint_seafloor(sea_floor, data, diagonal):
    # Find if x or y is the same in both pairs
    for data_pair in data:
        if data_pair[0][0] == data_pair[1][0]:
            paint_y(sea_floor, data_pair[0][0], min(data_pair[0][1], data_pair[1][1]),
                    max(data_pair[0][1], data_pair[1][1]))
        elif data_pair[0][1] == data_pair[1][1]:
            paint_x(sea_floor, data_pair[0][1], min(data_pair[0][0], data_pair[1][0]),
                    max(data_pair[0][0], data_pair[1][0]))
        elif diagonal:
            paint_diagonal(sea_floor, data_pair[0], data_pair[1])


def count_occurrences(sea_floor):
    occurrences = 0
    for row in sea_floor:
        #print(row)
        for i in row:
            if i > 1:
                occurrences += 1
    return occurrences


def prep_data():
    f = open("05data", "r")
    #f = [
    #   "0, 9 -> 5, 9",
    #   "8, 0 -> 0, 8",
    #   "9, 4 -> 3, 4",
    #   "2, 2 -> 2, 1",
    #   "7, 0 -> 7, 4",
    #   "6, 4 -> 2, 0",
    #   "0, 9 -> 2, 9",
    #   "3, 4 -> 1, 4",
    #   "0, 0 -> 8, 8",
    #   "5, 5 -> 8, 2",
    #]

    data = []
    x_values = []
    y_values = []
    for row in f:
        tmp_row = row.split(" -> ")
        pair1 = tmp_row[0].split(",")
        pair2 = tmp_row[1].split(",")
        data.append([[int(pair1[0]), int(pair1[1])], [int(pair2[0]), int(pair2[1])]])
        x_values.append(int(data[-1][0][0]))
        x_values.append(int(data[-1][1][0]))
        y_values.append(int(data[-1][0][1]))
        y_values.append(int(data[-1][1][1]))
    sea_floor = write_start_matrix(x_values, y_values)
    return sea_floor, data


def part1():
    sea_floor, data = prep_data()
    paint_seafloor(sea_floor, data, False)
    occurrences = count_occurrences(sea_floor)
    print(occurrences)

def part2():
    sea_floor, data = prep_data()
    paint_seafloor(sea_floor, data, True)
    occurrences = count_occurrences(sea_floor)
    print(occurrences)

#part1()
part2()
