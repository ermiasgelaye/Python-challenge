# Importing modules important for the analysis
import os
import re

# Set relative path for txt file

data_path = os.path.join('/Users/ermiasgaga/documents/GitHub/python-challenge/pyParagraph/', 'Resources', 'paragraph_1.txt')


# Holding a variable for paragraph

paragraph = ""

# Read the text file
with open(data_path) as txt_data:

    # Store the contents as a string (with no new lines)
    paragraph = txt_data.read().replace("\n", " ")
