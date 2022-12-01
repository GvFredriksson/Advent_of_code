import os

def read_data():
    data = []
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(__location__, '01data'))
    for row in f:
        data.append(row.split("\n")[0].strip(","))
    data[0] = data[0].strip("[")
    data[-1] = data[-1].strip("]")
    return data

def part1():
    #a = ["1000","2000","3000","","4000","","5000","6000","","7000","8000","9000","","10000"]
    a = read_data()
    top = 0
    count = 0
    for i in a:
        if i == "":
            if count > top:
                top = count
            count = 0
        else:
            count += int(i)
    print(top)

def part2():
    #a = ["1000","2000","3000","","4000","","5000","6000","","7000","8000","9000","","10000"]
    a = read_data()
    top3 = [0,0,0]
    count = 0
    for i in a:
        if i == "":
            top3 = part2iter(count, top3)
            count = 0
        else:
            count += int(i)
    top3 = part2iter(count, top3)
    count = 0

    print(top3)
    print(top3[0]+top3[1]+top3[2])

def part2iter(count, top3):
    if count > top3[0]:
        if count > top3[1]:
            if count > top3[2]:
                top3[0] = top3[1]
                top3[1] = top3[2]
                top3[2] = count
            else:
                top3[0] = top3[1]
                top3[1] = count
        else:
            top3[0] = count
    return top3

part1()
print("---------------------")
part2()