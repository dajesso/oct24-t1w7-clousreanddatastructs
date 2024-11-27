def multiply(multiplier):
    return lambda x : x * multiplier

doubler = multiply(2)
tripler = multiply(3)
print(doubler(50))
print(tripler(20))