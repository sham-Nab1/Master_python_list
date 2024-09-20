# university_list.py

# List of 10 universities in the Philippines.
university_list = [
    "University of the Philippines", "Ateneo de Manila University", 
    "De La Salle University", "University of Santo Tomas", 
    "Mapúa University", "Far Eastern University", 
    "University of San Carlos", "University of Mindanao", 
    "Adamson University", "Central Philippine University"
]

# Print the entire list.
print("Universities in the Philippines:")
print(university_list )

# Access and print the 6th index.
print()
print("6th index is:", university_list[5])

# Update the 4th index to "Harvard University".
university_list[3] = "Harvard University"
print()
print("Updated list after changing 4th index to 'Harvard University':")
print(university_list )

# Delete the 9th index.
del university_list [8]
print()
print("Updated list after deleting the 9th index:")
print(university_list )

# Print the last index.
print()
print("Last index is:", university_list [-1])