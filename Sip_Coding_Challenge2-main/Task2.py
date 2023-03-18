list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']
common_animal = []
uncommon_animal= []

for i in list_a:
    if i in list_b:
        common_animal.append(i)
for i in list_a:
    if i not in list_b:
        uncommon_animal.append(i)
for i in list_b:
    if i not in list_a:
        uncommon_animal.append(i)

for i in range(0, len(common_animal)):
    print("both list_a and list_b have ", common_animal[i], " in common")

for i in range(0, len(uncommon_animal)):
    print("both list_a and list_b do not have ", uncommon_animal[i], " in common")

