

def main():
    while True:
        try:
            person1, person2 = get_names()
            break
        except:
            print('Names not valid.')

        
    for letter in person1:
        if letter in person2:
            person2 = person2.replace(letter, '', 1)
            person1 = person1.replace(letter, '', 1)
    
    count = len(person1) + len(person2)
    res = flames(count)
    print(res)
    

def flames(count):
    l = ['F', 'L', 'A', 'M', 'E', 'S']
    print('---',*l, '---')
    while len(l) != 1:
        canceller =  count % len(l)
        l.pop(canceller)
    return l[0]

def get_names():
    p1 = input('P1 Name: ').strip().replace(' ','')
    p2 = input('P2 Name: ').strip().replace(' ','')
    print(p1, p2)
    if p1.isalpha() and p2.isalpha():
        return [p1.lower(), p2.lower()]
    

if __name__ == "__main__":
    main()