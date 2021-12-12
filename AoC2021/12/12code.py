import numpy as np


def part1():
    f = ["fs-end",
         "he-DX",
         "fs-he",
         "start-DX",
         "pj-DX",
         "end-zg",
         "zg-sl",
         "zg-pj",
         "pj-he",
         "RW-he",
         "fs-DX",
         "pj-RW",
         "zg-RW",
         "start-pj",
         "he-WI",
         "zg-he",
         "pj-fs",
         "start-RW"]
    f = open("12data", "r")
    data = []
    for row in f:
        tmp = row.split("\n")[0].split("-")
        data.append([tmp[0], tmp[1]])
    paths = map_caves(data)
    traverse_caves(paths)


def unique_elements(data):
    tmp = []
    for row in data:
        tmp.extend(row)
    x = np.array(tmp)
    return np.unique(x)


def map_caves(data):
    paths = {}
    keys = unique_elements(data)
    print(keys)
    for key in keys:
        tmp = []
        for row in data:
            if row[0] == key and row[1] not in tmp:
                tmp.append(row[1])
            if row[1] == key and row[0] not in tmp:
                tmp.append(str(row[0]))
        paths[str(key)] = tmp
    return paths


def traverse_caves(paths):
    possible_paths = []
    start = "start"
    traverse_caves_aux(paths, possible_paths, [start])
    print(len(possible_paths))


def traverse_caves_aux(paths, possible_paths, traversed_path):
    directions = [i for i in paths[traversed_path[-1]] if i.isupper() or i not in traversed_path]
    for direction in directions:
        if direction == "end":
            possible_paths.append(traversed_path + [direction])
        else:
            traverse_caves_aux(paths, possible_paths, traversed_path + [direction])


# -----------------------------------------------------------------------------------------------------


def part2():
    f = ["fs-end",
         "he-DX",
         "fs-he",
         "start-DX",
         "pj-DX",
         "end-zg",
         "zg-sl",
         "zg-pj",
         "pj-he",
         "RW-he",
         "fs-DX",
         "pj-RW",
         "zg-RW",
         "start-pj",
         "he-WI",
         "zg-he",
         "pj-fs",
         "start-RW"]
    f = open("12data", "r")
    data = []
    for row in f:
        tmp = row.split("\n")[0].split("-")
        data.append([tmp[0], tmp[1]])
    paths = map_caves(data)
    traverse_caves2(paths)


def traverse_caves2(paths):
    possible_paths = []
    start = "start"
    traverse_caves_aux2(paths, possible_paths, [start], False)
    print(len(possible_paths))


def traverse_caves_aux2(paths, possible_paths, traversed_path, duplicate_small_cave):
    if duplicate_small_cave:
        directions = [i for i in paths[traversed_path[-1]] if i.isupper() or i not in traversed_path]
    else:
        directions = [i for i in paths[traversed_path[-1]] if i != "start"]
    for direction in directions:
        if direction == "end":
            possible_paths.append(traversed_path + [direction])
        else:
            tmp = duplicate_small_cave
            if not duplicate_small_cave:
                if not direction.isupper() and direction in traversed_path:
                    tmp = True
            traverse_caves_aux2(paths, possible_paths, traversed_path + [direction], tmp)



part1()
part2()
