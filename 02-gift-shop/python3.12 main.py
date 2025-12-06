def main():
    input: str = ""
    with open("input.txt", "r") as file:
        input = file.read()

    ranges = input.split(",")

    print(ranges)


if __name__ == "__main__":
    main()
