# The data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources\election_results.csv'
#file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
#election_data = open(file_to_load, 'r')
#election_data.close()

#with open(file_to_load, "r") as election_data:
    # Print the file object.
#    print(election_data)

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")

# Open the election results and read the file.
with open(file_to_load, "r") as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Print headers
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)

# Write some data to the file.
#outfile.write("Hellow World")
#txtfile.write("Hello World")

# Write three counties to the file.
#    txt_file.write("Counties in the Election\n")
#    txt_file.write("------------------------\n")
#    txt_file.write("Arapahoe\n")
#    txt_file.write("Denver\n")
#    txt_file.write("Jefferson\n")

#Close the file
#outfile.close()

