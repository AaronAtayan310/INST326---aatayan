import random

n1 = int(input("Enter a lower bound number: "))
n2 = int(input("Enter an upper bound number: "))
answer = random.randint(n1, n2)

guess = int(input("Enter your guess of what the number generated is: "))

i = 0
while i < 100:
    i += 1
    guess = int(input("Enter your guess of what the number generated is: "))
    if guess < answer:
        print("Guess is lower than Answer")
        continue
    if guess > answer:
        print("Guess is higher than Answer")
        continue
    if guess == answer:
        print("Correct! The generated number was: " + answer)
        print("Total guesses: " + i)
        break