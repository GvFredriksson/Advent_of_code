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

class Monkey:
    items = []
    operation = []
    test = ""
    true_dest = 0
    false_dest = 0
    inspected_items = 0


def prepare_monkeys(a):
    monkeys = []
    monkey = Monkey
    for i in a:
        input = i.strip().split(" ")
        if input[0] == "Starting":
            tmp = i.replace(" ", "")
            items = tmp.split(":")
            monkey.items = items[1].split(",")
            for j in range(len(monkey.items)):
                monkey.items[j] = int(monkey.items[j])
        if input[0] == "Operation:":
            monkey.operation = [input[4],input[5]]
        elif input[0] == "Test:":
            monkey.test = int(input[3])
        elif input[0] == "If":
            if input[1] == "true:":
                monkey.true_dest = int(input[5])
            elif input[1] == "false:":
                monkey.false_dest = int(input[5])
        if i == "":
            monkey.inspected_items = 0
            monkeys.append(monkey)
            monkey = Monkey()
    monkeys.append(monkey)
    modulo = 1
    for i in range(len(monkeys)):
        monkeys[i].inspected_items = 0
        modulo *= monkeys[i].test
    return(monkeys, modulo)


def round(monkeys, calm, modulo=1):
    for monkey in monkeys:
        #print(monkey.items)
        for item in monkey.items:
            value = item if monkey.operation[1] == "old" else int(monkey.operation[1])
            if monkey.operation[0] == "+":
                item = int(item) + value
            else:
                item *= value
                item = item % modulo
            if calm:
                item = int(item/3)
            if int(item)%monkey.test == 0:
                monkeys[monkey.true_dest].items.append(item)
            else:
                monkeys[monkey.false_dest].items.append(item)
            monkey.inspected_items += 1
        monkey.items = []
    return monkeys


def part1():
    #a = read_data("data_test")
    a = read_data("data")
    monkeys, modulo = prepare_monkeys(a)
    for _ in range(20):
        monkeys = round(monkeys, calm=True, modulo=modulo)
    monkeys.sort(key=lambda x: x.inspected_items, reverse=True)
    print(monkeys[0].inspected_items * monkeys[1].inspected_items)


def part2():
    #a = read_data("data_test")
    a = read_data("data")
    monkeys, modulo = prepare_monkeys(a)
    for _ in range(10000):
        monkeys = round(monkeys, calm=False, modulo=modulo)
    monkeys.sort(key=lambda x: x.inspected_items, reverse=True)
    print(monkeys[0].inspected_items * monkeys[1].inspected_items)


part1()
print("---------------------")
part2()
