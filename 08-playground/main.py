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
    with open("input.txt", "r") as f:
        input = f.read()

    lines = input.splitlines()
    positions: list[Position] = []
    for line in lines:
        x, y, z = line.split(",")
        positions.append((int(x), int(y), int(z)))

    distances: list[tuple[Position, Position, float]] = []
    seen: set[tuple[Position, Position]] = set()
    for pos_1 in positions:
        for pos_2 in positions:
            if pos_1 == pos_2:
                continue
            if (pos_1, pos_2) in seen or (pos_2, pos_1) in seen:
                continue
            seen.add((pos_1, pos_2))
            dist = euclidian_distance(pos_1, pos_2)
            distances.append((pos_1, pos_2, dist))

    distances.sort(key=lambda x: x[2])

    circuits: list[set[Position]] = []

    for d in distances[:1_000]:
        pos_1, pos_2, _ = d
        if len(circuits) == 0:
            circuits.append(set([pos_1, pos_2]))
            continue

        found = False
        for circuit in circuits:
            if pos_1 in circuit or pos_2 in circuit:
                found = True
                circuit.update(set((pos_1, pos_2)))
                break

        if not found:
            circuits.append(set([pos_1, pos_2]))

    current_idx = 0
    while current_idx < len(circuits):
        circuit = circuits[current_idx]
        for c in circuits:
            if circuit != c:
                intersect = len(circuit.intersection(c)) > 0
                if intersect:
                    circuit.update(c)
                    circuits.remove(c)
                    current_idx = -1
                    break
        current_idx += 1

    for pos in positions:
        for circuit in circuits:
            if pos in circuit:
                break
        else:
            circuits.append(set([pos]))

    circuits.sort(key=lambda circuit: len(circuit), reverse=True)

    # for c in circuits[:10]:
    #     print(len(c))
    #     print(c)

    total = 1
    for c in circuits[:3]:
        total *= len(c)

    print("Result 1:", total)

    return


if __name__ == "__main__":
    main()
