
import random
import words

player_name = input("Hi! Whats your name? ")



while True:
    get_level = input(f"""Okay {player_name}, Lets get ready to play. Choose your difficulty with a number:
    1 - Easy
    2 - Medium
    3 - Hard
    Pick your level: """)
    get_level = get_level.lower()
    if get_level == "1" or get_level == "easy":
        user_choice = words.easyWords
        break
    elif get_level == "2" or get_level == "medium":
        user_choice = words.mediumWords
        break
    elif get_level == "3" or get_level == "hard":
        user_choice = words.hardWords
        break
    else:
        print("Sorry I didn't understand that, let's try that again")

user_choice_word = user_choice.keys()
word_definition = user_choice.values()
def shuffle_word():

    
    for word in user_choice_word:
        print("".join(random.sample(word, k=len(word))))
        print("Definition:", user_choice[word])
        user_answer = input("What is the word? ")

        if user_answer.upper() == word:
            continue
        else:
            print("Sorry thats the wrong answer...")
            break
     
shuffle_word()








