#2.Write a python program to find the wordcount in a file (input.txt) for each line and then print the output. 
#Finally store the output in output.txt file. Example: Input: a file includes two lines: Python Course Deep Learning Course Output: Python Course Deep Learning Course Word_Count: Python: 1 Course: 2 Deep: 1 Learning: 1
#Student Name: Yamini Saraswathi Borra
#Student ID: 700748022

from collections import Counter

# Read input from file
with open('C:\\Users\\M1097753\\Documents\\GITHUB\\input.txt', 'r') as file:
    lines = file.readlines()

# Initialize a Counter to store word counts
word_counts = Counter()

# Process each line
for line in lines:
    # Tokenize the line into words
    words = line.split()
    
    # Update word counts for the current line
    word_counts.update(words)

# Print the output
print('\n'.join(lines).strip())
print('Word_Count:')
for word, count in word_counts.items():
    print(f'{word}: {count}')

# Store the output in the output.txt file
with open('output.txt', 'w') as output_file:
    output_file.write('\n'.join(lines).strip() + '\n')
    output_file.write('Word_Count:\n')
    for word, count in word_counts.items():
        output_file.write(f'{word}: {count}\n')