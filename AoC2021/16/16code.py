def part1_2():
    f = open("16data", "r")
    data = f.readline().strip()

    binary = parse_hex(data)
    print(binary)
    print(len(binary))
    pos = 0
    pos, version_total, value = read_binary(binary, pos)
    print(f"VERSION TOTALE : {version_total}")
    print(f"Value: {value}")


def read_binary(binary, pos):
    version, pos = read_bits(binary, pos, 3)
    version_total = version
    type_id, pos = read_bits(binary, pos, 3)
    value = 0
    if type_id == 4:
        # literal value
        value_mp = []
        while True:
            i, pos = binary[pos], pos + 1
            numbr, pos = read_bits(binary, pos, 4)
            value_mp.append(numbr)
            if i == "0":
                break
        tmp_val = 0
        for val in value_mp:
            tmp_val = tmp_val*16 + val
        value = tmp_val
    else:
        # operator
        tmp_value = []
        switch, pos = read_bits(binary, pos, 1)
        if switch == 0:
            # the next 15 bits are a number that represents the total length in bits of the sub-packets contained
            bit_len = 15
            option, pos = read_bits(binary, pos, bit_len)
            stop = option + pos
            while pos < stop:
                pos, version_tmp, tmp = read_binary(binary, pos)
                tmp_value.append(tmp)
                version_total += version_tmp
        else:
            # the next 11 bits are a number that represents the number of sub-packets immediately contained
            bit_len = 11
            option, pos = read_bits(binary, pos, bit_len)
            for i in range(option):
                pos, version_tmp, tmp = read_binary(binary, pos)
                tmp_value.append(tmp)
                version_total += version_tmp
        if type_id == 0:
            # sum
            value = sum(tmp_value)
        if type_id == 1:
            # product
            value = 1
            for i in tmp_value:
                value *= i
        if type_id == 2:
            # minimum
            value = min(tmp_value)
        if type_id == 3:
            # maximum
            value = max(tmp_value)
        if type_id == 5:
            # greater than
            if tmp_value[0] > tmp_value[1]:
                value = 1
            else:
                value = 0
        if type_id == 6:
            # less than
            if tmp_value[0] < tmp_value[1]:
                value = 1
            else:
                value = 0
        if type_id == 7:
            # equal to
            if tmp_value[0] == tmp_value[1]:
                value = 1
            else:
                value = 0
    return pos, version_total, value


def read_bits(binary, pos, numbr):
    return int(binary[pos: pos + numbr], 2), pos + numbr


def read_bit(binary, pos, numbr):
    return binary[pos: pos + numbr], pos + numbr


def parse_hex(row):
    bits = []
    for hex in row:
        he = int(hex, 16)
        bi = bin(he)[2:]
        bi = '0' * (4 - len(bi)) + bi
        for bit in bi:
            bits.append(bit)
    return ''.join(bits)


part1_2()
