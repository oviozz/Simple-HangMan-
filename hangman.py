

import random

# Word list
word = ['apple','banana','cat','dog']
word_picker = random.choice(word) # random  word picks
print(word_picker)

list_container = ['_' for i in word_picker] # makes container based on the length of the word
tries = 10

while  ''.join(list_container) != word_picker:
    user = input(f'Guess a letter{[tries]}: ')
    index_words_finding = [i for i in range(len(word_picker)) if word_picker[i] == user] # makes a list of index in instances if the users input letter is in the word

    tries -= 1
    if tries == 0:
        break

    if user in word_picker: # Merge the list_container correct index with the value
        for i in index_words_finding:
            list_container[i] = user
    else:
        print('Sorry, Wrong Guess!')
        continue
    print(''.join(list_container))
print()

if ''.join(list_container) == word_picker:
    print('Congratz You won!')
else:
    print('Sorry You Lost, Try again?')




