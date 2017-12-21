for i in range(5):
    print(i)
    print('Hello World')

# My first comment
a = 100
print(id(a)) # Prints the id of the variable

print(dir(a))

# get help on a method
print(help(print))

# get the type of the variable
print(type(a))

# List comprehension
sq = [i*i for i in range(10)]

# Nested List comprehension

sq = [(x, y) for x in range(5) for y in range(10) if x!=y ]
print(sq)

# data structures - list , sets, tuples, dictionaries
