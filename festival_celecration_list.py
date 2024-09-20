# festival_celecration_list.py

# list of 10 festival celebrations.
festival_celebrations = [
    "TAti-Atihan", "Hanukkah", "Valentine's Day", "Lunar New Year", "Oktoberfest",
    "New Year", "Christmas", "Diwali", "Eid", "Halloween"    
]

# Print the entire list.
print("Festival Celebrations:")
print(festival_celebrations)

# Access and print the 5th index.
print()
print("5th index is:", festival_celebrations[4])

# Update the 3rd index to "Thanksgiving".
festival_celebrations[2] = "Thanksgiving"
print()
print("Updated list after changing 3rd index to 'Thanksgiving':")
print(festival_celebrations)

# Delete the 7th index.
del festival_celebrations[6]
print()
print("Updated list after deleting the 7th index:")
print(festival_celebrations)

# Print the last index.
print()
print("Last index is:", festival_celebrations[-1])