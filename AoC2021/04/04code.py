def part1():
    f = open("04data", "r")
    bingo_input = f.readline()
    f.readline()
    print(bingo_input)
    bingo_sheets = []
    bingo_sheets_ans = []
    for line in f:
        bingo_sheet = []
        bingo_sheet_ans = []
        for i in range(0, 5, 1):
            bingo_row = []
            bingo_row_ans = []
            for number in line.split("\n")[0].split(" "):
                if not number:
                    continue
                bingo_row.append(number)
                bingo_row_ans.append(False)
            bingo_sheet.append(bingo_row)
            bingo_sheet_ans.append(bingo_row_ans)
            line = f.readline()
        bingo_sheets.append(bingo_sheet)
        bingo_sheets_ans.append(bingo_sheet_ans)

    winner, winner_ans, last_num = run_bingo(bingo_input, bingo_sheets, bingo_sheets_ans)

    ans = 0
    for row in range(len(winner_ans)):
        for num in range(len(winner_ans[row])):
            if not winner_ans[row][num]:
                ans += int(winner[row][num])
    print(ans * int(last_num))


def run_bingo(bingo_input, bingo_sheets, bingo_sheets_ans):
    for bingo_number in bingo_input.split(","):
        for sheet in range(len(bingo_sheets)):
            for row in range(len(bingo_sheets[sheet])):
                for bingo_num in range(len(bingo_sheets[sheet][row])):
                    if bingo_sheets[sheet][row][bingo_num] == bingo_number:
                        bingo_sheets_ans[sheet][row][bingo_num] = True
                        winner = validate_victory(bingo_sheets_ans)
                        if winner:
                            return bingo_sheets[sheet], winner, bingo_number


# --------------------------------------------------------------------------------------

def part2():
    run_bingo_base(run_bingo_iter)


def run_bingo_base(func):
    f = open("04data", "r")
    bingo_input = f.readline()
    f.readline()
    print(bingo_input)
    bingo_sheets = []
    bingo_sheets_ans = []
    for line in f:
        bingo_sheet = []
        bingo_sheet_ans = []
        for i in range(0, 5, 1):
            bingo_row = []
            bingo_row_ans = []
            for number in line.split("\n")[0].split(" "):
                if not number:
                    continue
                bingo_row.append(number)
                bingo_row_ans.append(False)
            bingo_sheet.append(bingo_row)
            bingo_sheet_ans.append(bingo_row_ans)
            line = f.readline()
        bingo_sheets.append(bingo_sheet)
        bingo_sheets_ans.append(bingo_sheet_ans)

    winner, winner_ans, last_num = func(bingo_input, bingo_sheets, bingo_sheets_ans)
    ans = 0
    for row in range(len(winner_ans)):
        for num in range(len(winner_ans[row])):
            if not winner_ans[row][num]:
                ans += int(winner[row][num])
    print(ans * int(last_num))


def run_bingo_iter(bingo_input, bingo_sheets, bingo_sheets_ans):
    bingo_numbers = bingo_input.split(",")
    win_sheets = []

    for sheet in range(len(bingo_sheets)):
        win_sheets.append(False)
    for bingo_number in bingo_numbers:
        for sheet in range(len(bingo_sheets)):
            iter_sheet(bingo_sheets[sheet], bingo_sheets_ans[sheet], bingo_number)
        win_sheets, new_wins = populate_win_sheet(bingo_sheets_ans, win_sheets)
        if False not in win_sheets:
            return bingo_sheets[new_wins[-1]], bingo_sheets_ans[new_wins[-1]], bingo_number


def iter_sheet(bingo_sheet, bingo_sheet_ans, bingo_number):
    for row in range(len(bingo_sheet)):
        iter_row(bingo_sheet[row], bingo_sheet_ans[row], bingo_number)


def iter_row(row, row_ans, bingo_number):
    for pos in range(len(row)):
        if row[pos] == bingo_number:
            row_ans[pos] = True


def populate_win_sheet(bingo_sheets_ans, win_sheets):
    # Find if any row or column is all True
    new_wins = []
    for sheet in range(len(bingo_sheets_ans)):
        if not win_sheets[sheet]:
            for i in range(len(bingo_sheets_ans[sheet][0])):
                ans_row = validate_iterable(bingo_sheets_ans[sheet][i])
                ans_col = validate_iterable(
                    [bingo_sheets_ans[sheet][0][i], bingo_sheets_ans[sheet][1][i], bingo_sheets_ans[sheet][2][i],
                     bingo_sheets_ans[sheet][3][i], bingo_sheets_ans[sheet][4][i]])
                if ans_row or ans_col:
                    new_wins.append(sheet)
                    win_sheets[sheet] = True
    return win_sheets, new_wins


def validate_victory(bingo_sheets_ans, win_sheets):
    # Find if any row or column is all True
    for sheet in range(len(bingo_sheets_ans)):
        if not win_sheets[sheet]:
            for i in range(len(bingo_sheets_ans[sheet][0])):
                ans_row = validate_iterable(bingo_sheets_ans[sheet][i])
                ans_col = validate_iterable(
                    [bingo_sheets_ans[sheet][0][i], bingo_sheets_ans[sheet][1][i], bingo_sheets_ans[sheet][2][i],
                     bingo_sheets_ans[sheet][3][i], bingo_sheets_ans[sheet][4][i]])
                if ans_row or ans_col:
                    return sheet
    return False


def validate_iterable(iterr):
    for i in iterr:
        if not i:
            return False
    return True


part1()
part2()
