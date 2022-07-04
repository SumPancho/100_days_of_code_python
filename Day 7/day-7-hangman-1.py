#Step 1 

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess= input("Guess a letter: ")
guess= guess.lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

counter = 0

while counter < len(chosen_word):
  if chosen_word[counter] == guess:
    print("RIGHT")
  else:
    print("WRONG")
  counter += 1