# festival_list.py

# List of 15 festivals around the world.
festival_list = [
    "Coachella", "Chinese New Year","Carnival", "Oktoberfest", "Holi",
    "Mardi Gras", "Thanksgiving", "Bastille Day", "Day of the Dead", "Gion Matsuri"
    "Burning Man", "Rio Carnival", "Edinburgh Festival""La Tomatina", "Songkran",   
]

# Print the entire list.
print("Festivals List:")
print(festival_list)

# Access and print the 7th index.
print()
print("7th index is:", festival_list[6])

# Update the 11th index to "Diwali".
festival_list[10] = "Diwali"
print()
print("Updated list after changing 11th index to 'Diwali':")
print(festival_list)

# Delete the 9th index.
del festival_list[8]
print()
print("Updated list after deleting the 9th index:")
print(festival_list)

# Slice the list from index 5 to 12.
sliced_festival_list = festival_list[5:12]
print()
print("Sliced portion from index 5 to 12:")
print(sliced_festival_list)

# Print the last index of the list.
print()
print("Last index is:", festival_list[-1])