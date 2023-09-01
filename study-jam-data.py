# import two csv files


import csv
import os
import sys
import re

# import csv files
file1 = sys.argv[1]
file2 = sys.argv[2]

selected=[]
filled=[]

# open csv files
with open(file1, 'r') as f1:
    reader1 = csv.reader(f1)
    # get the first column
    
    for row in reader1:
        selected.append(row[0])
    

with open(file2, 'r') as f2:
    reader2 = csv.reader(f2)
    for row in reader2:
        filled.append(row[0])


not_filled=[]
# find numbers in selected that are not in filled
for i in selected:
    if i not in filled:
        not_filled.append(i)

print(len(not_filled))