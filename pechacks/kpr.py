from tqdm import tqdm

id ='20ee040@kpriet.ac.in'


yrs = [20,21,22]
last_roll = 300
depts = ['cs', 'ec', 'it', 'cb', 'ei', 'mb', 'ee', 'ic', 'me', 'pr', 'ai', 'ce', 'co']

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

            emails.append(str(yr) + dept + roll + '@kpriet.ac.in')

with open('kpr_it_spam.txt', 'w') as file:
    for email in emails:
        file.write(email + '\n')
    print(f'{len(emails)} Emails generated for {yrs} of {len(depts)} depts!')