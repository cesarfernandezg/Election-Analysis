# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# get the candidates options with a list
candidate_options = []

# declare empty dictionary
candidate_votes = {}

# Winning candidate and winning ount tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    # read the fle object with the reader function
    file_reader = csv.reader(election_data)
# Print each row in the CSV file
    # for row in file_reader:
    #     print(row[0])
# read and print the header row
    headers = next(file_reader)
    
# print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote coun
        total_votes += 1

        # print candidates name
        candidate_name = row[2]

        # if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

        # add candidate name to the candidate list
            candidate_options.append(candidate_name)
        
        # track candidates vote count
            candidate_votes[candidate_name] = 0
        # increment the votes by 1 for each candidate
        candidate_votes[candidate_name] += 1

# save results to a text file
with open (file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

        # determine the percentage of votes 
        # 1. iterate through the candidate list
    for candidate_name in candidate_votes:
        # 2. retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. print candidate name and percentage of votes
        # print(f"{candidate_name}: received {vote_percentage}% of the vote")
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
    #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        # To do: print out the winning candidate, vote count and percentage to
        # terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # print(winning_candidate_summary)

    # for our analysis we dont need the column headers
    # to skip the header row use the next() method

    # print candidate options
    #print(candidate_options)
    # print candidate vote dictionary
    # print(candidate_votes)
    # # 3. Print total votes
    # print(total_votes)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)




