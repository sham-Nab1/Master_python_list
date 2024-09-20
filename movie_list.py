# movie_list.py

# A list of 20 movie titles.
movie_list = [
    "Train to busan", "Pandora", "Parasite", "Wonderland", "20th Century Girl",
    "Lolo and the kid", "Will you Marry", "The Hows of Us", "Un/Happy for you", "Road Trip",
    "Rewind", "Hello, Love, Goodbye", "One More Chance", "Alone Together", "Unforgettable",
    "Miss Granny", "The Gifted", "An Inconvinient Love", "Diary ng Panget", "Seven Sundays"
]

# Print the entire list.
print ("Movie List: ")
print(movie_list)

# Access and print the 12th index.
print()
print("12th index is: ", movie_list[11])

# Update the 15th index to "Inception".
movie_list[14] = "Inception"
print()
print("Updated list after changing the 15th index to 'Inception' : ")
print(movie_list)

# Delete the 18th index.
del movie_list[17]
print()
print("Updated list after deleting the 18th index: ")
print(movie_list)

# Slice the list from index 8 to 13.
sliced_list = movie_list[8:14]
print()
print("Sliced portion from from 8 to 13: ")
print(sliced_list)

# Print the last index.
print()
print("The last index is: ", movie_list[-1])