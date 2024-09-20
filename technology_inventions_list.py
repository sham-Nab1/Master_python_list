# technology_list.py

# List of 15 modern technology inventions.
tech_inventions = [
    "VR Headset", "Smart Home", "Cloud Computing", "Wearable Tech",
    "Biometric Sensors", "Augmented Reality", "Quantum Computing",
    "Internet", "Robotics", "Laptop", "AI", "Blockchain", 
    "3D Printer", "Electric Car", "Drone", "Smartwatch"    
]

# Print the entire list.
print("Technology Inventions:")
print(tech_inventions)

# Access and print the 11th index.
print()
print("11th index is:", tech_inventions[10])

# Update the 8th index to "Smartphone".
tech_inventions[7] = "Smartphone"
print("\nUpdated list after changing 8th index to 'Smartphone':")
print(tech_inventions)

# Delete the 14th index.
del tech_inventions[13]
print()
print("Updated list after deleting the 14th index:")
print(tech_inventions)

# Slice the list from index 5 to 10.
sliced_list = tech_inventions[5:11]
print()
print("Sliced portion from 5 to 10:")
print(sliced_list)

# Print the last index.
print()
print("Last index is:", tech_inventions[-1])