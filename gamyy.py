import random
from unittest import result
from hangman import hangman
import sys
words=["apple","orange","graphes"]
word=random.choice(words)


def game(words):
    guess_word=["_" for i in word]
    tries=0
    print(hangman[tries])
    print("Guess word:{}".format(" ".join(guess_word)))
    while True:
        user=input("Enter a letter[a-z]")
        if not user.isalpha():
            print("please enter only in[a-z]only\n")
            continue
        if user in word:
            indexes=[i for i in range(len(word)) if word[i]==user]
            for index in indexes:
                guess_word[index]=user
            print("="*50)
            print("Good:{}".format(" ".join(guess_word)))
            if "".join(guess_word)==word:
                print( "Wow! you guessed:)")
                break
        
        else:
            tries+=1
            print(hangman[tries])
            if tries==6:
                return "game over"
            print("sorry, try again\n ")
        
        
        

if __name__ == "__main__":
    while True:
        word = random.choice(words)
        game(word)

        while True:
            play_again = input("Play again? [y/q]: ").lower()
            if play_again == "y":
                break  # break inner loop and start a new game
            elif play_again == "q":
                print("Thanks for playing! Bye!")
                exit()  # exit program completely
            else:
                print("Please enter 'y' to play again or 'q' to quit.")

   
