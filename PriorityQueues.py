from queue import PriorityQueue


def identify_nickname_count():
    try:
        return int(input("Enter how many classmate nicknames do you want to list: "))
    except ValueError:
        print("Invalid input!!! Please enter a number.")
        return identify_nickname_count()


def main():
    nickname_count = identify_nickname_count()
    prio = PriorityQueue()

    for names in range(nickname_count):
        nickname = input("")
        prio.put(nickname)

    while not prio.empty():
        nickname = prio.get()
        h_key = input("Press H to say Hi to each one of them: ")

        if h_key.upper() == 'H':
            print(f"Hi {nickname}")
        if h_key.upper() != 'H':
            print("Invalid input!!! Please input 'H'.")

    print("Done saying hi..")


if __name__ == "__main__":
    main()