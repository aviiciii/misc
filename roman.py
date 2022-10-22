roman={'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}

def romanToInt(s: str) -> int:
    # string to list
    romans = [letter for letter in s]
    
    # initializations
    ans= 0
    skip = False
    
    # convert to roman
    for letter in romans:
        # check input
        if letter not in roman.keys():
            return 'Invalid Input.'
            
        # check for skipping the letter
        if skip == True:
            skip = False
            continue

        # get value of letter
        value= roman[letter]


        # check for I, X, C for subtractions
        if letter in ('I', 'X', 'C'):
            # get next letter
            index = romans.index(letter)
            try:
                next_letter = romans[index+1]
            except:
                next_letter=False

            # overwrite current value with total value of current and next letter
            if next_letter:
                match letter:
                    case 'I':
                        if next_letter in ('V','X'):
                            value=roman[next_letter] - 1
                            skip = True
                    case 'X':
                        if next_letter in ('L','C'):
                            value=roman[next_letter] - 10
                            skip = True
                    case 'C':
                        if next_letter in ('D','M'):
                            value=roman[next_letter] - 100
                            skip = True
                    case False:
                        return 'error'
        # add current value to ans
        ans+=value

    return ans

# get input
inpt = input('Enter Roman Value: ').strip().upper()

# print output
print(romanToInt(inpt))