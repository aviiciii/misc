# id = '2021cs0000@svce.ac.in'
from tqdm import tqdm

yrs=[2020, 2021, 2022]
last_roll=1000
depts=['it', 'ad', 'ce', 'ch', 'ec', 'me', 'ee', 'mr','bt', 'cs', 'ec', 'mn']

emails = []
for dept in tqdm(depts):
    for yr in yrs:
        for i in range(1, last_roll):
            
            if i < 10:
                roll = '000' + str(i)
            elif i < 100:
                roll = '00' + str(i)
            elif i < 1000:
                roll = '0' + str(i)
            else:
                roll = str(i)

            emails.append(str(yr) + dept + roll + '@svce.ac.in')

with open('sairam_it_spam.txt', 'w') as file:
    for email in emails:
        file.write(email + '\n')
    print(f'{len(emails)} Emails generated for {yrs} of {len(depts)} depts!')

