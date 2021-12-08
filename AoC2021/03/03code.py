def part1():
    f = open("03data", "r")
    concatenation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    tmp = 0
    for row in f:
        tmp += 1
        for i in range(0, len(row) - 1):
            concatenation[i] += int(row[i])
    tmp = tmp / 2
    gamma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    epsilon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(concatenation)):
        if concatenation[i] > tmp:
            gamma[i] = 1
            epsilon[i] = 0
        else:
            gamma[i] = 0
            epsilon[i] = 1
    gamma_int = 0
    for bit in gamma:
        gamma_int = (gamma_int << 1) | bit
    epsilon_int = 0
    for bit in epsilon:
        epsilon_int = (epsilon_int << 1) | bit
    print(gamma_int * epsilon_int)


def part2():
    f = open("03data", "r")
    data = []
    for x in f:
        data.append(x)
    oxygen = iterate_data(data)
    co2 = iterate_data(data, reverse=True)
    life_support = int(oxygen[0], 2) * int(co2[0], 2)
    print(oxygen)
    print(co2)
    print(int(oxygen[0], 2))
    print(int(co2[0], 2))
    print(life_support)


def make_int_from_bit_list(bit_list):
    out = 0
    for bit in bit_list:
        out = (out << 1) | bit
    return out


def iterate_data(data, reverse=False):
    bit_position = 0
    while len(data) > 1:
        zeroes, onces = count_bit_place(data=data, bit_position=bit_position)
        if reverse:
            if not (zeroes > onces):
                focus = "0"
            else:
                focus = "1"
        else:
            if zeroes > onces:
                focus = "0"
            else:
                focus = "1"
        data = split_list(data=data, focus=focus, bit_position=bit_position)
        bit_position += 1
    return data


def split_list(data, focus, bit_position):
    new_data = []
    for row in data:
        if row[bit_position] == focus:
            new_data.append(row)
    return new_data


def count_bit_place(data, bit_position, reverse=False):
    zeroes = 0
    onces = 0
    for row in data:
        if row[bit_position] == "0":
            if reverse:
                onces += 1
            else:
                zeroes += 1
        else:
            if reverse:
                zeroes += 1
            else:
                onces += 1
    return zeroes, onces


print("-----Part1-----")
part1()
print("-----Part2-----")
part2()
