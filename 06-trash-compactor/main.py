def main():
    input: str = ""
    with open("input.txt", "r") as file:
        input = file.read()

    lines = input.splitlines()

    last_line = lines[-1]
    ops: list[str] = []
    col_ranges: list[tuple[int, int]] = []
    start = 0
    end = 0
    for i, char in enumerate(last_line):
        if i == 0:
            ops.append(char)
            continue
        if char != " ":
            ops.append(char)
            end = i - 2
            col_ranges.append((start, end))
            start = i
        if i == len(last_line) - 1:
            end = i
            col_ranges.append((start, end))

    cols_1: list[list[int]] = []
    for start, end in col_ranges:
        col: list[int] = []
        for line in lines[:-1]:
            digits = line[start : end + 1].strip()
            col.append(int(digits))

        cols_1.append(col)

    total_1 = 0
    for i, op in enumerate(ops):
        col = cols_1[i]
        if op == "*":
            result = 1
            for num in col:
                result *= num
            total_1 += result
        elif op == "+":
            total_1 += sum(col)

    print("Result 1: ", total_1)

    cols_2: list[list[int]] = []
    for start, end in col_ranges:
        col: list[int] = []
        for i in range(start, end + 1):
            digits = ""
            for line in lines[:-1]:
                digits += line[i]
            col.append(int(digits.strip()))

        cols_2.append(col)

    total_2 = 0
    for i, op in enumerate(ops):
        col = cols_2[i]
        if op == "*":
            result = 1
            for num in col:
                result *= num
            total_2 += result
        elif op == "+":
            total_2 += sum(col)

    print("Result 2: ", total_2)

    return


if __name__ == "__main__":
    main()
