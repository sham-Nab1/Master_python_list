# pokemon_list.py

# Create a list of 15 Pokémon names.
pokemon_list = [
    "Lucario", "Gardevoi", "Greninja", "Dragonite", "Togepi",
    "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Mewtwo"
    "Scyther", "Lapras", "Zubat", "Machamp", "Onix", 
]
# Print the entire list.
print("Original list is: ")
print(pokemon_list)

# Access and print the 9th index.
print()
print("9th index is: ", pokemon_list[8])

# Update the 12th index to "Pikachu".
pokemon_list[11] = "Pikachu"
print("Updated list after chnaging the 12th index to 'Pikachu': ")
print(pokemon_list)

# Delete the 10th index.
del pokemon_list[9]
print()
print("Updated list after deleting the last index: ")
print(pokemon_list)

# Slice the list from index 4 to 7.
sliced_list = pokemon_list[4:8]
print("Sliced portion from index 4 to 7: ")
print(sliced_list)

# Print the last index.
print()
print("The last index is : ", pokemon_list[-1])