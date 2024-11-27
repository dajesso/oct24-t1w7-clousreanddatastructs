# List - ordered (indexed) collection of items - mutable - can have duplicates

# Set - Unordered - Not Indexed - mutable - no duplicates

names_set = {'John', 'Felicis', 'Jesso', 'Amy'}
print(names_set)
names_set.add("Obama")
print(names_set)

names_set.remove("Amy")
print(names_set)

names_set.add('Jane')
print(names_set)

print('Amy' in names_set)

lists = ['felicis', 'jesso', 'amy', 'obama']
lists.append("evil felicis")
lists.remove("obama")

for x in range(0, len(lists)):
    print(lists[x])

set1 = {1, 2, 3, 4, 5}
set2 = {1,3,5,7,9}

print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))