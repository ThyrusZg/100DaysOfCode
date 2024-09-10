import random

def get_random_word():
    file_input = open("words.txt").readlines()
    word = random.choice(file_input).strip("\n")
    return word

def hide_word(word):
    word_hidden = ['_' for l in word]
    return word_hidden


new_word = get_random_word()
new_hidden_word = hide_word(new_word)
counter = 6
win = False

print("Guess the word")
print("".join(new_hidden_word))
while counter > 0:
    letter = input(">")
    if letter in new_word:
        for i in range(len(new_word)):
            if letter == new_word[i]:
                new_hidden_word[i] = letter
                if '_' not in new_hidden_word:
                    print("You have guessed the word!")
                    win = True
        print("".join(new_hidden_word))
    else:
        counter -= 1
        print(f"Letter ''{letter}'' does not exist in the word!")
        print(f"{counter} lives left")
        print("*********************************************")
    if win:
        break

print(f"Word was {new_word}")