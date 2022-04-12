# Keys need to be unique. Can include numbers & strings.
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    5: "May"
}

# Approach 1
print(monthConversions["Apr"])

# Approach 2
print(monthConversions.get("Lol", "No results found."))