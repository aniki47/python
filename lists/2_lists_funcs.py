lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar"]

print(friends)

# List functions

# .extend() - add another list to the calling list
friends.extend(lucky_numbers)
print(friends)

# .append() - add new item to the list
friends.append("Ram")
print(friends)

# .insert() - insert new item in the list at specified position
friends.insert(1, "Kelly")
print(friends)

# .remove() - remove specified element
friends.remove("Kelly")
print(friends)

# .pop() - remove the last element of the list
# .index() - search specified item on the calling list
# .count() - count the number of times specified element appears on the calling list
# .sort() - sort list in ascending order
# .reverse() - revers the items in the calling list
# .copy() - copies the calling list data to new list