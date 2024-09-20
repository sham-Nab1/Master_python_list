# sports_list.py

# List of 10 popular sports.
sports_list= [
    "Gymnastics", "Badminton", "Hockey", "Volleyball", "Swimming", 
    "Soccer", "Golf", "Baseball", "Tennis", "Cricket",
]

# Print the entire list.
print("Popular Sports:")
print(sports_list)

# Access and print the 6th index.
print()
print("6th index is:", sports_list[5])

# Update the 4th index to "Basketball".
sports_list[3] = "Basketball"
print()
print("Updated list after changing 4th index to 'Basketball':")
print(sports_list)

# Delete the 9th index.
del sports_list[8]
print()
print("Updated list after deleting the 9th index:")
print(sports_list)

# Print the last index of the list.
print()
print("Last index is:", sports_list[-1])