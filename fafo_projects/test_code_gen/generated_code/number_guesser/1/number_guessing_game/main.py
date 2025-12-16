import random

number_to_guess = random.randint(1, 100)

while True:
    user_guess = int(input('Guess a number between 1 and 100: '))
    if user_guess < number_to_guess:
        print('Too low!')
    elif user_guess > number_to_guess:
        print('Too high!')
    else:
        print('Congratulations! You guessed the number.')
        break