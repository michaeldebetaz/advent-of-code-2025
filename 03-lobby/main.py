def find_largest_joltage(bank, joltage_length) -> int:
    digits = ""
    start_idx = 0
    for i in range(joltage_length):
        max_ = 0
        for j in range(start_idx, len(bank) - joltage_length + i + 1):
            digit = bank[j]
            number = int(digit)
            if number > max_:
                max_ = number
                start_idx = j + 1
        digits += str(max_)

    return int(digits)


def main():
    input = ""
    with open("input.txt", "r") as f:
        input = f.read().strip()

    lines = input.split("\n")

    joltages_1: list[int] = []

    for line in lines:
        joltage = find_largest_joltage(line, 2)
        joltages_1.append(joltage)

    print("Result 1: ", sum(joltages_1))

    joltages_2: list[int] = []

    for line in lines:
        joltage = find_largest_joltage(line, 12)
        joltages_2.append(joltage)

    print("Result 2: ", sum(joltages_2))


if __name__ == "__main__":
    main()
