# dessert_list.py

# List of 10 desserts.
desserts_list = [
    "Apple PieIce Cream", "Tiramisu", "Cheesecake", "Brownies", "Pavlova",
    "Cupcakes", "Panna Cotta", "Chocolate Mousse", "Macarons", "Fruit Tart"  
]

# Print the entire list.
print("Desserts List:")
print(desserts_list)

# Access and print the 4th index.
print()
print("4th index is:", desserts_list[3])

# Update the 6th index to "Chocolate Cake".
desserts_list[5] = "Chocolate Cake"
print()
print("Updated list after changing 6th index to 'Chocolate Cake':")
print(desserts_list)

# Delete the 3rd index.
del desserts_list[2]
print()
print("Updated list after deleting the 3rd index:")
print(desserts_list)

# Print the last index of the list.
print()
print("Last index is:", desserts_list[-1])