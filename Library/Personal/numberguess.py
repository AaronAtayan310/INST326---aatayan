import random

n1 = int(input("Enter a lower bound number: "))
n2 = int(input("Enter an upper bound number: "))
answer = random.randint(n1, n2)

i = 0
while True:
    guess = int(input("Enter your guess of what the number generated is: "))
    i += 1

    if guess < answer:
        print("Guess is lower than Answer")
    elif guess > answer:
        print("Guess is greater than Answer")
    else:
        if i == 1:
            print("Nice! You got it in one try!!")
        else:
            print("Correct! The generated number was: " + str(guess))
            print("Total guesses: " + str(i))
        break