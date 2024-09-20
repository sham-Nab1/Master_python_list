# animal_habitats_list.py

# List of 8 animal habitats.
animal_habitats = [    
    "Grassland","Wetlands", "Savannah", "Mountain", 
    "Forest", "Desert", "Ocean", "Tundra"
]

# Print the entire list.
print("Animal Habitats:")
print(animal_habitats)

# Access and print the 5th index.
print()
print("5th index is:", animal_habitats[4])

# Update the 3rd index to "Savannah".
animal_habitats[2] = "Savannah"
print()
print("Updated list after changing 3rd index to 'Savannah':")
print(animal_habitats)

# Delete the 6th index.
del animal_habitats[5]
print()
print("Updated list after deleting the 6th index:")
print(animal_habitats)

# Print the last index.
print()
print("Last index is:", animal_habitats[-1])