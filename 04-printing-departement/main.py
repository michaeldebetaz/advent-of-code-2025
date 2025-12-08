ROLL = "@"


def is_roll(lines: list[list[str]], position: tuple[int, int]) -> bool:
    row, col = position

    if row < 0 or row > len(lines) - 1 or col < 0 or col > len(lines[0]) - 1:
        return False

    return lines[row][col] == ROLL


def count_adjacent_rolls(lines: list[list[str]], row: int, col: int) -> int:
    prev_row = row - 1
    prev_col = col - 1
    next_row = row + 1
    next_col = col + 1
    positions = [
        (prev_row, prev_col),
        (prev_row, col),
        (prev_row, next_col),
        (row, prev_col),
        (row, next_col),
        (next_row, prev_col),
        (next_row, col),
        (next_row, next_col),
    ]

    count = 0
    for position in positions:
        if is_roll(lines, position):
            count += 1

    return count


def positions_to_remove(lines: list[list[str]]) -> list[tuple[int, int]]:
    positions: list[tuple[int, int]] = []
    for row in range(len(lines)):
        line = lines[row]
        for col in range(len(line)):
            spot = line[col]
            if spot == ROLL:
                count = count_adjacent_rolls(lines, row, col)
                if count < 4:
                    positions.append((row, col))

    return positions


def main():
    input = ""
    with open("input.txt", "r") as file:
        input = file.read().strip()

    lines: list[list[str]] = []
    for line in input.splitlines():
        lines.append([char for char in line])

    to_remove_1 = positions_to_remove(lines)
    count_1 = len(to_remove_1)
    print("Result 1: ", count_1)

    to_remove: list[tuple[int, int]] = []
    positions: list[tuple[int, int]] = []
    first_iteration = True
    while first_iteration or len(positions) > 0:
        first_iteration = False
        positions = positions_to_remove(lines)
        for position in positions:
            to_remove.append(position)
            row, col = position
            lines[row][col] = "."

    count_2 = len(to_remove)
    print("Result 2: ", count_2)

    return


if __name__ == "__main__":
    main()
