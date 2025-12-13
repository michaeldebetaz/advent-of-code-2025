def main():
    input: str = ""
    with open("test.txt", "r") as file:
        input = file.read().strip()

    lines = input.splitlines()

    last_line = lines[-1]
    col_ranges: list[tuple[int, int]] = []
    start = 0
    end = 0
    for char in last_line[1:]:
        if char == " ":
            end += 1
        else:
            col_ranges.append((start, end))
            start = end + 1
            end += 1

    ops: list[str] = []
    for start, end in col_ranges:
        ops.append(last_line[start : start + 1])

    print(ops)
    print(input)
    print(col_ranges)

    return


if __name__ == "__main__":
    main()
