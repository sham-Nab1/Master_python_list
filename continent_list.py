# continent_list.py

# List of 7 continents.
continent_list = [
    "Asia", "North America", "South America", "Antarctica",
    "Europe", "Australia",  "Africa" 
]

# Print the entire list.
print("Continents List:")
print(continent_list)

# Access and print the 4th index.
print()
print("4th index is:", continent_list[3])

# Update the 2nd index to "Africa".
continent_list[2] = "Africa"
print()
print("Updated list after changing 2nd index to 'Africa':")
print(continent_list)

# Delete the 6th index.
del continent_list[5]
print()
print("Updated list after deleting the 6th index:")
print(continent_list)

# Print the last index of the list.
print()
print("Last index is:", continent_list[-1])