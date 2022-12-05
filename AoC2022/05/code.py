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


def build_stacks(a,i,stacks):
    b = a[i].split(" ")
    for x in b:
        if x != "":
            stacks.append([])
    for j in range(0, i):
        start = 0
        stop = 0
        for g in range(0,len(stacks)):
            stop += 4
            if (a[j])[start:stop].strip() != "":
                stacks[g].append((a[j])[start+1:start+2])
            start += 4


def part1():
    #a = read_data("data_test")
    a = read_data("data")
    stacks = []
    for i in range(len(a)):
        if a[i][:2] == " 1":
            build_stacks(a,i,stacks)
        if a[i][:4] == "move":
            b = a[i].split(" to ")
            c = b[0].split("move ")[1].split(" from ")
            amount = int(c[0])
            source = int(c[1]) -1
            dest = int(b[1]) -1
            for _ in range(0,amount):
                stacks[dest].insert(0,stacks[source][0])
                stacks[source].pop(0)
    ans = ""
    for stack in stacks:
        ans += stack[0]
    print(ans)


def part2():
    #a = read_data("data_test")
    a = read_data("data")
    stacks = []
    for i in range(len(a)):
        if a[i][:2] == " 1":
            build_stacks(a,i,stacks)
        if a[i][:4] == "move":
            b = a[i].split(" to ")
            c = b[0].split("move ")[1].split(" from ")
            amount = int(c[0])
            source = int(c[1]) -1
            dest = int(b[1]) -1
            stacks[dest] = stacks[source][:amount] + stacks[dest]
            for _ in range(0,amount):
                stacks[source].pop(0)
    ans = ""
    for stack in stacks:
        ans += stack[0]
    print(ans)


part1()
print("---------------------")
part2()