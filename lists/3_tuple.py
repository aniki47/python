# tuple is immutable i.e you cannot alter it once you create it
coordinates = (4, 5)
print(coordinates[0])

# try changing a tuple
# We get error > TypeError: 'tuple' object does not support item assignment
# coordinates[1] = 10

# list vs. tuple
# square brackets - paranthesis
# edit OK - edit not OK

# Tuple is used in case where data is never going to be changed. Like coordinates.

# tuples inside a list example
tuple_list = [(4, 5), (6, 7), (80, 34)]