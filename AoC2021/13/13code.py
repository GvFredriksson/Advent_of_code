import re


def part1():
    f = ["6,10",
         "0,14",
         "9,10",
         "0,3",
         "10,4",
         "4,11",
         "6,0",
         "6,12",
         "4,1",
         "0,13",
         "10,12",
         "3,4",
         "3,0",
         "8,4",
         "1,10",
         "2,14",
         "8,10",
         "9,0",
         "",
         "fold along y=7",
         "fold along x=5"]
    f = open("13data", "r")
    dots = []
    folds = []
    for row in f:
        if row == "\n":
            break
        tmp = row.split("\n")[0].split(",")
        dots.append([int(tmp[0]), int(tmp[1])])
    for row in f:
        if not re.findall("^fold along", row):
            continue
        tmp = row.split("fold along ")[1].split("=")
        folds.append([tmp[0], int(tmp[1])])
    fold(dots, [folds[0]])
    print(len(unique_elements(dots)))


def unique_elements(data):
    tmp = []
    for i in data:
        if i not in tmp:
            tmp.append(i)
    return tmp


def fold(dots, folds):
    for fol in folds:
        if fol[0] == "y":
            direction = "up"
        else:
            direction = "left"
        for dot_pos in range(len(dots)):
            if direction == "left" and dots[dot_pos][0] > fol[1]:
                dots[dot_pos][0] = fol[1] - (dots[dot_pos][0] - fol[1])
            if direction == "up" and dots[dot_pos][1] > fol[1]:
                dots[dot_pos][1] = fol[1] - (dots[dot_pos][1] - fol[1])


# ---------------------------------------------------------------------------------------------

def part2():
    f = open("13data", "r")
    dots = []
    folds = []
    for row in f:
        if row == "\n":
            break
        tmp = row.split("\n")[0].split(",")
        dots.append([int(tmp[0]), int(tmp[1])])
    for row in f:
        if not re.findall("^fold along", row):
            continue
        tmp = row.split("fold along ")[1].split("=")
        folds.append([tmp[0], int(tmp[1])])
    fold(dots, folds)
    paint_code(dots)


def paint_code(dots):
    y_max = 0
    x_max = 0
    y_min = 0
    x_min = 0
    for i in dots:
        if i[0] > y_max:
            y_max = i[0]
        if i[1] > x_max:
            x_max = i[1]
    for x in range(x_min, x_max + 1, 1):
        row = []
        for y in range(y_min, y_max + 1, 1):
            if [y, x] in dots:
                row.append("#")
            else:
                row.append(".")
        print(row)


part1()
part2()
