# actor_list.py

# List of 10 famous actors.
actor_names = [
    "Cha Eun Woo", "Kim Soo-hyun", "Byeon Woo Seok", "Park Seo-joon", "Lee Min-ho" 
    "Hyun Bin", "Lee Jong-suk", "Song Kang", "Gong Yoo", "Park Hae-jin" 
]

# Print the entire list.
print("Actor Names:")
print(actor_names)

# Access and print the 7th index.
print()
print("7th index is:", actor_names[7])

# Update the 3rd index to "Leonardo DiCaprio".
actor_names[3] = "Leonardo DiCaprio"
print()
print("Updated list after changing 3rd index to 'Leonardo DiCaprio':")
print(actor_names)

# Delete the 8th index.
del actor_names[8]
print()
print("Updated list after deleting the 8th index:")
print(actor_names)

# Print the last index of the list.
print()
print("Last index is:", actor_names[-1])