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
    sum = 0
    for i in a:
        b = i.split(",")
        c = b[0].split("-")
        d = b[1].split("-")
        if int(c[0]) >= int(d[0]) and int(c[1]) <= int(d[1]):
            sum += 1
        elif int(c[0]) <= int(d[0]) and int(c[1]) >= int(d[1]):
            sum += 1
    print(sum)


def part2():
    #a = read_data("data_test")
    a = read_data("data")
    sum = 0
    for i in a:
        b = i.split(",")
        c = b[0].split("-")
        d = b[1].split("-")
        if int(c[0]) >= int(d[0]) and int(c[0]) <= int(d[1]) or int(c[1]) >= int(d[0]) and int(c[1]) <= int(d[1]):
            sum += 1
        elif int(c[0]) <= int(d[0]) and int(c[1]) >= int(d[0]) or int(c[0]) <= int(d[1]) and int(c[1]) >= int(d[1]):
            sum += 1
    print(sum)



part1()
print("---------------------")
part2()