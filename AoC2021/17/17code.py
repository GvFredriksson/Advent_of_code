def part1_2():
    f = open("17data", "r")
    data = f.readline().strip().split("target area: x=")[1]
    data = data.split(", y=")
    target_y = data[1].split("..")
    target_y = [int(target_y[0]), int(target_y[1])]
    target_x = data[0].split("..")
    target_x = [int(target_x[0]), int(target_x[1])]

    x = find_x_vel(target_x)
    y = find_y_vel(target_y)
    max_y = sum_y(y[-1])
    print(max_y)
    pairs = find_correct_pairs(target_x, target_y, x, y)
    print(pairs)
    print(len(pairs))


def sum_y(y):
    max_y = 0
    velocity = y
    while velocity > 0:
        max_y += velocity
        velocity -= 1
    return max_y


def find_x_vel(target_x):
    posible_x = []
    for i in range(0, 1000, 1):
        vel = i
        pos = 0
        while True:
            pos += vel
            if target_x[0] <= pos <= target_x[1]:
                posible_x.append(i)
                break
            if vel < 0:
                vel += 1
            else:
                vel -= 1
            if pos > target_x[1] or vel == 0:
                break
    return posible_x


def find_y_vel(target_y):
    posible_y = []
    for i in range(-1000, 1000, 1):
        vel = i
        pos = 0
        while True:
            pos += vel
            if target_y[0] <= pos <= target_y[1]:
                posible_y.append(i)
                break
            vel -= 1
            if target_y[0] > pos:
                break
    return posible_y


def find_correct_pairs(target_x, target_y, xs, ys):
    start_accs = []
    for x in xs:
        for y in ys:
            if launch([x, y], target_x, target_y):
                start_accs.append((x, y))
    return start_accs


def launch(acc, target_x, target_y):
    pos = [0, 0]
    while True:
        if target_x[0] <= pos[0] <= target_x[1] and target_y[0] <= pos[1] <= target_y[1]:
            return True
        pos[0] += acc[0]
        pos[1] += acc[1]
        if pos[0] > target_x[1] or pos[1] < target_y[0]:
            return False
        if acc[0] < 0:
            acc[0] += 1
        if acc[0] > 0:
            acc[0] -= 1
        acc[1] -= 1

    return False


part1_2()
