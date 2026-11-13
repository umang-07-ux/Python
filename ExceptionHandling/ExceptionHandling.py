a=int(input("Enter a number:"))

try:
    print(10/a)   # this line can give an exception if we divide by 0 and due to this lines below this will not execute, so to avoid this we put it into 'try' block.

except Exception as err:   # with try block we have to add an except block or a finally block.
    print(f"Sorry there is an error as {err}")

# else block is paired with except block and if there is exception then except block will run and if ther eis no error then else block will run.
else:
    print("Good there is no error")

print("Ok I have done the division")

# finally block-finally block wo bloxk hai jo ki chalega whether there is an exception or not.
b=int(input("Enter a number:"))

try:
    print(10/b)

except Exception as err:
    print(f"Sorry there is error which is {err}")

finally:
    print("I will run no matter what")

# raise block- it is use to explicitly raise an error.
age=int(input("Enter you age-"))

try:
    if age < 10 or age > 18:
        raise ValueError("Your age must be between 10 and 18")

    else:
        print("Welcome to the club")

except Exception as err:
    print(f"An error has occured which is {err}")

print("The club will start soon!")