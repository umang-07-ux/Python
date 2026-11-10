import random #It is a library in python to provide random numbers
randomNum=random.randint(1,10)
tries=0
while True:
    guess=int(input("Guess a number between 1 and 10:"))
    if guess==randomNum:
        tries+=1
        print(f"The guessed number is equal to the random number and you took {tries} tries")
        break
    elif guess > randomNum:
        tries+=1
        print("You guessed a little higher number")
    elif guess < randomNum:
        tries+=1
        print("You guessed a little lower number")
    else:
        print(f"Sorry you are wrong")    