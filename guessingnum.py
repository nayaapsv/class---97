import random

print("Number guessing game")
print("Guess a number (from 1 and 9):")

num = random.randint(1, 9)
chance = 0

if (chance>5) :
    print("You Lose The number is", num)

while chance < 5:

    guess = int(input("Enter your guess - "))

    if guess == num:
       
        print("You Won")
        

    
    elif guess < num:
        print("Your guess was too low  - Guess a number higher than", guess)

    
    else:
        print("Your guess was too high  - Guess a number lower than", guess)

    
    chance = chance+1



