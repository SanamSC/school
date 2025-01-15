#1
string = input("enter a string")
for i in string:
    print(i)
    
#2
word = input("enter a word")
lenght = len(word)
for a in word:
    if a.islower():
        print(a.upper())
for b in word:
    if b.isupper():
        print(b.lower())

#3
input1 = input("enter an input")
final = ""
for c in input1:
    double = c*2
    final = final + double
print(final)

#4

    