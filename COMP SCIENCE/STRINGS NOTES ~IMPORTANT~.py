#TRAVERSING A STRING#

#1
name = "superb"
for ch in name:
    print(ch,"-", end = "")
#above code should print: s-u-p-u-r-b-
    
    
#2
string1 = input("enter a string")
print("the", string1 , "in reverese order is:")
lenght = len(string1)
for a in range(-1 , (-lenght -1), -1):
    print(string1[a])
    
