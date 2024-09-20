# land_ animal_speed_list.py

# List of 12 land animals and their speeds.
land_animal_speeds = [
    "Elephant - 40 km/h", "Lion - 50 km/h", "Horse - 70 km/h",
    "Gazelle - 80 km/h", "Kangaroo - 70 km/h", "Tiger - 65 km/h",
    "Wolf - 60 km/h", "Zebra - 65 km/h", "Giraffe - 55 km/h",
    "Bison - 40 km/h", "Rhino - 50 km/h", "Buffalo - 50 km/h"
]

# Print the entire list.
print("Land Animals and Their Speeds:")
print(land_animal_speeds)

# Access and print the 7th index.
print()
print("7th index is:", land_animal_speeds[6])

# Update the 9th index to "Cheetah - 120 km/h".
land_animal_speeds[8] = "Cheetah - 120 km/h"
print()
print("Updated list after changing 9th index to 'Cheetah - 120 km/h':")
print(land_animal_speeds)

# Delete the 10th index.
del land_animal_speeds[9]
print()
print("Updated list after deleting the 10th index:")
print(land_animal_speeds)

# Slice the list from index 3 to 7.
sliced_list = land_animal_speeds[3:8]
print()
print("Sliced portion from index 3 to 7:")
print(sliced_list)

# Print the last index.
print()
print("Last index is:", land_animal_speeds[-1])