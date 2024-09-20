# recipe_list.py

# List of 15 recipes.
recipe_list = [
    "Adobo", "Sinigang", "Kare-Kare", "Lechon", "Halo-Halo",
    "Pancit", "Lumpiang Shanghai", "Bicol Express", "Mami", "Balut",
    "Bibingka", "Puto", "Tinola", "Chicken Inasal", "Menudo"
]

# Print the entire list.
print("Favorite Filipino Recipes:")
print(recipe_list)

# Access and print the 12th index.
print()
print("12th index is:", recipe_list[11])

# Update the 9th index to "Lasagna".
recipe_list[8] = "Lasagna"
print()
print("Updated list after changing 9th index to 'Lasagna':")
print(recipe_list)

# Delete the 11th index.
del recipe_list[10]
print()
print("Updated list after deleting the 11th index:")
print(recipe_list)

# Slice the list from index 5 to 10.
sliced_list = recipe_list[5:11]
print()
print("Sliced portion from index 5 to 10:")
print(sliced_list)

# Print the last index.
print()
print("Last index is:", recipe_list[-1])