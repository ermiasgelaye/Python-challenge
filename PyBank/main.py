import os
import csv
# Set relative path for csv file
data_path=os.path.join('/Users/ermiasgaga/documents/GitHub/python-challenge/PyBank/', 'Resources', 'budget_data.csv')
# counter for the total number of months
total_months = 0

# A counter for the total profit and loss
total_profit_loss = 0

# A counter for the output value of total profit and loss
value = 0

# A counter for the output value of total profit and loss
change = 0

# A list to hold the dates of the financial records
dates = []

# A list to hold the profits/loss
profits = []

# Read csv file
with open(data_path, newline="") as budget_file:
    csvreader = csv.reader(budget_file, delimiter=",")
    # Reading header row
    csv_header = next(csvreader)
    # Go to the first row


    first_row = next(csvreader)

    total_months += 1

    total_profit_loss += int(first_row[1])
    value = int(first_row[1])
    # Read the rows after the header row
  


