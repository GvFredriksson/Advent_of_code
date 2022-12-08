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


def part2():
    #a = read_data("data_test")
    a = read_data("data")



part1()
print("---------------------")
part2()