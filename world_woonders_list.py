# world_woonders_list.py

# List of 7 wonders of the world.
wonders_of_the_world = [
    "Statue of Zeus at Olympia", "Temple of Artemis at Ephesus", "Mausoleum at Halicarnassus","Colossus of Rhodes",
    "Great Pyramid of Giza", "Hanging Gardens of Babylon",  "Lighthouse of Alexandria"   
]

# Print the entire list.
print("Wonders of the World List:")
print(wonders_of_the_world)

# Access and print the 4th index.
print()
print("4th index is:", wonders_of_the_world[3])

# Update the 2nd index to "Great Wall of China".
wonders_of_the_world[2] = "Great Wall of China"
print()
print("Updated list after changing 2nd index to 'Great Wall of China':")
print(wonders_of_the_world)

# Delete the 5th index.
del wonders_of_the_world[4]
print()
print("Updated list after deleting the 5th index:")
print(wonders_of_the_world)

# Print the last index.
print()
print("Last index is:", wonders_of_the_world[-1])