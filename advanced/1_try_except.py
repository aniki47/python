# The program breaks whenever a user enters a string instead of a n integer
# number = int(input("Enter a number: "))
# print(number)

# Introduce try/execpt block to handle erronous situations
# This can be used to protect the program from irregularities
try:
    # Below statement will induce ZeroDivisionError exception
    # value = 10/0
    number = int(input("Enter a number: "))
    print(number)
# Using only "except" without specifying the type is too broad.
# So its a best practice to handle the exceptions for specific cases a below.
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Exception: Invalid input")
except:
    print("Exception: Unknown error")