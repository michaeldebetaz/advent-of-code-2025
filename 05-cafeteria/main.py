def is_in_ranges(id: int, ranges: list[tuple[int, int]]) -> bool:
    for start, end in ranges:
        if start <= id <= end:
            return True
    return False


def main():
    text: str = ""
    with open("input.txt", "r") as file:
        text = file.read()

    ranges_str, ids_str = text.split("\n\n")

    ranges: list[tuple[int, int]] = []

    for r in ranges_str.splitlines():
        start, end = r.split("-")
        ranges.append((int(start), int(end)))

    fresh_ids: list[int] = []
    for id_str in ids_str.splitlines():
        id = int(id_str)
        if is_in_ranges(id, ranges):
            fresh_ids.append(id)

    print(f"Result 1: {len(fresh_ids)}")

    fresh_id_count = 0
    ranges.sort()
    seen_ranges: list[tuple[int, int]] = []
    for r in ranges:
        start, end = r
        for seen_r in seen_ranges:
            seen_start, seen_end = seen_r
            if seen_start <= start <= seen_end:
                start = seen_end + 1
            if seen_start <= end <= seen_end:
                end = seen_start - 1
        count = end + 1 - start
        if count <= 0:
            continue
        seen_ranges.append((start, end))
        fresh_id_count += count

    print(f"Result 2: {fresh_id_count}")


if __name__ == "__main__":
    main()
