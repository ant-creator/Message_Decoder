#!/usr/bin/env python
# coding: utf-8

# In[11]:


def decode(message_file):
    # Read the contents of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    decoded_words = []
    current_number = 1

    # Iterate through each line in the file
    for line in lines:
        # Split the line into number and word
        number, word = line.strip().split(' ')
        number = int(number)

        # If the number matches the current number, add the word to the decoded message
        if number == current_number:
            decoded_words.append(word)
            current_number += 1

    # Join the decoded words into a single string
    decoded_message = ' '.join(decoded_words)
    return decoded_message

# Example usage:
decoded_message = decode('message_file.txt')
print(decoded_message)




# In[ ]:




