# Promptly - Quickly generate AI prompts from CSV files 
Promptly is a python script for quickly generating AI prompts. The script takes in two files (a .txt file that contains a prompt "skeleton" and a CSV file that contains "descriptors" and "phrases"). 

## Using Promptly

**Setup**: 
1. Install python3 if not already installed on your system

2. Clone the repository 

3. In the repository directory, create a .txt file for your prompt skeleton

4. In the repository directory, create a .csv file for filling in the prompt skeleton

**Running the script**: 

`python3 promptly.py <prompt.txt> <words.csv> <number of prompts to generate>`

## How it works
Promptly works by creating lists of keywords from a .csv file and phrases that can be stored with them. The script then parses a prompt stored in a .txt file and looks for places where the descriptors - marked by closed brackes ("[ ]") - will be replaced by words in the .csv dictionary. 


## Example Input and Output

`prompt.txt`: You are a [role or profession] who has been asked to solve [a problem]. Respond to the query following 'Prompt >' as if you are this person.

`dictionary.csv`: 

| descriptor | phrase |
| ---------- | -------|
|role or profession | doctor |
|role or profession | programmer |
|role or profession | designer |
|a problem | generative AI accuracy |
|a problem | defining open source AI |

`python3 promptly.py prompt.txt dictionary.csv 1`:
You are a designer who has been asked to solve generative AI accuracy. Respond to the query following 'Prompt >' as if you are this person.