# furniture_list.py

# List of 12 furniture items.
furniture_list= [        
    "Recliner", "Ottoman", "Wardrobe", "Desk", "Couch", "Dining Table",
    "Dresser", "Bookshelf", "Nightstand", "Chair", "Table", "Bed" 
]

# Print the entire list.
print("Furniture List:")
print(furniture_list)

# Access and print the 8th index.
print()
print("8th index is:", furniture_list[7])

# Update the 5th index to "Sofa".
furniture_list[4] = "Sofa"
print()
print("Updated list after changing 5th index to 'Sofa':")
print(furniture_list)

# Delete the 10th index.
del furniture_list[9]
print()
print("Updated list after deleting the 10th index:")
print(furniture_list)

# Print the last index of the list.
print()
print("Last index is:", furniture_list[-1])