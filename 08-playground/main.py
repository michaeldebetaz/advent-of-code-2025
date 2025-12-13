import math

Position = tuple[int, int, int]


def euclidian_distance(pos_1: Position, pos_2: Position) -> float:
    x1, y1, z1 = pos_1
    x2, y2, z2 = pos_2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def find_closest_position(src: Position, positions: list[Position]) -> Position:
    min_dist = float("inf")
    closest_pos = None
    for pos in positions:
        dist = euclidian_distance(src, pos)
        if dist < min_dist:
            min_dist = dist
            closest_pos = pos

    if closest_pos is None:
        raise ValueError("No closest position found")

    return closest_pos


def main():
    input = ""
    with open("test.txt", "r") as f:
        input = f.read()

    lines = input.splitlines()
    positions: list[tuple[int, int, int]] = []
    for line in lines:
        x, y, z = line.split(",")
        positions.append((int(x), int(y), int(z)))

    pairs: list[tuple[Position, Position]] = []

    current_idx = 0
    other_positions = positions.copy()
    while True:
        pos_1 = positions[current_idx]
        other_positions.remove(pos_1)
        pos_2 = find_closest_position(pos_1, other_positions)
        pos_2_idx = positions.index(pos_2)
        pairs.append((pos_1, pos_2))
        current_idx = pos_2_idx
        if len(other_positions) == 1:
            break

    print(pairs)

    return


if __name__ == "__main__":
    main()
