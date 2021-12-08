def calculate_position_simple(data):
    min_pos = min(data)
    max_pos = max(data)
    min_cost = None
    for i in range(min_pos, max_pos):
        tmp_cost = 0
        for crab in data:
            tmp_cost += abs(crab - i)
        if min_cost:
            min_cost = min(min_cost, tmp_cost)
        else:
            min_cost = tmp_cost
    return min_cost


def part1():
    f = open("07data", "r")
    tmp = f.readline().split(",")
    tmp = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    data = []

    for crab in tmp:
        data.append(int(crab))
    min_cost = calculate_position_simple(data)
    print(f"min_cost: {min_cost}")


def calculate_position(data):
    min_pos = min(data)
    max_pos = max(data)
    min_cost = None
    for i in range(min_pos, max_pos):
        tmp_cost = 0
        for crab in data:
            for step in range(1, abs(crab - i)+1):
                tmp_cost += step
        if min_cost:
            min_cost = min(min_cost, tmp_cost)
        else:
            min_cost = tmp_cost
    return min_cost


def part2():
    f = open("07data", "r")
    tmp = f.readline().split(",")
    #tmp = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    data = []

    for crab in tmp:
        data.append(int(crab))
    min_cost = calculate_position(data)
    print(f"min_cost: {min_cost}")


part1()
part2()
