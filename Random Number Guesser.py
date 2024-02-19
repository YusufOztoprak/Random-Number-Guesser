#!/usr/bin/env python
# coding: utf-8

# In[6]:


def RandomNumberGuesser():
    import random
    import time
    
    print("Welcome to the Random Number Guesser. \n ****************\n I am thinking of a number between 1 and 100. Can you guess it?")
    time.sleep(1)
    right_to_guess= 6
    secret_number = round(random.random()*99 + 1)
    
    while right_to_guess > 0:
        print("You have " + str(right_to_guess) + " guesses left.")
        guess = int(input("Take a guess: "))
        
        if guess > secret_number:
            print("Computer is guessing...")
            time.sleep(1)
            print("Your guess is too high.")
        
        elif guess < secret_number:
            print("Computer is guessing...")
            time.sleep(1)
            print("Your guess is too low.")
        
        else:
            print("Computer is guessing...")
            time.sleep(1)
            print("Good job! You guessed my number in " + str(6 - right_to_guess) + " guesses!")
            break

        right_to_guess = right_to_guess - 1
    
    if right_to_guess == 0:
        print("Sorry, you ran out of guesses. The number I was thinking of was " + str(secret_number) + ".")
    
    
RandomNumberGuesser()


# In[ ]:





# In[ ]:




