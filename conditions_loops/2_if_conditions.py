is_male = True
is_tall = False

# Conditional "if" statement
# Example 1 OR
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

print("---x----x----")

# Example 2 AND
if is_male and is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

print("---x----x----")

# Example 3 ELSEIF = ELIF
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are neither male nor tall")