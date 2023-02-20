import random
import hangman_art
import hangman_words
import os

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
winner = False

# display hint of the secret word
print(f"the secret word is: '{chosen_word}'")
#display logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    
    if guess in display:
      print(f"You already guessed {guess}")
  
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the secret word. You lose 1 life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(hangman_art.end)
            

    #Join all the elements in the list and turn it into a String.
    if lives != 0:
      print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(hangman_art.win)
        winner = True

    if lives != 0 and winner == False:
      print(hangman_art.stages[lives])