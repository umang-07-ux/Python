def pallin(str):
    rev=""
    for i in range(len(str)-1,-1,-1):
        rev+=str[i]
    if str==rev:
        print("The string is pallindrome")
    else:
        print("The string is not pallindrome")

pallin("NAMAN")
pallin("umang")
