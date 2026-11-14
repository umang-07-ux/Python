# We can open any file using its path 
# 'r' is used to read the file-
# p=open(r'C:\Users\ASUS\Desktop\1)High Order Functions-.txt')
# print(p.read()) # Used to red the file

# p2=open(r'FileHandling.py') # we can also open python files
# print(p2.read())

# Use of 'w'-it is used to create or overwrite a file.
# a=open("superman.txt",'w')  # this made a new file.
# a.write("Hello this is Umang and i was inside this file")
# a.close()

# Use of 'a'- it is used to append in the file as i we use 'w' then that will always overwrites so that is why 'a' is used to add further content.
# it also creates the file.
b=open("superman.txt",'a')
b.write(", and now i am appending some content inside this file")
b.close()