# Basic translator for the Giraffe Language
# vowels -> g (Any vowel is going to get converted to "g")
# ex: dog > dgg or cat > cgt
# Vowels: a, e, i, o, u
# ----------------

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation+"G"
            else:
                translation = translation+"g"
        else:
            translation = translation+letter

    return translation

# Simple conversion
# print(translate("dog"))

# Get user input and translate
print(translate(input("Enter a phrase to translate: ")))