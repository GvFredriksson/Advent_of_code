def part1():
    # f = ["5483143223",
    #      "2745854711",
    #      "5264556173",
    #      "6141336146",
    #      "6357385478",
    #      "4167524645",
    #      "2176841721",
    #      "6882881134",
    #      "4846848554",
    #      "5283751526"]
    f = open("11data", "r")
    data = []
    for row in f:
        tmp_row = []
        for fish in row.split("\n")[0]:
            tmp_row.append(int(fish))
        data.append(tmp_row)
    flashes = turn_cycle(data, 100)
    print(flashes)


def turn_cycle(data, turns):
    flashes = 0
    for turn in range(turns):
        exploding = []
        # print(turn)
        increase_all(data)
        while True:
            new_cycle = []
            find_exploding_fish(data, exploding, new_cycle)
            if not new_cycle:
                break
            for fish in new_cycle:
                increase_neighbours(data, fish)
            exploding.extend(new_cycle)
        flashes += len(exploding)
        for fish in exploding:
            data[fish[0]][fish[1]] = 0
        # for row in data:
        #    print(row)
    return flashes


def increase_all(data):
    rows = len(data)
    width = len(data[0])
    for row_pos in range(rows):
        for fish_pos in range(width):
            data[row_pos][fish_pos] += 1


def find_exploding_fish(data, exploding, new_cycle):
    rows = len(data)
    width = len(data[0])
    for row_pos in range(rows):
        for fish_pos in range(width):
            if [row_pos, fish_pos] not in exploding and \
                    [row_pos, fish_pos] not in new_cycle \
                    and data[row_pos][fish_pos] > 9:
                new_cycle.append([row_pos, fish_pos])


def try_increase(data, row, pos):
    try:
        if row >= 0 and pos >= 0:
            data[row][pos] += 1
    except IndexError:
        pass


def increase_neighbours(data, focus):
    try_increase(data, focus[0] - 1, focus[1] - 1)
    try_increase(data, focus[0] - 1, focus[1])
    try_increase(data, focus[0] - 1, focus[1] + 1)

    try_increase(data, focus[0], focus[1] - 1)
    try_increase(data, focus[0], focus[1])
    try_increase(data, focus[0], focus[1] + 1)

    try_increase(data, focus[0] + 1, focus[1] - 1)
    try_increase(data, focus[0] + 1, focus[1])
    try_increase(data, focus[0] + 1, focus[1] + 1)


# ----------------------------------------------------------------------------------------------

def is_flash_simultaneous(data):
    for row in data:
        if any(i != 0 for i in row):
            return False
    return True


def part2():
    # f = ["5483143223",
    #     "2745854711",
    #     "5264556173",
    #     "6141336146",
    #     "6357385478",
    #     "4167524645",
    #     "2176841721",
    #     "6882881134",
    #     "4846848554",
    #     "5283751526"]
    f = open("11data", "r")
    data = []
    for row in f:
        tmp_row = []
        for fish in row.split("\n")[0]:
            tmp_row.append(int(fish))
        data.append(tmp_row)
    turns = turn_cycle2(data)
    print(turns)


def turn_cycle2(data):
    turns = 0
    while not is_flash_simultaneous(data):
        turns += 1
        exploding = []
        increase_all(data)
        while True:
            new_cycle = []
            find_exploding_fish(data, exploding, new_cycle)
            if not new_cycle:
                break
            for fish in new_cycle:
                increase_neighbours(data, fish)
            exploding.extend(new_cycle)
        for fish in exploding:
            data[fish[0]][fish[1]] = 0

    return turns


part1()
part2()
