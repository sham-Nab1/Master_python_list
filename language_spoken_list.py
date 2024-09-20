# language_spoken_list.py

# A list of 20 languages spoken around the world.
language_spoken_list = [
    "Korean", "English", "Mandarine Chinese", "Filipino(Tagalog)", "Swahili",
    "Arabic", "Portuguese", "Russian", "Japanese", "Punjabi",
    "German", "French", "Italian", "Turkish", "Vietnamese",
    "Thai", "Persian(Farsi)", "Dutch", "Swedeish",  "Hindi"
]
# Print the entire list.
print("Original list is : ")
print(language_spoken_list)

# Access and print the 13th index.
print()
print("13th index is: ", language_spoken_list[12])
print(language_spoken_list)

# Update the 10th index to "Spanish".
language_spoken_list[9] = "Spanish"
print()
print("Updated list after changing the 10th index to 'Spanish': ")
print(language_spoken_list)

# Delete the 16th index.
del language_spoken_list [15]
print()
print("Updatedlist after deleting the 16th index : ")
print(language_spoken_list)

# Slice the list from index 6 to 11.
sliced_list = language_spoken_list[6:12]
print()
print("Sliced portion from 6 to 11 is: ")
print(sliced_list)

# Print the last index.
print()
print("The last index is : ", language_spoken_list[-1] )