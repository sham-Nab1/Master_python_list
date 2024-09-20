# school_subject_list.py

# List of 12 school subjects.
school_subjects = [
    "Purposive Communication", "Science", "Computer Science", "Literature", "English",
    "Art", "Physical Education", "Biology", "Chemistry", "Music", 
    "History", "Geography",
]

# Print the entire list.
print("School Subjects:")
print(school_subjects)

# Access and print the 6th index.
print()
print("6th index is:", school_subjects[6])

# Update the 8th index to "Mathematics".
school_subjects[7] = "Mathematics"
print()
print("Updated list after changing 8th index to 'Mathematics':")
print(school_subjects)

# Delete the 4th index.
del school_subjects[3]
print()
print("Updated list after deleting the 4th index:")
print(school_subjects)

# Slice the list from index 2 to 5.
sliced_list = school_subjects[2:6]
print()
print("Sliced portion from index 2 to 5:")
print(sliced_list)

# Print the last index of the list.
print()
print("Last index is:", school_subjects[-1])