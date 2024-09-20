# currency_list.py

# List of 10 world currencies.
currencies = [
    "US Dollar", "Australian Dollar" , "Euro", "Indian Rupee", "Brazilian Real",
    "Chinese Yuan", "Swiss Franc","Canadian Dollar", "British Pound", "Japanese Yen"    
]

# Print the entire list.
print("World Currencies:")
print(currencies)

# Access and print the 4th index.
print()
print("4th index is:", currencies[3])

# Update the 7th index to "Euro".
currencies[6] = "Euro"
print()
print("Updated list after changing 7th index to 'Euro':")
print(currencies)

# Delete the 9th index.
del currencies[8]
print()
print("Updated list after deleting the 9th index:")
print(currencies)

# Print the last index.
print()
print("Last index is:", currencies[-1])