low = 1
high = 1000
print("Please think of a number between {} and {}:".format(low,high))
input("Press ENTER to start the game.")
guesses = 1

while True:
    guess = low + (high - low) // 2
    hi_lo = input("My guess is {}. Enter 'h', 'l' or 'c' to guess higher, lower or correct.".format(guess)).casefold()

    if hi_lo == "h":
        #guess higher. the low end of the guess becomes 1 greater than the guess.
        low = guess + 1
    elif hi_lo == "l":
        #guess lower. the high end of the guess becomes 1 less than the guess.
        high = guess - 1
    elif hi_lo == "c":
        print("I got it right in {} guesses..!\n".format(guesses))
        break
    else:
        print("please enter h, l or c for high, low, and correct respectively.")
    
    guesses += 1
    
