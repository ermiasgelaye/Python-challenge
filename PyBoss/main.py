
# Importing modules important for the analysis
import os
import csv

# Set relative path for csv file

data_path = os.path.join('..', 'Resources', 'employee_data.csv')

# Abrivation of ssates added form "https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5"
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
# A list to hold employees ID
employee_id = []
# A list to hold employees Firist Name
first_name = []
# A list to hold employees Last Name
last_name = []
# A list to hold  dob
dob = []
# A list to hold  SSN
ssn = []
# A list to hold states
state = []

# Read csv file
with open(data_path, 'r') as csvdata_path:
    reader = csv.DictReader(csvdata_path)
    # appends information to empty lists after being altered
    for row in reader:
        employee_id.append(row['Emp ID'])
        first_name.append(row['Name'].split(" ")[0])
        last_name.append(row['Name'].split(" ")[1])
        dob.append(row['DOB'].split('-')[1] + '/' +
                   row['DOB'].split('-')[2] + '/' + row['DOB'].split('-')[0])
        ssn.append('***-**-' + row['SSN'].split('-')[2])
        state.append(us_state_abbrev[row['State']])

# zips lists together
new_data = zip(employee_id, first_name, last_name, dob, ssn, state)

#names output data_path

doutput_file = os.path.join('..', 'Analysis', 'pyBoss_output.txt')

#open and writes to csv
with open(doutput_file, 'w') as csvwrite:
    cleandata_path = csv.writer(csvwrite, delimiter=",")
    cleandata_path.writerow(
        ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    cleandata_path.writerows(new_data)
