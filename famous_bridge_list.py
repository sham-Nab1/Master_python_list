# famous_bridge_list.py

# List of 8 famous bridges.
famous_bridges = [    
    "Sydney Harbour Bridge", "Pont du Gard", "London Bridge", "Akashi Kaikyō Bridge",
    "Brooklyn Bridge", "Tower Bridge", "Charles Bridge", "Forth Bridge"  
]

# Print the entire list.
print("Famous Bridges:")
print(famous_bridges)

# Access and print the 3rd index.
print()
print("3rd index is:", famous_bridges[2])

# Update the 6th index to "Golden Gate Bridge".
famous_bridges[5] = "Golden Gate Bridge"
print()
print("Updated list after changing 6th index to 'Golden Gate Bridge':")
print(famous_bridges)

# Delete the 7th index.
del famous_bridges[6]
print()
print("Updated list after deleting the 7th index:")
print(famous_bridges)

# Print the last index.
print()
print("Last index is:", famous_bridges[-1])