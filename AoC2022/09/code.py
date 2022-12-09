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


def part1():
    #a = read_data("data_test")
    a = read_data("data")
    H = [0,0]
    T = [0,0]
    ans = [[0,0]]
    for i in a:
        sub_i = i.split(" ")
        dir = sub_i[0]
        for _ in range(0,int(sub_i[1])):
            if dir == "R":
                H[0] += 1
            if dir == "L":
                H[0] -= 1
            if dir == "U":
                H[1] += 1
            if dir == "D":
                H[1] -= 1
            if H[0] > T[0]+1 and H[1] == T[1]:
                T[0] += 1
            elif H[0] < T[0]-1 and H[1] == T[1]:
                T[0] -= 1
            elif H[1] > T[1]+1 and H[0] == T[0]:
                T[1] += 1
            elif H[1] < T[1]-1 and H[0] == T[0]:
                T[1] -= 1
            elif H[0] > T[0]+1 and H[1] > T[1] or H[0] > T[0] and H[1] > T[1]+1:
                T[0] += 1
                T[1] += 1
            elif H[0] > T[0]+1 and H[1] < T[1] or H[0] > T[0] and H[1] < T[1]-1:
                T[0] += 1
                T[1] -= 1
            elif H[0] < T[0]-1 and H[1] > T[1] or H[0] < T[0] and H[1] > T[1]+1:
                T[0] -= 1
                T[1] += 1
            elif H[0] < T[0]-1 and H[1] < T[1] or H[0] < T[0] and H[1] < T[1]-1:
                T[0] -= 1
                T[1] -= 1
            if T not in ans:
                ans.append([T[0],T[1]])
    print(len(ans))


def part2():
    #a = read_data("data_test")
    a = read_data("data")
    T = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    ans = [[0,0]]
    for i in a:
        sub_i = i.split(" ")
        dir = sub_i[0]
        for _ in range(0,int(sub_i[1])):
            if dir == "R":
                T[0][0] += 1
            if dir == "L":
                T[0][0] -= 1
            if dir == "U":
                T[0][1] += 1
            if dir == "D":
                T[0][1] -= 1
            for j in range(1,len(T)):
                if T[j-1][0] > T[j][0]+1 and T[j-1][1] == T[j][1]:
                    T[j][0] += 1
                elif T[j-1][0] < T[j][0]-1 and T[j-1][1] == T[j][1]:
                    T[j][0] -= 1
                elif T[j-1][1] > T[j][1]+1 and T[j-1][0] == T[j][0]:
                    T[j][1] += 1
                elif T[j-1][1] < T[j][1]-1 and T[j-1][0] == T[j][0]:
                    T[j][1] -= 1
                elif T[j-1][0] > T[j][0]+1 and T[j-1][1] > T[j][1] or T[j-1][0] > T[j][0] and T[j-1][1] > T[j][1]+1:
                    T[j][0] += 1
                    T[j][1] += 1
                elif T[j-1][0] > T[j][0]+1 and T[j-1][1] < T[j][1] or T[j-1][0] > T[j][0] and T[j-1][1] < T[j][1]-1:
                    T[j][0] += 1
                    T[j][1] -= 1
                elif T[j-1][0] < T[j][0]-1 and T[j-1][1] > T[j][1] or T[j-1][0] < T[j][0] and T[j-1][1] > T[j][1]+1:
                    T[j][0] -= 1
                    T[j][1] += 1
                elif T[j-1][0] < T[j][0]-1 and T[j-1][1] < T[j][1] or T[j-1][0] < T[j][0] and T[j-1][1] < T[j][1]-1:
                    T[j][0] -= 1
                    T[j][1] -= 1
            if T[9] not in ans:
                ans.append([T[9][0],T[9][1]])
    print(len(ans))


part1()
print("---------------------")
part2()