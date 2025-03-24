num1 = int(input("give me a number"))
num2 = int(input("give me a second number"))
if num1 > num2 :
    print (num2 , num1)
else:
    print (num1 , num2)

num3 = int(input("enter a number under 20"))
if num3 > 20 :
    print ("Too high!")
else:
    print ("thank you!")
    

num4 = int(input("enter a number between 10 and 20 please"))
if num4 >= 10 and num4 <= 20 :
    print ("Thank you!")
else:
    print ("Incorrect asnwer")
    

fav_colour = input("whats your favourite colour")
if fav_colour == "red" :
    print("i like red too!")
else:
    print(f"I dont like {fav_colour}, i prefer red")
    
    
weather = input(" is it raining lad?!")
print (weather.lower())
if weather == "yes" :
    print("is it too windy for an umbrella")
else:
    print("take an umbrella")
    
age = int(input("Enter your age"))
if age >= 18 :
          print("you can vote")
if age ==17 :
          print("you can learn to drive")
if age == 16 :
          print("you can buy a lottery ticket")
if age <= 16 :
          print("you can go trick or treating")
          

num5 = int(input("Enter a number"))
if num5 < 10 :
    print ("Too low")
elif num5 <= 11 and num5 <= 20 :
    print("Correct")
else:
    print("Too high")
    
num6 = int(input("enter 1, 2 or 3"))
if num6 == 1 :
    print("thank you!")
if num6 == 2 :
    print("Well done")
if num6 == 3 :
    print("Correct!")
if num6 > 3 :
    print("Error message")