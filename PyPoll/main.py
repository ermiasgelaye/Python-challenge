# Importing modules important for the analysis
import os
import csv

data_path = os.path.join('/Users/ermiasgaga/documents/GitHub/python-challenge/PyPoll/', 'Resources', "election_data.csv")

# A list to hold the names of candidates
candidates = []

# A list to hold the number of votes each candidate receives
num_votes = []

# A list to hold the percentage of total votes each candidates
percent_votes = []

# A counter for the total number of votes
total_votes = 0

with open(data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote-counter
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
