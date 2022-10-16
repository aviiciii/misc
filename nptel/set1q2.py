inpt_1 = input().split()
inpt_2 = input().split()

no_of_jars = inpt_1[0]
villagers = inpt_1[1]

ladoos = inpt_2

ladoo_count = 0
for ladoo in ladoos:
    ladoo_count += int(ladoo)

remainder = ladoo_count % int(villagers)

print(remainder)