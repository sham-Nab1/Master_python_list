# invention_list.py

# List of 8 famous inventions.
inventions = [
    "Telephone", "Radio", "Television", 
    "Airplane", "Computer", "Internet", 
    "Computer", "Printing Press"
]

# Print the entire list.
print("Famous Inventions List:")
print(inventions)

# Access and print the 6th index.
print()
print("6th index is:", inventions[5])

# Update the 2nd index to "Lightbulb".
inventions[2] = "Lightbulb"
print()
print("Updated list after changing 2nd index to 'Lightbulb':")
print(inventions)

# Delete the 5th index.
del inventions[4]
print()
print("Updated list after deleting the 5th index:")
print(inventions)

# Print the last index of the list.
print()
print("Last index is:", inventions[-1])