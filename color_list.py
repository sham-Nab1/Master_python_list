# color_list.py

# list 15 colors.
color_list = [
    "Pink", "Black", "Green", "Blue", "White",
    "Yellow", "Violet", "Gold", "Brown", "Red",
    "Khaki", "Gray", "Cyan", "silver", "Maroon"
]

# Print the entire list.
print("Color List: ")
print(color_list)

# Access and print the 10th index.
print()
print("10th index is :" , color_list[9])

# Update the 4th index to "Purple".
color_list[3] = "Purple"
print()
print("Updated list after changing the 4th index to 'Purple': ")
print(color_list)

# Delete the 5th index.
print()
del color_list[4]
print("Updated list after deleting th 5th index : ")
print (color_list)

# Slice the list from index 2 to 8.
sliced_list = color_list[2:9]
print()
print("Sliced portion from 2 to 8: ")
print (sliced_list)

# Print the last index.
print()
print("The lsat index is: ", color_list[-1])