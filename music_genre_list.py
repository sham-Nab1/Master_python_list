# music_genre_list.py

# List of 15 music genres.
music_genres = [
     "Reggae", "Blues", "Electronic", "Metal","Pop",
     "Rock", "Hip Hop", "Classical", "Country","Punk",
     "Latin", "Gospel", "Folk", "Soul", "R&B"
]

# Print the entire list.
print("Music Genres:")
print(music_genres)

# Access and print the 10th index.
print()
print("10th index is:", music_genres[9])

# Update the 5th index to "Jazz".
music_genres[4] = "Jazz"
print()
print("Updated list after changing 5th index to 'Jazz':")
print(music_genres)

# Delete the 7th index.
del music_genres[6]
print()
print("Updated list after deleting the 7th index:")
print(music_genres)

# Slice the list from index 3 to 8.
sliced_list = music_genres[3:9]
print()
print("Sliced portion from index 3 to 8:")
print(sliced_list)

# Print the last index of the list.
print()
print("Last index is:", music_genres[-1])