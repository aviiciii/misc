

def main():
    person1, person2 = get_names()
    print(person1, person2)


def get_names():
    p1 = input('P1 Name: ')
    p2 = input('P2 Name: ')
    return [p1, p2]

if __name__ == "__main__":
    main()