a=[]                        #empty list
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
var1 = eval(input("enter a value to evaluate:"))
print(var1,type(var1))


#joining lists
lst1=[10,12,14]
lst2=[20,22,24]
lst3=[30,32,34]
lst=lst1+lst2+lst3
print(lst)

#slicing list
lst=[10,12,14,20,22,24,30,32,24]
seq=lst[3:-3]                   #start:stop
print("list slice: ", seq)
seq2=lst[0:10:2]
print("LIST SLICE:", seq2)                     #start:stop:step

#appending items to a list:
lst = [10,12,14]
lst.append(16)
print("appended list:", lst)

#updating elements to a list
lst=[10,12,14,16]
lst[2]=24
print("updated list:",lst)     #changes number in position 2 to a "24"

#deleting from list
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
del lst[10]
print(lst)

#index ,method returns the index of first matched item from the list.
list=[12,14,16,18,20,18,16,14,12]
list.index(18)
print(list)

#extend method is used to add multiple elements to a list.
t1=["a","b","c"]
t2=["d","e"]
t1.extend(t2)
print("extended list of t1+t2 is:",t1)

#insert method can add elements into a list in any positon you want
t1=["a","e","u"]
t1.insert(2,"I")
print(t1)           #inserts "I" into position 2

#remove method
t1=["a","b","c","d","e","f"]
t1.remove("a") 
print(t1)                  #removes A from the list


#clear method
l1=[2,3,4,5]
l1.clear()
print(l1)


#reverse method
t1=[1,2,3,4,5,6,7]
t1.reverse()
print("reversed list is:",t1)


#sort method
t1=["e","i","q","a","q","p"]
t1.sort()
print(t1)


#programing Examples:
#program 11.3                #enter:2,3,4,-2,6,-7,8,11,-9,11
lst=eval(input("enter list:"))
lenght=len(lst)
min_ele=lst[0]
min_index=0
for i in range(1,lenght):
    if lst[i] < min_ele:
        min_ele = lst[i]
        min_index = i
print("Given list is: ", lst)
print("The minimum element of the given list is:")
print(min_ele, "at index", min_index)


#program 11.4                   ##enter:7,23,-11,55,13.5,20.05,-5.5
lst=eval(input("Enter list:"))
lenght=len(lst)
mean=sum=0
for i in range(0,lenght):
    sum+=lst[i]
mean = sum/lenght
print("Given list is :", lst)
print("The mean of the given list is:", mean)

#11.5
lst=eval(input("enter list:")) 
lenght = len(lst)
element = int(input("Enter element to be searched for"))
for i in range(0, lenght):
    if element == lst[i]:
        print(element, "found at index", i)
        break
else:                                                   #else of for loop
    print(element,"not found in given list")
    
    
#11.6
lst=eval(input("Enter list:"))    #enter: 1,1,1,2,2,2,3,4,2,2,5,5,2,2,5
lenght = len(lst)
element = int(input("enter element"))   #enter:2
count = 0
for i in range(0,lenght):
    if element ==lst[i]:
        count+=1
if count == 0:
    print(element, "not found in given list")
else:
    print(element, "has frequency as", count, "in given list")
    
    
#11.7
lst = eval(input("Enter list:"))
lenght = len(lst)
uniq = []
dupl = []
count = i = 0
while i < lenght:
    element = lst[i]
    count =1
    if element not in uniq and element not in dupl:
        i+=1
        for j in range(i,lenght):
            count += 1
        else:
            print("Element", element, "frequency:", count)
            if count ==1:
                uniq.append(element)
            else:
                dupl.append(element)
    else:
        i+=1
print("Original list", lst)
print("Unique elements list", uniq)
print("Duplicates elements list", dupl)





    
    




