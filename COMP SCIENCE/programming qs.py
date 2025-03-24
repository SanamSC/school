
#1
lst1=input("enter a list")
list_of_input=list(lst1)
list_of_input.reverse()
print(list_of_input)

#2
input1= input("enter a list")
list1 = list(input1)
input2=input("enter a second list")
list2=list(input2)
list3 = list1+list2
print(list3)


#3
list2= input("Enter a list of 1-12:")
lista = list(list2)
lenght = len(list2)
for i in range(0,lenght):
    if i>10:
        lista[i] = 10
print(lista)

#4
lista = input("Enter a list of strings")
izlist= list(lista)
lenghty = len(izlist)
list4 = izlist.remove(1,"_")
print(list4)

        
        
    



