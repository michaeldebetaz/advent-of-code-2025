def main():
    input: str = ""
    with open("elsainput.txt", "r") as file:
        input = file.read().strip()

    ranges_str = input.split(",")

    ranges: list[tuple[int, int]] = []

    for r in ranges_str:
        start_str, end_str = r.split("-")
        ranges.append((int(start_str), int(end_str)))

    invalid_ranges_1: list[int] = []

    for start, end in ranges:
        for n in range(start, end + 1):
            s = str(n)
            length = len(s)
            if length % 2 != 0:
                continue
            else:
                split = length // 2
                first, last = s[:split], s[split:]
                if first == last:
                    invalid_ranges_1.append(n)

    result_1 = sum(invalid_ranges_1)
    print("Result 1:", result_1)

    invalid_ranges_2: set[int] = set()

    for start, end in ranges:
        for n in range(start, end + 1):
            s = str(n)
            length = len(s)
            for split in range(2, length + 1):
                if length % split != 0:
                    continue
                else:
                    part_len = length // split
                    patterns: set[str] = set()
                    for idx in range(0, length, part_len):
                        part = s[idx : idx + part_len]
                        patterns.add(part)

                    if len(patterns) == 1:
                        invalid_ranges_2.add(n)

    result_2 = sum(invalid_ranges_2)
    print("Result 2:", result_2)


if __name__ == "__main__":
    main()
