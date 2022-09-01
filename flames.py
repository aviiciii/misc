

def main():
    person1, person2 = get_names()
    for letter in person1:
        if letter in person2:
            person2 = person2.replace(letter, '', 1)
            person1 = person1.replace(letter, '', 1)
    
    count = len(person1) + len(person2)
    print(flames(count))


def flames(count):
    l = ['F', 'L', 'A', 'M', 'E', 'S']
    while len(l) != 1:
        print(*l)
        canceller =  count % len(l)
        l.pop(canceller)
    print(*l)
    return l[0]

def get_names():
    p1 = input('P1 Name: ')
    p2 = input('P2 Name: ')
    if p1.isalpha() and p2.isalpha():
        return [p1.lower().strip(), p2.lower().strip()]

if __name__ == "__main__":
    main()