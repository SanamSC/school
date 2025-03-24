#5
"""
string = input("enter a string:" )
lenght = len(string)
a = 0
end = lenght
string2 = ""
while a<lenght :
    if a == 0:
        string2 +=string[0].upper()
        a +=1
    elif(string[a] == " " and string[a+1] != " "):
        string2 += string[a]
        string2 += string[a+1].upper()
        a += 2
    else:
        string2 += string[a]
        a += 1
print("original string:" , string)
print("Capatalized words string" , string2)
"""
#6
word = input("enter a string: ")
lenght1 = len(word)
mid = lenght1 // 2
rev = -1
for a in range(mid):
    if word[a] == word[rev]:
        a += 1
        rev -= 1
    else:
        print(word, "is not a palindrome")
        break
else:
        print(word, "is a palindrome")
        
    
#7
string1=input("enter a word:")
width=len(string1)
maxlenght=0
maxwidth=0
maxsub=""
sub=""
lensub=0
for b in range(width):
    if string1[b] in "aeiou" or string1[b] in "AEIOU":
        if lensub >maxwidth:
            sub+=string1[b]
            lensub=len(sub)
            maxsub=sub
            maxwidth=lensub-1
        else:
            sub+=string1[b]
            lensub=len(sub)
       # a+=1
print('maximum width consonant sub string is :', maxsub, end='' )
print(' with', len(sub), ' characters')


#8
string2 = input("enter a string")
lenght2 = len(string2)
print("original string is" , string2)
string3 = " "
for c in range(0,lenght2,2):
    string3 += string2[c]
    if c < (lenght2 - 1):
        string3 += string2[c + 1].upper()
print("alterantively capatalized string:" , string3)


#9
email =input("enter an email")
domain = "@edupillar.com"
lendomain = len(domain)
lenemail = len(email)
substring = email[lendomain - lenemail :]
if substring == domain:
    if lendomain != lenemail:
        print("its a valid email")
    else:
        print("this is an invalid email - conatains only domain")
else:
    print("this email-id is either not valid or belongs to some other domain")