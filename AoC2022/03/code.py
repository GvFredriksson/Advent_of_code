import os
import string


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


value = {}

def populate_value():
    weight = 1
    for i in string.ascii_letters:
        value[i] = weight
        weight += 1


def part1():
    #a = read_data("data_test")
    a = read_data("data")
    sum = 0
    for i in a:
        i_1 = i[:(len(i)//2)]
        i_2 = i[len(i)//2:len(i)]
        for x in i_1:
            if x in i_2:
                sum += value[x]
                break
    print(sum)



def part2():
    #a = read_data("data_test")
    a = read_data("data")
    sum = 0
    for i in range(0,len(a),3):
        for x in a[i]:
            if x in a[i+1] and x in a[i+2]:
                sum += value[x]
                break
    print(sum)


populate_value()
part1()
print("---------------------")
part2()