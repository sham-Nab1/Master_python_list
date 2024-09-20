# planet_list.py

# A list of 8 planet names.
planet_list = [
    "Mercury", "Venus", "Earth", "Mars", 
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

# Print the entire list.
print("Original List is: ")
print(planet_list)

# Access and print the 3rd index.
print()
print("3rd index is :" , planet_list[2])

# Update the 7th index to "Pluto".
planet_list[6] = "Pluto"
print()
print("Updated list after changing the 7th index to 'Pluto': ")
print(planet_list)

# Delete the 4th index.
del planet_list[3]
print()
print("Updated list after deleting the 4th index :")
print(planet_list)

# Print the last index.
print()
print("The last index is: ", planet_list[-1])