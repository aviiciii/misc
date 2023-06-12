def find_duplicates(lst):
    duplicates = []
    seen = set()

    for item in lst:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)

    return duplicates

# add contents to my_list
my_list = []

result = find_duplicates(my_list)
print("Duplicates in the list:", result)
