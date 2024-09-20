# drink_list.py

# List of 8 popular drinks.
drinks = [
    "Water", "Tea", "Milkshake", "Soda", 
    "Coffee", "Smoothie","Juice",  "Beer"
]

# Print the entire list.
print("Popular Drinks:")
print(drinks)

# Access and print the 4th index.
print()
print("4th index is:", drinks[3])

# Update the 3rd index to "Coffee".
drinks[2] = "Coffee"
print()
print("Updated list after changing 3rd index to 'Coffee':")
print(drinks)

# Delete the 7th index.
del drinks[6]
print()
print("Updated list after deleting the 7th index:")
print(drinks)

# Print the last index.
print()
print("Last index is:", drinks[-1])