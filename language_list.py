# language_list.py

# A list of 14 programming languages.
language_list = [
    "C++", "Java", "JavaScript", "C#", "Ruby", 
    "Perl", "PHP", "Swift", "Go", "Rust", 
    "Kotlin", "Scala", "TypeScript", "f#"    
]
# Print the entire list.
print("Language List : ")
print(language_list)

# Access and print the 11th index.
print()
print("11th index is: ", language_list[10])

# Update the 9th index to "Python".
language_list[8] = "Python"
print()
print("Updated list after changing 9th index to 'Python': ")
print(language_list)

# Delete the 13th index.
del language_list[12]
print()
print("Updated list after deleting the 13th index: ")
print(language_list)

# Slice the list from index 5 to 12.
sliced_list = language_list[5:13]
print()
print("Sliced portion of index 5 to 12: ")
print (sliced_list)

# Print the last index.
print()
print("The last index is: ", language_list[-1])

