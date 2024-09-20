# animal_species_list.py

# A list of 7 animal species.
animal_species_list = [
    "Koala", "Red Fox", "Giant Panda", "Blue Whale"
    "Bengal Tiger", "Cheetah", "Gray Wolf"
]

# Print the entire list.
("Original list is: ")
print(animal_species_list)

# Access and print the 2nd index.
print()
print("2nd index is: ", animal_species_list[1])

# Update the 5th index to "Gorilla".
animal_species_list[4] = "Gorilla"
print("Updated list after changing the 5th index to 'Gorilla': ")
print(animal_species_list)

# Delete the 6th index.
del animal_species_list[5]
print()
print("Updated list after deleting the 6th index: ")
print(animal_species_list)

# Print the last index.
print()
print("The last index is: ", animal_species_list[-1])