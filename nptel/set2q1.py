rows, columns = list(map(int,input().split()))

for row in range(rows):
    for column in range(columns):
        print('+-', end='')
    print('+')
    
    for column in range(columns):
        print('|.', end ='')
    print('|')

for column in range(columns):
    print('+-', end='')
print('+', end ='')