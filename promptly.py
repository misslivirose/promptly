# Import needed libraries
import csv
import sys
import random

# Store number of random prompts to generate
num_prompts = int(sys.argv[1])

# Set up our data structures for the prompt
replacements = []

# Set up our data structures for the CSV files
descriptors = []
phrases = []

# Provide prompt skeleton
original_prompt = "You are a [Profession or role that requires coming up with new ideas] who has been tasked with [A type of problem or project / job to be done]. You have a degree in [Degree] and experience working at [Company, non-profit, or public institution], [Company, non-profit, or public institution], and [Company, non-profit, or public institution]. You now work at Mozilla, and your professional values include [Values that you would find that a Mozilla employee has], [Values that you would find that a Mozilla employee has], and [Values that you would find that a Mozilla employee has]. You have access to a library of articles and resources that have been shared with you by your team, and you are looking to find new insights and ideas from these resources. Following the word “Prompt >”, you will be given a question by one of your team members who is trying to find new insights from the library that you have access to. Respond as the persona above, with a goal of generating a brand new idea and citing your sources."

# Test that phrases are properly saved
def print_phrases(): 
    for phrase in phrases: 
        print(str(phrase))

# Test that prompt is correctly processed
def print_prompt_replacements(): 
    for replacement_phrase in replacements:
        print(str(replacement_phrase))

# Choose a random item from the supplied list of phrases
def choose_random_word(descriptor_phrase, existing_text):
    reduced_list = []
    for item in phrases:
        if item[0] == descriptor_phrase:
            reduced_list.append(item[1]) 

    # Check for duplicates and replace the word if it's already been used
    def choose_word_and_check_for_duplicates():               
        new_index = random.randint(0, len(reduced_list)-1)
        proposed_word = reduced_list[new_index]
        try: 
            existing_text.index(proposed_word)
            choose_word_and_check_for_duplicates()
        except ValueError:
            return proposed_word

    new_word = str(choose_word_and_check_for_duplicates())
    return new_word

# Generate a random individual prompt by replacing descriptor fragments
def generate_random_prompt(prmpt, replacements_to_make):
    if(len(replacements_to_make) > 0):
      replacement_key = replacements_to_make.pop(0)
      replacement_word = choose_random_word(replacement_key, prmpt)
      tmp_prmpt = prmpt.replace(replacement_key, replacement_word, 1)
      generate_random_prompt(tmp_prmpt, replacements_to_make)  
    else:
        print(prmpt)

# Generate a number of random prompts as specified in the program arguments    
def generate_random_prompts():
    i = 0
    while i < num_prompts: 
        generate_random_prompt(original_prompt, replacements)
        i += 1

# Process the prompt given
def process_prompt(prompt):
    try: 
        next_replacement_start = prompt.index('[')
        next_replacement_end = prompt.index(']')
        replacements.append(prompt[int(next_replacement_start): int(next_replacement_end)+1])
        new_prompt = prompt[int(next_replacement_end)+1:]
        process_prompt(new_prompt)

    except ValueError: 
        generate_random_prompts()
        

# Read in from our test csv file to store items
with open('promptly_test.csv', newline='') as csv_file: 
    reader = csv.DictReader(csv_file)
    for row in reader:
        try: 
            descriptors.index(row['descriptor'])
        except ValueError: 
            descriptors.append(row['descriptor'])

        phrases.append(('[' + row['descriptor'] + ']', row['phrase']))

    process_prompt(original_prompt)




