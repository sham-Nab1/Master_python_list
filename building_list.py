# building_list.py

# List of 8 famous buildings.
famous_buildings = [
    "Great Wall of China", "St. Basil's Cathedral", "Eiffel Tower", "Sydney Opera House",
    "Burj Khalifa", "Colosseum", "Statue of Liberty", "Sagrada Familia"
]

# Print the entire list.
print("Famous Buildings:")
print(famous_buildings)

# Access and print the 5th index.
print()
print("5th index is:", famous_buildings[4])

# Update the 2nd index to "Eiffel Tower".
famous_buildings[1] = "Eiffel Tower"
print()
print("Updated list after changing 2nd index to 'Eiffel Tower':")
print(famous_buildings)

# Delete the 6th index.
del famous_buildings[5]
print()
print("Updated list after deleting the 6th index:")
print(famous_buildings)

# Print the last index of the list.
print()
print("Last index is:", famous_buildings[-1])