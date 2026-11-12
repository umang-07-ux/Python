# List -
a = [12,13,14,15,16,16] #It is called a list.
print(type(a)) #O/P-<class 'list'>
b=[12,"umang",True,12.5,0] #We can store different kinds of datatypes.
print(b[1]) #We can access the values using the index of the values as lists are odered DS.
print(a[0:4]) #We can also perform slicing like we do in string.
print(b[-2]) #O/P-12.5

# list are mutable-
a[3]=9 #Changes the value at index 3.
#1st way of traversing on list using index-
for i in range(len(a)):
    print(a[i])

# 2nd way directly on values-
for i in a:
    print(i)

# Methods of list-
print(dir(list)) #tells all the methods of list.
# can refer to the python book.

# ----------------------------------------------------------------------------------------------
# Tuple
c=(1,2,3,4,4,5) #this is a tuple
print(type(c)) #O/P-<class 'tuple'>

# Tuples are immutable
# c[0]=12
# print(c) ,This will give error

print(c[2]) #O/P-3 , as tuple are also ordered DS.

d=(1,2,3,4.5,"Umang")
print(d)

# Can do traversing same as list.

# methods of tuple-(only two are there)
index=d.index(4.5)
print(index) #O/P-3
counts=c.count(4)
print(counts) #O/P-2

# tuple unpacking-
p,q,r,s,t=(1,2,3,4,5) #All there types are now integer and this is only what tuple unpacking is.
print(p) #1 
print(q) #2
print(r) #3
print(s) #4
print(t) #5

# ----------------------------------------------------------------------------------------------
# Set
e={1,2,8,9,3,4,5} #this is set and every element must be unique

# sets are mutable

# sets are unordered so no index values as set uses hash values to store the elements.

# Ex of hash-
c=hash((1,2,3,4))
print(c)  #it will always going to give a random big number.

# traversing in set-
for i in e:
    print(i) #its order of giving output always changes

# set methods-
f = {1, 2, 3}

f.add(4) # Adds an element to the set
print(f)
f.remove(2)# Removes 2 (Raises an error if not found)
print(f)
f.discard(5) # Removes 5 (No error if not found)
print(f)
popped_element = f.pop() # Removes a random element
print(f)
f.clear() # Removes all elements
print(f)

# Some methods to perform between two sets-
g={1,2,3}
h={3,4,5}

union_set = g.union(h)
print(union_set) #{1,2,3,4,5}
intersection_set = g.intersection(h)
print(intersection_set) #{3}
difference_set = g.difference(h) #difference_set=g-h
print(difference_set) #{1,2}
difference_set2 = h.difference(g) #differnce_set2=h-g
print(difference_set2) #{4,5}
symmetric_diff = g.symmetric_difference(h) #symmetric_diff=g^h
print(symmetric_diff) #{1,2,4,5}

h-=g
print(h) #{4,5}

# -------------------------------------------------------------------------------------------------
# Dictionary-(Same as Hashmap)
# Has key,value pair
k={1:"Umang",2:56}
m={}
print(type(m)) #<class 'dict'>
l={10:100,20:200,30:300,40:400}
print(l[20]) #200 ,We can access the values using there keys

l[30]=3000
print(l) #{10: 100, 20: 200, 30: 3000, 40: 400}

# Adding new key,value
l.update({50:500})
print(l) #{10: 100, 20: 200, 30: 3000, 40: 400, 50: 500}
# Or We can simply do-
l[60]=600 #Creating value
print(l) #{10: 100, 20: 200, 30: 3000, 40: 400, 50: 500, 60: 600}

# Deleting-
del l[30]
print(l) #{10: 100, 20: 200, 40: 400, 50: 500, 60: 600}


# Traversing in dictionary-
for i in l:
    print(i) #prints only keys
    print(l[i]) #print only values

# another way to traverse values-
for i in l.values():
    print(i) #gives values

# Merging two dictionary-
d1={10:100,20:200,30:300}
d2={40:400,50:500,60:600}

for i in d2:
    d1[i]=d2[i] # adding d2 dictinary in d1

print(d1) #{10: 100, 20: 200, 30: 300, 40: 400, 50: 500, 60: 600}


# Finding frequency of the element using dictionary-
li=[1,1,2,3,3,3,2,4,5,5,5,6,7]
d3={}

for i in li:
    if i in d3.keys():
        d3[i]+=1 # d3[i]=d3[i]+1, here the d3[i] on the left side is the key or the value of the list and the d3[i] on the right side gives the value or the frequency for the current key or the element of the list.
    else:
        d3[i]=1
 
print(d3) # {1: 2, 2: 2, 3: 3, 4: 1, 5: 3, 6: 1, 7: 1}

# Adding the values of same keys in two dictionary-
d4={10:100,20:200,30:300,40:400}
d5={40:400,50:500,60:600,70:700}

for i in d5:
    if i in d4.keys():
        d4[i]+=d5[i]
    else:
        d4[i]=d5[i]

print(d4) # {10: 100, 20: 200, 30: 300, 40: 800, 50: 500, 60: 600, 70: 700}