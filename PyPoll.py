# The data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load, "r") as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Print headers
    headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to candidate list
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
    
        # Update candidate count
        candidate_votes[candidate_name] += 1

# Save results to a file
with open(file_to_save, "w") as txt_file:
    election_results =  (
                        f"\nElection Results \n"
                        f"-------------------------- \n"
                        f"Total Votes: {total_votes:,} \n"
                        f"-------------------------- \n"
                        )
    txt_file.write(election_results)   
    
    #Print Total Votes
    #print(total_votes)

    # Print Candidate list
    #print(candidate_options)

    #Print Votes per Candidate
    #print(candidate_votes)

    # Print percentage of votes for each candidate
    for candidate in candidate_options:
        votes = candidate_votes[candidate]
        percent_votes = float(votes)/float(total_votes)*100
        #print(f"{candidate}:  {percent_votes:.1f}% ({votes:,}). \n")
        candidate_result = (f"{candidate}:  {percent_votes:.1f}% ({votes:,}). \n")
        txt_file.write(candidate_result)

        # Determine winner stats
        if votes > winning_count and percent_votes > winning_percentage:
            winning_candidate = candidate
            winning_count = votes
            winning_percentage = percent_votes

    # Print winning candidate stats 
    winning_candidate_summary = (f"---------------------------------------- \n"
                                f"Winner: {winning_candidate} \n"
                                f"Winning Vote Count: {winning_count:,} \n"
                                f"Winning Percentage: {winning_percentage:.1f}% \n"
                                f"---------------------------------------- \n"
                                )
    #print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
