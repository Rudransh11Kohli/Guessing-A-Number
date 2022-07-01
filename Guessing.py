import random
num = random.randint(1, 50)                      

player_name = input('Hello! What is your name? ')
number_of_guesses = 0
player_guess = input('Okay.' + player_name + 'I am now going to guess a number between 1 & 50.')

while (number_of_guesses < 3):
    user_num = int(input('Guess? '))
    number_of_guesses +=1
    if (user_num > num):
        print("Sorry, your guess is too high.")
    if (user_num < num):
        print("Guess higher!")
    if user_num == num:
        break
if user_num == num:
    print("Well done! You guess the number right in" + str(number_of_guesses))
else:
    print("You miserably failed... The number was" + str(num))
    

