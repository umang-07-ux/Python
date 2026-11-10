import random #It is a library in python to provide random numbers
randomNum=random.randint(1,10)
guess=int(input("Enter a random number:"))
if guess==randomNum:
    print("The guessed number is equal to the random number")
else:
    print(f"The guessed number is not equal to the random number, the random number is {randomNum} and the guessed number is {guess}")    