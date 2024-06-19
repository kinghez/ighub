"""
Author: Br. Solomon Itie
Course: CSE 110 (Introduction to Programming)
Project 04: Word Puzzle
Purpose: To write a program that uses loop to accomplish a meaningful task.
Task: To complete my program.
Kindly note that this program also contain the "Showing Creativity and Exceeding Requirements part.
"""

#Core requirement part

word = "mosiah"


hint = "_ _ _ _ _ _"


num_guess = 0

print(f"Your Hint Is:{hint}")

while num_guess >=0:
    num_guess +=1
    user = input("What is your guess?")
    
    if len(user) != len(word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        
        
    else:
        if user != word:
            lis_hint = hint.split(" ")
            for leta in user:
                if leta in word:
                    if user.index(leta) != word.index(leta):
                        ind = user.index(leta)
                        lis_hint[ind] = leta.lower()
                         
                    else:
                        ind = word.index(leta)
                        lis_hint[ind] = leta.upper()
                    
                else:
                    ind = user.index(leta)
                    lis_hint[ind] = "_"
                    
            print("Your Hint Is:"+ " ".join(lis_hint))
                     
        
        else:
             print("Congratulations! You guessed it!")
             print(f"It took you {num_guess} guesses.")
             break
   
        

        
    
        
