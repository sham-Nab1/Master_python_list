# fruit_list.py

# list of 12 Fruits
fruit_list= [
    "Banana", "Apple", "Orange", "Lemon", "Kiwi", "Cherry",
    "Grape", "Watermelon", "Avocado", "Papaya", "Mangosteen"
]
# Print the entire list.
print("Original list is: ")
print(fruit_list)

# Access and print the 9th index.
print()
print("The 9th index is: ", fruit_list[8])

# Update the 2nd index to "Mango".
fruit_list[1] = "Mango"
print()
print("Updated list after changing the 2nd index to 'Mango': ")
print(fruit_list)

# Delete the 10th index.
del fruit_list[9]
print()
print ("Updated list after deleting the 10th index: ")
print (fruit_list)

# Slice the list from index 4 to 7.
sliced_list = fruit_list[4:8]
print("Sliced portion from 2 to 5: ")
print(sliced_list)

# Print the last index of the list.
print()
print("Last index is:", fruit_list[-1])