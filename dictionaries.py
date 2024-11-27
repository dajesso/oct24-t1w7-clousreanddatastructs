# List - ordered (indexed) collection of items - mutable - can have duplicates

# Dictionary (dict) - mutable - collection of items - mutable - unordered - not indexed
# keyed - key/value pairs - keys cannot have duplicates

person1 = {
    "name": "Felicis",
    "last_name": "Amy",
    "age": 6000
}

print(person1.get('foo', 'Key not found'))
print(person1["name"])
print(type(person1))

person1['address'] = {
    'state' : 'SA',
    'postcode': 5112,
    'city': 'Adelaide'
}
print(person1['address']['postcode'])
print(person1)
person1.update({'name': 'Jesso', 'age': 27})
print(person1)

# Loop

for key, val in person1.items():
    print(f'Key: {key}')
    print(f'Value: {val}')