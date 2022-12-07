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


def calculate_dirs(a):
    dirs = {}
    dirs["/"] = 0
    inside = []
    for i in a:
        if "$ cd" in i and ".." not in i:
            inside.append(i.split("$ cd ")[1])
        elif ".." in i:
            inside.pop(-1)
        elif "/" in i:
            inside = []
        elif "$" not in i and "dir" not in i:
            sum = int(i.split(" ")[0])
            for j in range(1, len(inside)+1):
                dirs["".join(inside[:j])] += sum
        elif "dir" in i:
            if "".join(inside)+i.split("dir ")[1] in dirs:
                print("How did this happen!?")
                print("".join(inside)+i.split("dir ")[1])
            dirs["".join(inside)+i.split("dir ")[1]] = 0
    return dirs


def part1():
    #a = read_data("data_test")
    a = read_data("data")
    dirs = calculate_dirs(a)

    ans = 0
    for dir in dirs:
        if dirs[dir] <= 100000:
            ans += dirs[dir]
    print(ans)

def part2():
    #a = read_data("data_test")
    a = read_data("data")
    dirs = calculate_dirs(a)

    current_size = 70000000 - dirs["/"]
    candidates = []
    for dir in dirs:
        if (current_size + dirs[dir]) >= 30000000:
            candidates.append(dirs[dir])
    candidates.sort()
    print(candidates[0])


part1()
print("---------------------")
part2()