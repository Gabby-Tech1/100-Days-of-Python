import random
import hangman_word
import hangman_art
random_word = random.choice(hangman_word.word_list)

lives = 6
display = []
print(hangman_art.logo)
        
for i in range(len(random_word)):
    display += "_"

end_of_game = False
while not end_of_game:    
    guess = input("Can you guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}")

    for i in range(len(random_word)):
        letter = random_word[i]
        if letter == guess:
            display[i] = guess
            
    print(hangman_art.stages[lives])
    
    if guess not in random_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lost")
    
    if "_" not in display:
        end_of_game = True
        print("You won")
                