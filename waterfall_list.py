# waterfall_list.py

# List of 10 famous waterfalls.
famous_waterfalls = [
    "Gullfoss", "Yosemite Falls", "Plitvice Waterfalls", "Angel Falls", "Iguazu Falls", 
    "Huangguoshu Falls", "Sutherland Falls", "K waterfalls", "Skogafoss", "Victoria Falls"   
]

# Print the entire list.
print("Famous Waterfalls:")
print(famous_waterfalls)

# Access and print the 8th index.
print()
print("8th index is:", famous_waterfalls[7])

# Update the 5th index to "Niagara Falls".
famous_waterfalls[4] = "Niagara Falls"
print()
print("Updated list after changing 5th index to 'Niagara Falls':")
print(famous_waterfalls)

# Delete the 9th index.
del famous_waterfalls[8]
print()
print("Updated list after deleting the 9th index:")
print(famous_waterfalls)

# Print the last index.
print()
print("Last index is:", famous_waterfalls[-1])