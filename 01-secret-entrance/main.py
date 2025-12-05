def main():
    text: str = ""
    with open("input.txt", "r") as file:
        text = file.read()

    movements: list[str] = text.split("\n")

    current = 50
    count_land = 0
    count_pass = 0
    for movement in movements:
        if movement == "":
            continue

        # ex. movements[0] = "L68"
        direction = movement[0]

        value_str = movement[1:]
        value = int(value_str)

        full_cycles = value // 100
        count_pass += full_cycles

        reminder = value % 100

        result = 0
        if direction == "R":
            if current == 0 or current + reminder > 100:
                count_pass += 1
            result = (current + value) % 100
        elif direction == "L":
            if current - reminder < 0:
                count_pass += 1
            result = (current - value) % 100

        if result == 0:
            count_land += 1

        print(f"{movement} -> {current} -> {result} -> {count_pass}")

        current = result

    print(f"Count 1: {count_land}")
    print(f"Count 2: {count_pass}")

    return


if __name__ == "__main__":
    main()
