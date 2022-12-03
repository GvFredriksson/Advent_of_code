import os


def read_data():
    data = []
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(__location__, '03data'))
    for row in f:
        data.append(row.split("\n")[0].strip(","))
    data[0] = data[0].strip("[")
    data[-1] = data[-1].strip("]")
    return data


def part1():
    a = []
    #a = read_data()



def part2():
    a = []
    #a = read_data()


part1()
print("---------------------")
part2()