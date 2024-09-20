# natural_landmark_list.py

# List of 10 natural landmarks.
natural_landmarks = [
    "Mount Everest", "Great Barrier Reef", "Yosemite Falls","Grand Canyon","Niagara Falls",
    "Salar de Uyuni", "Aurora Borealis", "Machu Picchu", "Angel Falls", "Stonehenge"   
]

# Print the entire list.
print("Natural Landmarks:")
print(natural_landmarks)

# Access and print the 8th index.
print()
print("8th index is:", natural_landmarks[7])

# Update the 5th index to "Grand Canyon".
natural_landmarks[4] = "Grand Canyon"
print()
print("Updated list after changing 5th index to 'Grand Canyon':")
print(natural_landmarks)

# Delete the 9th index.
del natural_landmarks[8]
print()
print("Updated list after deleting the 9th index:")
print(natural_landmarks)

# Print the last index.
print()
print("Last index is:", natural_landmarks[-1])