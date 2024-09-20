# flower_list.py

# A list of 10 flower names.
flower_list = [
    "Tulip", "Sunflower", "Daisy", "lily",  "Chrysanthemum"
    "Marigold", "Orchid", "Carnation", "Dahlia", "Lilac"
]

# Print the entire list.
print("Original list is")
print(flower_list)

# Access and print the 5th index.
print()
print("5th index is: ", flower_list[4])

# Update the 8th index to "Rose".
flower_list[7] = "Rose"
print()
print("Updated list after changing 8th index to 'Rose': ")
print(flower_list)

# Delete the 2nd index.
del flower_list[1]
print()
print("Updated list after deleting the 2nd index: ")
print(flower_list)

# Print the last index.
print()
print("The last index is: ", flower_list[-1])