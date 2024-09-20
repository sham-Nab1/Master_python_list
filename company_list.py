# company_list.py

# Create a list of 10 company names.
company_list = [
    "Microsoft", "Amazon", "Google", "Tesla", "Nike",
    "Facebook", "Coca-Cola", "Samsung", "Toyota", "Walmart"
]
# Print the entire list.
print("Original list is: ")
print(company_list)

# Access and print the 7th index.
print()
print("7th index is : ", company_list[6])

# Update the 5th index to "Apple".
company_list[4] = "Apple"
print()
print("Updated list after changing the 5th index to 'Apple': ")
print(company_list)

# Delete the 8th index.
del company_list[7]
print()
print("Updated list after deleting the 8th index: ")
print(company_list)

 # Print the last index.
print()
print("The last index is: ", company_list[-1])