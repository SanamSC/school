'''
#1 a)
print("""
1
    2
        3
""")

#b)
text = "Test.\nNext line."
print(text)

#c)
print("one", "two" *2)
print("one" + "two" *2)
print(len("123456789"))

#d)
s = "0123456789"
print(s[3],",",s[0:3], "-", s[2:5])
print(s[:3], "-" , s[3:], " , ", s[3:100])
print(s[20:], s[2:1], s[1:1])

#e)
s = "987654321"
print(s[-1], s[-3])
print(s[-3:], s[:-3])
print(s[-100:-3], s[-100:3])

#2 a)
y = str(123)
x = "hello" *3
print(x,y)
x = "hello" + "world"
y=len(x)
print(y, x)

#b)
x = "hello" + \
"to python" + \
"world"
for char in x:
    y=char
    print(y,":", end="")
    
#c)
x = "hello world"
print(x[:2], x[:-2], x[-2:])
print(x[6], x[2:4])
print(x[2:-3], x[-4:-2])

#3 (i)
theStr = "this is a test"
InputStr = input("enter integer")
inputInt = int(InputStr)
testStr = theStr
while inputInt >= 0:
    testStr = testStr[1:-1]
    inputInt = inputInt -1
testBool = "t" in testStr
print(theStr)
print(testStr)
print(inputInt)
print(testBool)

#4
testStr = "abcdefghi"
InputStr = input("enter an integer")
inputint = int(InputStr)
count = 2
newStr= ""
while count <= inputInt:
    newStr = newStr + testStr[0:count]
    testStr = testStr[2:] #L1
    count= count +1
print(newStr)             #L2
print(testStr)            #L3
print(count)              #L4
print(inputInt)           #L5

'''
#5
inputStr = input("Give me a string")
bigInt = 0
littleInt = 0
otherInt = 0
for ele in inputStr :
    if ele >="a" and ele <="m":    #L1
        littleInt = littleInt + 1
    elif ele > "m" and ele <="z":
        bigInt = bigInt + 1
    else:
        otherInt = otherInt + 1
print("bigInt is", bigInt)   #l2
print("littleint is", littleInt)#l3
print("otherInt is", otherInt) #L4
print("is it all digit", inputStr.isdigit()) #L5


#6
