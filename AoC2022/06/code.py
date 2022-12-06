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
    a = read_data("data")[0]
    for i in range(0, len(a), 1):
        if i > 2:
            if a[i] != a[i-1] and a[i] != a[i-2] and a[i] != a[i-3]:
                if a[i-1] != a[i-2] and a[i-1] != a[i-3]:
                    if a[i-2] != a[i-3]:
                        print(i+1)
                        return


def part2():
    #a = read_data("data_test")
    a = read_data("data")[0]
    for i in range(0, len(a), 1):
        if i > 13:
            if isUniqueString(a[i-14:i]):
                print(i)
                return


def isUniqueString(st):
    chars = []

    for i in range(0, len(st)):
        if st[i] in chars:
            return False
 
        chars.append(st[i])
    return True



part1()
print("---------------------")
part2()