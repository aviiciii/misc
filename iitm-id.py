import re

inpt=input('ID:')
# inpt = '21F3000426'

# writting regex
if re.search(r'^(21|22)(F|DP|DS)([1-3]{1})([0-9]{6})$', inpt):
    print('Valid ID')
else:
    print('Invalid ID')