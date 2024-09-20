# holiday_list.py

# List of 12 holidays.
holiday_list = [
    "Valentine's Day", "Easter", "New Year's Day"
    "Thanksgiving", "Midsummer", "Independence Day", 
    "Halloween", "Hanukkah", "Diwali", "Ramadan", 
    "Labor Day", "Veterans Day"
]

# Print the entire list.
print("Holidays List:")
print(holiday_list)

# Access and print the 9th index.
print()
print("9th index is:", holiday_list[8])

# Update the 3rd index to "Christmas".
holiday_list[2] = "Christmas"
print()
print("Updated list after changing 3rd index to 'Christmas':")
print(holiday_list)

# Delete the 11th index.
del holiday_list[10]
print()
print("Updated list after deleting the 11th index:")
print(holiday_list)

# Slice the list from index 2 to 7.
sliced_holidays = holiday_list[2:8]
print()
print("Sliced portion from index 2 to 7:")
print(sliced_holidays)

# Print the last index of the list.
print()
print("Last index is:", holiday_list[-1])