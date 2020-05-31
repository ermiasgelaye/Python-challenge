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