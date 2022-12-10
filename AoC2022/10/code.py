import os


def read_data(name):
    data = []
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(__location__, name))
    for row in f:
        data.append(row.split("\n")[0].strip(","))
    data[0] = data[0].strip("[")
    data[-1] = data[-1].strip("]")
    return data


def part1():
    #a = read_data("data_test")
    a = read_data("data")
    cycles = 0
    x = 1
    key_cycles = [20,60,100,140,180,220]
    sums = []
    for i in a:
        input = i.split(" ")
        if input[0] == "addx":
            cycles += 1
            if cycles in key_cycles:
                sums.append(cycles*x)
            cycles += 1
            if cycles in key_cycles:
                sums.append(cycles*x)
            x += int(input[1])
        else:
            cycles += 1
            if cycles in key_cycles:
                sums.append(cycles*x)
    ans = 0
    for i in sums:
        ans += i
    print(ans)
            


def part2():
    #a = read_data("data_test")
    a = read_data("data")
    cycles = 0
    x = 1
    key_cycles = [40,80,120,160,200,240]
    image = []
    for i in key_cycles:
        image.append(["."]*40)
    for i in a:
        input = i.split(" ")
        if input[0] == "addx":
            cycles += 1
            draw_img(image, cycles, x)
            cycles += 1
            draw_img(image, cycles, x)
            x += int(input[1])
        else:
            cycles += 1
            draw_img(image, cycles, x)
    for i in image:
        print(i)


def draw_img(image, cycles, x):
    row = int(cycles/40)
    col = (cycles%40) - 1
    if x-1 == col or x == col or x+1 == col:
        print("ROW: " + str(row))
        print("COL: " + str(col))
        image[row][col] = "#"
    return draw_img



part1()
print("---------------------")
part2()