# vegetable_list.py

# list of 7 vegetables.
vegetable_list = [
    "Eggplant", "Broccoli", "Cauliflower", "Cabage",
    "Cucumber", "Pumpkin", "Beet"
]

# Print the entire list.
print("Vegetable_List : ")
print(vegetable_list)

# Access and print the 5th index.
print()
print("5th index is: ", vegetable_list[4])

# Update the 3rd index to "Spinach".
vegetable_list[2] = "Spinach"
print()
print("Updated list after changing the 3rd index to 'Spinach': ")
print(vegetable_list)

# Delete the 6th index.
del vegetable_list[5]
print()
print("Updated list after deleting the 6th index: ")
print (vegetable_list)

# Print the last index.
print()
print("The last index is: ", vegetable_list[-1])