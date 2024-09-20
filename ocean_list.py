# ocean_list.py

# List of 5 oceans.
oceans = [
    "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Southern Ocean", "Pacific Ocean"     
]

# Print the entire list.
print("Oceans:")
print(oceans)

# Access and print the 3rd index.
print()
print("3rd index is:", oceans[2])

# Update the 2nd index to "Pacific Ocean".
oceans[1] = "Pacific Ocean"
print()
print("Updated list after changing 2nd index to 'Pacific Ocean':")
print(oceans)

# Delete the 4th index.
del oceans[3]
print()
print("Updated list after deleting the 4th index:")
print(oceans)

# Print the last index.
print()
print("Last index is:", oceans[-1])