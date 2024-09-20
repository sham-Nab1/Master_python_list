# game_list.py

# A list of 15 video game titles.
game_list = [
    "Among Us", "Cyberpunk 2077", "Dead Cells", "Super Mario Odyssey", "Animal Crossing: New Horizons",
    "Sackboy: A big Adventure", "Mario Kart 8 Deluxe", "Pokemon Sword and Shield", "Splaton 2", "Rayman Legends",
    "LittleBigPlanet 3", "Stardew Valley", "Disney Infinity", "Crash Team Racing Nitro-Fueled", "Spiritfarer"
]
# Print the entire list.
print("Original List is : ")
print (game_list)

# Access and print the 7th index.
print()
print("7th index is: ", game_list [6])

# Update the 4th index to "Minecraft".
game_list[4] = "Minecraft"
print()
print("Updated list after changing the 4th index to 'Minecraft' : ")
print(game_list)

# Delete the 9th index.
del game_list[8]
print()
print("Updated list after deleting the 9th index : ")
print (game_list)

# Slice the list from index 5 to 10.
sliced_list = game_list[5:11]
print()
print("Sliced portion from 5 to 10")
print(sliced_list)

# Print the last index.
print()
print("The last index is : ", game_list[-1])