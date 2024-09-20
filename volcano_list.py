# volcano_list.py

# List of 7 famous volcanoes.
famous_volcanoes = [
    "Mount St. Helens", "Mauna Loa","Mount Fuji", "Kilimanjaro",
    "Krakatoa", "Mount Etna", "Mount Pinatubo"
]

# Print the entire list.
print("Famous Volcanoes:")
print(famous_volcanoes)

# Access and print the 4th index.
print()
print("4th index is:", famous_volcanoes[3])

# Update the 3rd index to "Mount Vesuvius".
famous_volcanoes[2] = "Mount Vesuvius"
print()
print("Updated list after changing 3rd index to 'Mount Vesuvius':")
print(famous_volcanoes)

# Delete the 5th index.
del famous_volcanoes[4]
print()
print("Updated list after deleting the 5th index:")
print(famous_volcanoes)

# Print the last index.
print()
print("Last index is:", famous_volcanoes[-1])