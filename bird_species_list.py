# bird_species_list.py

# List of 12 bird species.
bird_species = [
    "Sparrow", "Robin", "Pigeon", "Swan", "Hummingbird", 
    "Canary", "Flamingo", "Falcon", "Parrot", "Peacock",
    "Owl", "Penguin",
]

# Print the entire list.
print("Bird Species:")
print(bird_species)

# Access and print the 9th index.
print()
print("9th index is:", bird_species[8])

# Update the 6th index to "Eagle".
bird_species[5] = "Eagle"
print()
print("Updated list after changing 6th index to 'Eagle':")
print(bird_species)

# Delete the 8th index.
del bird_species[7]
print()
print("Updated list after deleting the 8th index:")
print(bird_species)

# Slice the list from index 3 to 7.
sliced_list = bird_species[3:8]
print()
print("Sliced portion from index 3 to 7:")
print(sliced_list)

# Print the last index.
print()
print("Last index is:", bird_species[-1])