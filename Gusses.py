SECRET_NUMBER = 9
GUESS_COUNT = 0
GUESS_LIMIT = 3
while GUESS_COUNT < GUESS_LIMIT:
    GUESS = int(input('Guess : '))
    GUESS_COUNT += 1
    if GUESS == SECRET_NUMBER:
        print('You Won !')
        break
else:                                   # This is While else not if else Python special feature
    print("Sorry you failed!")
