# river_list.py

# List of 10 famous rivers.
famous_rivers = [
    "Yenisei River", "Yellow River", "Mississippi River" , "Ganges River", "Zambezi River",
    "Amazon River", "Euphrates River", "Yangtze River", "Ob River", "Danube River"   
]

# Print the entire list.
print("Famous Rivers:")
print(famous_rivers)

# Access and print the 6th index.
print()
print("6th index is:", famous_rivers[5])

# Update the 8th index to "Nile River".
famous_rivers[7] = "Nile River"
print()
print("Updated list after changing 8th index to 'Nile River':")
print(famous_rivers)

# Delete the 9th index.
del famous_rivers[8]
print()
print("Updated list after deleting the 9th index:")
print(famous_rivers)

# Print the last index.
print()
print("Last index is:", famous_rivers[-1])