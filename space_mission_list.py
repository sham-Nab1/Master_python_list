# space_mission_list.py

# List of 10 space missions.
space_missions = [
    "Apollo 1", "Apollo 8", "Gemini 4", "Voyager 1","Voyager 2"
    "Mars Rover Opportunity", "Hubble Space Telescope","Curiosity Rover", 
    "New Horizons", "James Webb Space Telescope"
]

# Print the entire list.
print("Space Missions:")
print(space_missions)

# Access and print the 7th index.
print()
print("7th index is:", space_missions[6])

# Update the 4th index to "Apollo 11".
space_missions[3] = "Apollo 11"
print()
print("Updated list after changing 4th index to 'Apollo 11':")
print(space_missions)

# Delete the 6th index.
del space_missions[5]
print()
print("Updated list after deleting the 6th index:")
print(space_missions)

# Print the last index.
print()
print("Last index is:", space_missions[-1])