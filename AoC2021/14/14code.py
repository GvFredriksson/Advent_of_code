def part1():
    f = ["NNCB",
         "",
         "CH -> B",
         "HH -> N",
         "CB -> H",
         "NH -> C",
         "HB -> C",
         "HC -> B",
         "HN -> C",
         "NN -> C",
         "BH -> H",
         "NC -> B",
         "NB -> B",
         "BN -> B",
         "BB -> N",
         "BC -> B",
         "CC -> N",
         "CN -> C"]
    f = open("14data", "r")
    data_pair = []
    data = []
    #start = f[0]
    start = f.readline().split("\n")[0]
    f.readline()
    for row in f: #[2:]:
        tmp = row.split("\n")[0].split(" -> ")
        data_pair.append(tmp[0])
        data.append(tmp[1])
    result = build_polymer(start, data_pair, data, 10)
    tmp = most_common(result)
    most = result.count(tmp)
    tmp = least_common(result)
    least = result.count(tmp)
    print(most-least)


def build_polymer(start, data_pair, data, step):
    for ste in range(step):
        tmp_polymer = ""
        for i in range(len(start)):
            try:
                pair = start[i] + start[i + 1]
            except IndexError:
                tmp_polymer += start[i]
            else:
                indx = data_pair.index(pair)
                tmp_polymer += (start[i] + data[indx])
        start = tmp_polymer
    return start


def unique_char(data):
    tmp = []
    for i in data:
        if i not in data:
            tmp.append(i)


def most_common(data):
    return max(set(data), key=data.count)


def least_common(data):
    return min(set(data), key=data.count)


# ----------------------------------------------------------------------------------------


def part2():
    f = open("14data", "r")
    input_data = f.readline().split("\n")[0]
    f.readline()
    rules = {}
    for row in f:
        x, y = row.split("\n")[0].split(' -> ')
        rules[x] = y
    counter = {}
    for i in range(len(input_data) - 1):
        x = input_data[i:i + 2]
        counter[x] = 1
    counter[input_data[-1]] = 1
    a = build_polymer2(40, rules, counter)
    print(a)


def build_polymer2(steps, rules, counter):
    print(rules)
    print(counter)
    for _ in range(steps):
        counter_tmp = {}
        for k, v in counter.items():
            if k in rules:
                y = rules[k]
                a = k[0] + y
                b = y + k[1]
                try:
                    counter_tmp[a] += v
                except KeyError:
                    counter_tmp[a] = v
                try:
                    counter_tmp[b] += v
                except KeyError:
                    counter_tmp[b] = v
            else:
                try:
                    counter_tmp[k] += v
                except KeyError:
                    counter_tmp[k] = v
        counter = counter_tmp
    total = {}
    for k, v in counter.items():
        try:
            total[k[0]] += v
        except KeyError:
            total[k[0]] = v
    lst = sorted(total.values())
    return lst[-1] - lst[0]


part1()
part2()
