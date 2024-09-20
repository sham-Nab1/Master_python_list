# job_title_list.py

# List of 10 job titles in computer.
job_titles = [
    "Software Developer", "Data Scientist", "Web Developer", "System Administrator", 
    "Network Engineer", "Database Administrator", "DevOps Engineer", 
    "Cybersecurity Analyst", "UX/UI Designer", "IT Support Specialist"
]

# Print the entire list.
print("Job Titles in Computer:")
print(job_titles)

# Access and print the 6th index.
print()
print("6th index is:", job_titles[5])

# Update the 5th index to "Software Engineer".
job_titles[4] = "Software Engineer"
print()
print("Updated list after changing 5th index to 'Software Engineer':")
print(job_titles)

# Delete the 9th index.
del job_titles[8]
print()
print("Updated list after deleting the 9th index:")
print(job_titles)

# Print the last index.
print()
print("Last index is:", job_titles[-1])