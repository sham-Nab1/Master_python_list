# continent_country_list.py

# List of countries and their corresponding continents.
continent_country_list = [
    ("USA", "North America"), ("Canada", "North America"), ("Brazil", "South America"),
    ("Argentina", "South America"), ("France", "Europe"), ("Germany", "Europe"),
    ("China", "Asia"), ("Japan", "Asia"), ("India", "Asia"),
    ("South Africa", "Africa"), ("Egypt", "Africa"), ("Australia", "Australia"),
    ("New Zealand", "Australia"), ("Russia", "Europe"), ("Mexico", "North America")
]

# Print the entire list.
print("Countries and their Continents:")
for country, continent in continent_country_list:
    print(f"{country}: {continent}")

# Access and print the 9th index.
print("\n9th index is:", continent_country_list[8])

# Update the 10th index to "Australia".
continent_country_list[9] = ("Australia", "Australia")
print()
print("Updated list after changing 10th index to 'Australia':")
for country, continent in continent_country_list:
    print(f"{country}: {continent}")

# Delete the 12th index.
del continent_country_list[11]
print()
print("Updated list after deleting the 12th index:")
for country, continent in continent_country_list:
    print(f"{country}: {continent}")

# Slice the list from index 4 to 8.
sliced_list = continent_country_list[4:9]
print()
print("Sliced portion from index 4 to 8:")
for country, continent in sliced_list:
    print(f"{country}: {continent}")

# Print the last index.
print()
print("Last index is:", continent_country_list[-1])