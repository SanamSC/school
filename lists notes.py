a= []                       #empty list
b=[1,2,3]                   #list of integers
c=[1,2.5,3.7,9]             #list of numbers(ints and floats)
d=["a","b","c"]             #list of characters
e=["a",1,"b",3.5,"zero"]    #list of mixed value types(string,int,float)
f=["One", "two", "three"]   #list of strings
print(f)

#mutability of lists
vowels = ["A","B","C","D","E"]
vowels[-1] = "Z"
#vowel should now be ["A","B","C", "D", "Z"]
print(vowels)

#Nested lists
l1=[3,4,[5,6],7]    #l1[2] = [5,6] as its a nested list
print(l1[2])

#CREATING LIST FROM SEQUENCES:
l1=list("hello")
print(l1)

t=("W","E","R","T","Y") # is a tuple 
l2 = list(t)            #converts it to a list
print(l2)               #prints list


#EVAL FUNCTION:
var1 = eval(input("enter a value:"))
print(var1,type(var1))


