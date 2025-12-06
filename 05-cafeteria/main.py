def main():
    text: str = ""
    with open("test.txt", "r", encoding="utf-8") as file:
        text = file.read()

    print(text)


if __name__ == "__main__":
    main()
