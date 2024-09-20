# author_list.py

# A list of 12 famous authors.
author_list = [
    "William Shakespear", "Jane Austen", "Kurt Vonnegut", "Isaac Asimov", "Sylvia plath", "Stephen King",
    "Charles Dickens", "F. Scott Fitgerald", "Ernest Hemingway", "Harper Lee", "J.K. Rowling", "George Orwell" 
]

# Print the entire list.
print("Original list is : ")
print(author_list)

# Access and print the 6th index.
print()
print("6th index is: ", author_list[5])

# Update the 4th index to "Mark Twain".
author_list[3] = "Mark Twain"
print()
print("Updated list after changing the 4th index to 'Mark Twain': ")
print(author_list)

# Delete the 10th index.
del author_list[9]
print()
print("Updated list after deleting the 10th index: ")
print(author_list)

# Slice the list from index 3 to 8.
sliced_list=author_list[3:9]
print()
print("Sliced option from 3 to 8")
print(sliced_list)

# Print the last index.
print()
print("The last index is: ", author_list[-1])