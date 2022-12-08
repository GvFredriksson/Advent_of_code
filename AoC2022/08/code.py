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


def get_col(a, y):
    col = []
    for i in a:
        col.append(i[y])
    return col


def is_big_tree(tree, trees):
    for t in trees:
        if int(tree) <= int(t):
            return False
    return True


def trees_in_view(tree, trees):
    ans = 0
    for t in trees:
        if int(tree) > int(t):
            ans += 1
        else:
            return ans + 1
    return ans


def convert(string):
    list1 = []
    list1[:0] = string
    return list1


def part1():
    #a = read_data("data_test")
    a = read_data("data")
    visible = len(a)*2 + len(a[0])*2 - 4

    for i in range(1, len(a)-1):
        x = convert(a[i])
        for y in range(1, len(x)-1):
            col = get_col(a,y)
            if is_big_tree(x[y], x[:y]):
                visible += 1
            elif is_big_tree(x[y], x[y+1:]):
                visible += 1
            elif is_big_tree(x[y], col[:i]):
                visible += 1
            elif is_big_tree(x[y], col[i+1:]):
                visible += 1
    print(visible)


def part2():
    #a = read_data("data_test")
    a = read_data("data")
    max_trees = 0
    for i in range(1, len(a)-1):
        x = convert(a[i])
        for y in range(1, len(x)-1):
            col = get_col(a,y)
            reordered_row = x[:y]
            reordered_row.reverse()
            sum = trees_in_view(x[y], reordered_row)
            sum *= trees_in_view(x[y], x[y+1:])
            reordered_col = col[:i]
            reordered_col.reverse()
            sum *= trees_in_view(x[y], reordered_col)
            sum *= trees_in_view(x[y], col[i+1:])
            if sum > max_trees:
                max_trees = sum
    print(max_trees)


part1()
print("---------------------")
part2()