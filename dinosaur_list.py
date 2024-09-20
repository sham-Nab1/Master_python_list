# dinosaur_list.py

# List of 8 dinosaur names.
dinosaur_names = [
    "Velociraptor", "Brachiosaurus", "Triceratops", "Spinosaurus", 
    "Stegosaurus", "Diplodocus", "Spinosaurus", "Diplodocus"
]

# Print the entire list.
print("Dinosaur Names:")
print(dinosaur_names)

# Access and print the 4th index.
print()
print("4th index is:", dinosaur_names[3])

# Update the 6th index to "Tyrannosaurus Rex".
dinosaur_names[5] = "Tyrannosaurus Rex"
print()
print("Updated list after changing 6th index to 'Tyrannosaurus Rex':")
print(dinosaur_names)

# Delete the 7th index.
del dinosaur_names[6]
print()
print("Updated list after deleting the 7th index:")
print(dinosaur_names)

# Print the last index.
print()
print("Last index is:", dinosaur_names[-1])