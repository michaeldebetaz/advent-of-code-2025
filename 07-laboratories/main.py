def main():
    input = ""
    with open("test.txt", "r") as f:
        input = f.read()

    lines = [list(line) for line in input.splitlines()]

    split_count = 0
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if row == 0:
                continue
            prev_char = lines[row - 1][col]

            if char == "." or char.isdigit():
                if prev_char != ".":
                    if prev_char == "S":
                        lines[row][col] = "1"
                    else:
                        if prev_char.isdigit():
                            a = int(prev_char)
                            n = int(char) if char.isdigit() else 0
                            lines[row][col] = str(a + n)
            elif char == "^":
                if prev_char == "S" or prev_char.isdigit():
                    left = lines[row][col - 1]
                    left = int(left) if left.isdigit() else 0
                    lines[row][col - 1] = str(int(prev_char) + left)

                    right = lines[row][col + 1]
                    right = int(right) if right.isdigit() else 0
                    lines[row][col + 1] = str(int(prev_char) + right)

                    split_count += 1

    for line in lines:
        print("".join(line))

    print(f"Result 1: {split_count}")

    total = 0
    for s in lines[-1]:
        if s.isdigit():
            total += int(s)

    print(f"Result 2: {total}")

    return


if __name__ == "__main__":
    main()
