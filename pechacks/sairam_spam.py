# id = 'sec19ec025@sairamtap.edu.in'
from tqdm import tqdm

yrs=[20, 21, 22]
last_roll=300
depts=['cs', 'ec', 'it', 'cb', 'ei', 'mb', 'ee', 'ic', 'me', 'pr', 'ai', 'ce']

emails = []
for dept in tqdm(depts):
    for yr in yrs:
        for i in range(1, last_roll):
            if i < 10:
                roll = '00' + str(i)
            elif i < 100:
                roll = '0' + str(i)
            else:
                roll = str(i)

            emails.append('sit' + str(yr) + dept + roll + '@sairamtap.edu.in')

with open('sairam_it_spam.txt', 'w') as file:
    for email in emails:
        file.write(email + '\n')
    print(f'{len(emails)} Emails generated for {yrs} of {len(depts)} depts!')

