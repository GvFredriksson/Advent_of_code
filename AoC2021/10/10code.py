def part1():
    # data = ["[({(<(())[]>[[{[]{<()<>>",
    #         "[(()[<>])]({[<{<<[]>>(",
    #         "{([(<{}[<>[]}>{[]{[(<()>",
    #         "(((({<>}<{<{<>}{[]{[]{}",
    #         "[[<[([]))<([[{}[[()]]]",
    #         "[{[{({}]{}}([{[{{{}}([]",
    #         "{<[[]]>}<{[{[{[]{()[[[]",
    #         "[<(<(<(<{}))><([]([]()",
    #         "<{([([[(<>()){}]>(<<{{",
    #         "<{([{{}}[<[[[<>{}]]]>[]]"]
    data = []
    f = open("10data", "r")
    for row in f:
        data.append(row.split("\n")[0])
    errors = []
    point_values = [3, 57, 1197, 25137]
    close_brackets = [")", "]", "}", ">"]
    for row in data:
        error = validate_row(row)
        if error:
            errors.append(error)
    total = errors.count(close_brackets[0]) * point_values[0] + \
            errors.count(close_brackets[1]) * point_values[1] + \
            errors.count(close_brackets[2]) * point_values[2] + \
            errors.count(close_brackets[3]) * point_values[3]
    print(errors)
    print(total)


def validate_row(row):
    open_bracket = []
    open_brackets = ["(", "[", "{", "<"]
    close_brackets = [")", "]", "}", ">"]
    for bracket in row:
        if bracket in open_brackets:
            open_bracket.append(bracket)
        else:
            pos_close = close_brackets.index(bracket)
            pos_open = open_brackets.index(open_bracket[-1])
            if pos_close == pos_open:
                open_bracket.pop()
            else:
                return bracket


# -----------------------------------------Part 2-----------------------------------------------------------


def validate_row2(row):
    open_brackets = ["(", "[", "{", "<"]
    close_brackets = [")", "]", "}", ">"]
    open_bracket = []
    for bracket in row:
        if bracket in open_brackets:
            open_bracket.append(bracket)
        else:
            pos_close = close_brackets.index(bracket)
            pos_open = open_brackets.index(open_bracket[-1])
            if pos_close == pos_open:
                open_bracket.pop()
            else:
                return
    missing_brackets = []
    for bracket in range(len(open_bracket)-1, -1, -1):
        pos_open = open_brackets.index(open_bracket[bracket])
        missing_brackets.append(pos_open)
    return missing_brackets


def part2():
    # data = ["[({(<(())[]>[[{[]{<()<>>",
    #         "[(()[<>])]({[<{<<[]>>(",
    #         "{([(<{}[<>[]}>{[]{[(<()>",
    #         "(((({<>}<{<{<>}{[]{[]{}",
    #         "[[<[([]))<([[{}[[()]]]",
    #         "[{[{({}]{}}([{[{{{}}([]",
    #         "{<[[]]>}<{[{[{[]{()[[[]",
    #         "[<(<(<(<{}))><([]([]()",
    #         "<{([([[(<>()){}]>(<<{{",
    #         "<{([{{}}[<[[[<>{}]]]>[]]"]
    data = []
    f = open("10data", "r")
    for row in f:
        data.append(row.split("\n")[0])
    point_values = [1, 2, 3, 4]
    missing_brackets = []
    for row in data:
        correct = validate_row2(row)
        if correct:
            missing_brackets.append(correct)
    scores = []
    for row in missing_brackets:
        total = 0
        for bracket in row:
            total = total * 5 + point_values[bracket]
        scores.append(total)
    scores.sort()
    print(scores)
    print(scores[int((len(scores)-1)/2)])


part1()
part2()
