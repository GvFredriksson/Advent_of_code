def calculate_1_4_7_8(data):
    one = 2
    four = 4
    seven = 3
    eight = 7
    digits = [one, four, seven, eight]
    total = 0
    for row in data:
        for digit in row[1]:
            if len(digit) in digits:
                total += 1
    return total


def part1():
    # f = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\n"\
    #       "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\n"\
    #       "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\n"\
    #       "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\n"\
    #       "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\n"\
    #       "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\n"\
    #       "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\n"\
    #       "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\n"\
    #       "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\n"\
    #       "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
    data = []
    # for line in f.split("\n"):
    #    line = line.split(" | ")
    #    data.append([line[0].split(" "), line[1].split(" ")])
    f = open("08data", "r")
    for line in f:
        line = line.split("\n")[0].split(" | ")
        data.append([line[0].split(" "), line[1].split(" ")])
    total = calculate_1_4_7_8(data)
    print(total)


def calculate_positions(data):
    a = None
    b = None
    c = None
    d = None
    e = None
    f = None
    g = None

    while True:
        for element in data[0]:
            if not f and not c:
                if len(element) == 2:
                    for element2 in data[0]:
                        if not a:
                            if len(element2) == 3:
                                for part in element2:
                                    if part not in element:
                                        a = part
                    for element2 in data[0]:
                        if len(element2) == 6:
                            if element[0] not in element2 or element[1] not in element2:
                                if element[0] not in element2:
                                    c = element[0]
                                    f = element[1]
                                else:
                                    f = element[0]
                                    c = element[1]
                                break
        for element in data[0]:
            if len(element) == 5 and a and a in element and c and c in element and f and f in element:
                for element2 in data[0]:
                    if len(element2) == 4:
                        for i in element2:
                            if i not in element:
                                b = i
                        for i in element:
                            if i != c and i != f:
                                if i in element2:
                                    d = i
                        for i in element:
                            if i != a and i != c and i != d and i != f:
                                g = i
            if a and b and c and d and f and g:
                if len(element) == 7:
                    for i in element:
                        if i != a and i != b and i != c and i != d and i != f and i != g:
                            e = i
        if a and b and c and d and e and f and g:
            break

    zero = [[a, b, c, e, f, g], "0"]
    one = [[c, f], "1"]
    two = [[a, c, d, e, g], "2"]
    three = [[a, c, d, f, g], "3"]
    four = [[b, c, d, f], "4"]
    five = [[a, b, d, f, g], "5"]
    six = [[a, b, d, e, f, g], "6"]
    seven = [[a, c, f], "7"]
    eight = [[a, b, c, d, e, f, g], "8"]
    nine = [[a, b, c, d, f, g], "9"]
    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    total = 0
    num = ""
    for numb in data[1]:
        for number in numbers:
            number_list = [i for i in numb]
            found = is_number(number[0], number_list)
            if found:
                num = num + number[1]
                break
    total += int(num)
    return total


def is_number(number, data):
    if len(number) == len(data):
        for i in data:
            if i not in number:
                return False
        return True
    return False

def part2():
    f = "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\n"\
          "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\n"\
          "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\n"\
          "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\n"\
          "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\n"\
          "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\n"\
          "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\n"\
          "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\n" \
          "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce\n" \
          "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"

    data = []
    #for line in f.split("\n"):
    #   line = line.split(" | ")
    #   data.append([line[0].split(" "), line[1].split(" ")])
    f = open("08data", "r")
    for line in f:
        line = line.split("\n")[0].split(" | ")
        data.append([line[0].split(" "), line[1].split(" ")])
    total = 0
    for row in data:
        total += calculate_positions(row)
    print(total)

#part1()
part2()

# 1068904 High
