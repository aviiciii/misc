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

    results = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affectionate',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }

    print(res, ':', results[res])
    

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
    if p1.isalpha() and p2.isalpha():
        return [p1.lower(), p2.lower()]
    

if __name__ == "__main__":
    main()