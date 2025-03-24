#45
total = 0
while total <= 50:
    num = int(input("enter a number"))
    total = total + num
    print("the total is", total)

#46
num2 = int(input("enter a number"))
while num2 <= 5:
    num2 = int(input("enter a number"))
print("the last number you entered was a", num2)


#47
num3 = int(input("enter a number"))
num4 = int(input("enter another number"))
num5 = num3 + num4
print(num5)
ask = input("do you want to add another number")
while ask == "y":
    numero = int(input("enter another number"))
    ask = input("do you want to add another number")
    print(numero + num5)



