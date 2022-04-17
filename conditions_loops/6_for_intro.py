
# Print all characters in letter using for loop
for letter in "Giraffe Academy":
    print(letter)

# Print array using for loop
friends = ["Jim", "Karen", "Kevin"]
for name in friends:
    print("Length of the array: "+str(len(friends)))
    print(name)

# Print numbers in a rage using for loop
for index in range(3, 10):
    print(index)

# Play with the index value
for index in range(5):
    if(index==0):
        print("Conditional part of the loop")
    else:
        print("Normal part of the loop")
