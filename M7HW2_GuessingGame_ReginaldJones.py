#A Guessing game that allows a person to enter a number and guess which number is given
#12/9/2017
#CTI-110 M7HW2 - Random Number Guessing Game
#Reginald Jones
#

import random #import of random fuction

def main():
    
    number = random.randint(1, 5)
    again = 'y'
    
    while again == 'y' or again == 'Y': #While statement to retry if guess is wrong
        
        guess = int(input('Please choose a number between 1 and 5...   '))
        #Guesses are given between 1 and 5
        guess = int(guess)

        if guess == number:
            print ('Lucky You! You guessed the right number!')
            
        if guess < number:
            print ('Hmmm not quite...A little lower')
            
        if guess > number:
            print ('Hmmm not quite...A little higher')
            
        else:
            again = input('Try Again? ("y" or "Y" for Yes):  ')
            
main()
