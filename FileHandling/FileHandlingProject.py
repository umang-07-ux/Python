# Doing CRUD operations using File Handling

from pathlib import Path
import os

# Path ka use files aur folders ke paths ko handle karne ke liye hota hai.

# Function to display all files and folders
def readfileandfolder():
    path = Path('')  # Current working directory ko represent karta hai.
    items = list(path.rglob('*'))  # rglob('*') current directory ke saare files aur folders find karta hai.

    # enumerate() index aur item dono provide karta hai.
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")


# Creating a file:
def createfile():
    try:
        readfileandfolder()

        name = input("Please tell your file name :-")
        p = Path(name)  # User ke diye hue name ka Path object banata hai.

        if not p.exists():  # exists() check karta hai ki file ya folder already exist karta hai ya nahi.
            with open(p, "w") as fs:
                # with automatically file ko close kar deta hai.
                # "w" mode file create karta hai aur existing data ko overwrite karta hai.

                data = input("What you want to write in this file :-")
                fs.write(data)  # write() file ke andar data likhta hai.

            print("FILE CREATED SUCCESSFULLY")

        else:
            print("This file already exist")

    except Exception as err:
        # except error ko handle karta hai.
        # err mein error ki information store hoti hai.
        print(f"An error occured as {err}")


# Reading a file:
def readfile():
    try:
        readfileandfolder()

        name = input("Which file you want to read")
        p = Path(name)

        # exists() check karta hai ki path exist karta hai.
        # is_file() check karta hai ki given path ek file hai ya nahi.
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                # "r" mode ka use file ko read karne ke liye hota hai.

                data = fs.read()  # read() poori file ka data read karta hai.
                print(data)

            print("FILE READ SUCCESSFULLY")

        else:
            print("The file does not exist")

    except Exception as err:
        print(f"An error occur as {err}")


# Updating a file:
def updatefile():
    try:
        readfileandfolder()

        name = input("Tell which file you want to update")
        p = Path(name)

        if p.exists() and p.is_file():

            print("Press 1 for changing the name of the file :-")
            print("Press 2 for overwriting the data of your file :-")
            print("Press 3 for appending some content in your file:-")

            res = int(input("Tell your response :-"))

            if res == 1:
                name2 = input("Tell me the new file name :-")
                p2 = Path(name2)

                p.rename(p2)  # rename() file ka name change karta hai.
                print("FILE RENAMED")

            if res == 2:
                with open(p, 'w') as fs:
                    # "w" mode purane data ko delete karke naya data write karta hai.

                    data = input("Tell what you want to write, this will overwrite the data :-")
                    fs.write(data)
                    print("DATA OVERWRITTEN")

            if res == 3:
                with open(p, 'a') as fs:
                    # "a" mode existing data ko delete nahi karta.
                    # Ye file ke end mein new data add karta hai.

                    data = input("Tell what you want to append :-")
                    fs.write(" " + data)
                    print("APPENDING DONE")

    except Exception as err:
        print(f"An error occured as {err}")


# Deleting a file:
def deletefile():
    try:
        readfileandfolder()

        name = input("Which file you want to delete :-")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)  # remove() file ko permanently delete karta hai.
            print("FILE REMOVED SUCCESSFULLY")

        else:
            print("No such file exist")

    except Exception as err:
        print(f"An error occured as {err}")


# Main Menu
print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("Please tell your response :-"))

# User ke input ke according respective function call hoga.

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()
