def run_lifecycle(days, data):
    for _ in range(0, days):
        new_population = []
        for fish in data:
            if fish == 0:
                new_population.append(6)
                new_population.append(8)
            else:
                new_population.append(fish - 1)
        data = new_population
    return new_population


def run_lifecycle_int(days, population):
    zeros = population.count(0)
    ones = population.count(1)
    twos = population.count(2)
    trees = population.count(3)
    fours = population.count(4)
    fives = population.count(5)
    sixes = population.count(6)
    sevens = population.count(7)
    eights = population.count(8)

    for day in range(days):
        print(day)
        tmp = zeros
        zeros = ones
        ones = twos
        twos = trees
        trees = fours
        fours = fives
        fives = sixes
        sixes = sevens + tmp
        sevens = eights
        eights = tmp
    return zeros + ones + twos + trees + fours + fives + sixes + sevens + eights



def part1():
    # f = open("06data", "r")
    # tmp = f.readline().split(",")
    tmp = [3, 4, 3, 1, 2]
    data = []
    for fish in tmp:
        data.append(int(fish))
    populations = run_lifecycle(80, data)
    total = 0
    for population in populations:
        total += len(population)
    print(total)


def part2():
    f = open("06data", "r")
    tmp = f.readline().split(",")
    #tmp = [3, 4, 3, 1, 2]
    data = []

    for fish in tmp:
        data.append(int(fish))
    #current_population = run_lifecycle_improved(256, data)
    #print(len(current_population))
    final_population = run_lifecycle_int(256, data)
    print(final_population)


# part1()
part2()
