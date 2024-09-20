# tool_list.py

# list of 10 carpentry tools
carpentry_tools = [
    "Miter Saw", "Chisel", "Measuring Tape", "Square", "Pliers",
    "Plane", "Drill", "Screwdriver", "Clamps", "Router"
]

# Print the entire list
print("Carpentry Tools:")
print(carpentry_tools)

# Access and print the 4th index
print()
print("4th index is:", carpentry_tools[4])

# Update the 7th index to "Hammer"
carpentry_tools[6] = "Hammer"
print()
print("Updated list after changing 7th index to 'Hammer':")
print(carpentry_tools)

# Delete the 5th index
del carpentry_tools[5]
print()
print("Updated list after deleting the 5th index:")
print(carpentry_tools)

# Print the last index
print()
print("Last index is:", carpentry_tools[-1])