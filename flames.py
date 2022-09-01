results = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affectionate',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }

def main():

    # getting input names
    while True:
        try:
            p1, p2 = get_names()
            break
        except:
            print('Names not valid.')

    # getting result
    res = flames(p1, p2)

    
    # print result
    print('--- FLAMES ---')
    print(res, ':', results[res])
    

def flames(person1, person2):

    # removing common letters
    for letter in person1:
        if letter in person2:
            person2 = person2.replace(letter, '', 1)
            person1 = person1.replace(letter, '', 1)
    
    # getting count of unique letters
    count = len(person1) + len(person2)

    # iterating over FLAMES
    l = ['F', 'L', 'A', 'M', 'E', 'S']

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