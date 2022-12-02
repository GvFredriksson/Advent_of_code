def read_data():
    data = []
    f = open("C:/Users/GvFre/Github/Advent_of_code/AoC2022/02/02data", "r")
    for row in f:
        data.append(row.split("\n")[0].strip(","))
    data[0] = data[0].strip("[")
    data[-1] = data[-1].strip("]")
    return data

def part1():
    #X = Rock
    #Y = Paper
    #Z = Scissors
    #a = ["A Y", "B X", "C Z"]
    a = read_data()
    score = 0
    for i in a:
        if i[2] == "X":
            score += 1
            if i[0] == "A":
                score += 3
            if i[0] == "C":
                score += 6
        if i[2] == "Y":
            score += 2
            if i[0] == "B":
                score += 3
            if i[0] == "A":
                score += 6
        if i[2] == "Z":
            score += 3
            if i[0] == "C":
                score += 3
            if i[0] == "B":
                score += 6
    print(score)


def part2():
    #X = lose
    #Y = Draw
    #Z = Win
    #a = ["A Y", "B X", "C Z"]
    a = read_data()
    score = 0
    for i in a:
        if i[2] == "X":
            if i[0] == "A":
                score += 3
            if i[0] == "B":
                score += 1
            if i[0] == "C":
                score += 2
        if i[2] == "Y":
            score += 3
            if i[0] == "A":
                score += 1
            if i[0] == "B":
                score += 2
            if i[0] == "C":
                score += 3
        if i[2] == "Z":
            score += 6
            if i[0] == "A":
                score += 2
            if i[0] == "B":
                score += 3
            if i[0] == "C":
                score += 1
    print(score)

part1()
print("---------------------")
part2()