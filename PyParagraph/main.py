# Importing modules important for the analysis
import os
import re

# Set relative path for txt file
# select a paragraph 1 or paragraph 2 in the path for this test I choose paragraph 1

data_path = os.path.join('Resources', 'paragraph_1.txt')


# Holding a variable for paragraph

paragraph = ""

# Read the text file
with open(data_path) as txt_data:

    # Store the contents as a string (with no new lines)
    paragraph = txt_data.read().replace("\n", " ")
# Split the paragraph based on spaces to calculate word count
word_split = paragraph.split(" ")
word_count = len(word_split)

# Create a list for holding all the letter counts
letter_counts = []

# Loop through the word array and calculate the length of each word
for word in word_split:

    # Add each letter count into the letter_counts list
    letter_counts.append(len(word))

# Calculate the avg letter count
avg_letter_count = sum(letter_counts) / float(len(letter_counts))

# Re-split the original paragraph based on punctuation (. ? !)
sentence_split = re.split("(?<=[.!?]) +", paragraph)

print(sentence_split)
sentence_count = len(sentence_split)

words_per_sentence = []

# Loop through the sentence array and calculate the number of words in each
for sentence in sentence_split:

    # Calculate the number of words in each sentence and add to the list
    words_per_sentence.append(len(sentence.split(" ")))

# Calculate the avg word count (per sentence)
avg_sentence_len = sum(words_per_sentence) / float(len(words_per_sentence))

# Generate Paragraph Analysis Output
output = (
    f"\nParagraph Analysis\n"
    f"-----------------\n"
    f"Approximate Word Count: {word_count}\n"
    f"Approximate Sentence Count: {sentence_count}\n"
    f"Average Letter Count: {avg_letter_count}\n"
    f"Average Sentence Length: {avg_sentence_len}\n")

# Print all of the results (to terminal)
print(output)

# Save the results to analysis text file
output_file = os.path.join('Analysis', 'pyParagraph_output.txt')

with open(output_file, "a") as txt_file:
    txt_file.write(output)

# This Code is compiled and written for the Python class Homework in the Data Analytics Bootcamp class given by-Trilogy Education Services at the University of Toronto,continuing studies. The code used learning resources from the class.

# ©2020 Trilogy Education Services
