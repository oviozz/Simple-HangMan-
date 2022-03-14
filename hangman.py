import requests
from bs4 import BeautifulSoup
import lxml

word_url = 'https://randomword.com'

request = requests.get(word_url).text
soup = BeautifulSoup(request,'lxml')
game_word = soup.find('div',id='random_word').text


list_container = ['_' for i in game_word] # makes container based on the length of the word
tries = len(game_word) + 5

while  ''.join(list_container) != game_word:
    user = input(f'Guess a letter{[tries]}: ')
    index_words_finding = [i for i in range(len(game_word)) if game_word[i] == user] # makes a list of index in instances if the users input letter is in the word

    tries -= 1
    if tries == 0:
        break

    if user in game_word: # Merge the list_container correct index with the value
        for i in index_words_finding:
            list_container[i] = user
    else:
        print('Sorry, Wrong Guess!')
        continue
    print(''.join(list_container))
print()

if ''.join(list_container) == game_word:
    print('Congratz You won!')
else:
    print('Sorry You Lost, Try again?')





