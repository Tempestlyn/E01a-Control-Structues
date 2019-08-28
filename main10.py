#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #prints "Greetings"
colors = ['red','orange','yellow','green','blue','violet','purple'] #creates a list of strings
play_again = '' #creates a string variable
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #checks to see if the user wants to "play again"
    match_color = random.choice(colors) #assigns a random string from colors to match color
    count = 0 #sets count eqaul to 0
    color = '' #sets color eqaul to empty string
    while (color != match_color): #checks to see if color is not eqaul to match color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #lowercases and removes surrounding spaces from color
        count += 1 #adds 1 to number of attempts
        if (color == match_color): #checks to see if color is matched color
            print('Correct!') #displays "correct"
        else: #if it isn't eqaul...
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #prints that the user is incorrect and the number of attempts
    print('\nYou guessed it in {0} tries!'.format(count)) #prints the number of guesses when user is correct
    if (count < best_count): #if count is less than best count...
        print('This was your best guess so far!') #prints that the user has a new least attempts
        best_count = count #makes the best count eqaul to current count
    play_again = input("\nWould you like to play again? ").lower().strip() #prompts an input asking if the user would like to play again, while also assigning the input as the variable play again
print('Thanks for playing!') #if the user inputs no, it prints thanks for playing