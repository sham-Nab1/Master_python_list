# historical_figures_list.py

# A List of 10 historical figures.
historical_figures = [
    "George Washington", "Abraham Lincoln", "Leonardo da Vinci", "Rosa Parks" , "Julius Caesar", 
    "Martin Luther King Jr.", "Cleopatra", "Marie Curie", "Albert Einstein", "Winston Churchill"
]    

# Print the entire list.
print("Historical Figures List:")
print(historical_figures)

# Access and print the 8th index.
print()
print("8th index is:", historical_figures[7])

# Update the 4th index to "Nelson Mandela".
historical_figures[3] = "Nelson Mandela"
print()
print("Updated list after changing 4th index to 'Nelson Mandela':")
print(historical_figures)

# Delete the 7th index.
del historical_figures[6]
print()
print("Updated list after deleting the 7th index:")
print(historical_figures)

# Print the last index of the list.
print()
print("Last index is:", historical_figures[-1])