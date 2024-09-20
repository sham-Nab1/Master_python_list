# mountain_list.py

# A list of 8 mountain names.
mountain_list = [
    "Mount Apo", "Mount Pulag", "Mount Kitanglad", "Mount Mayon",
    "Mount Arayat", "Mount Pinatubo", "Mount Makiling", "Mount Talinis"
]
# Print the entire list.
print("Original list is: ")
print(mountain_list)

# Access and print the 5th index.
print()
print("5th index is : ", mountain_list[4])

# Update the 3rd index to "Everest".
mountain_list[2] = "Everest"
print()
print("Updated list after changing the 3rd index to 'Everest': ")
print(mountain_list)

# Delete the 6th index.
del mountain_list[5]
print()
print("Updated list after deleting the 6th index: ")
print(mountain_list)

# Print the last index.
print()
print("The last index is: ", mountain_list[-1])