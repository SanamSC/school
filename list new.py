list1= ["football", "basketball"]
sport = input("whats your favourite sport?!: ")
print(list1.append(sport))
print(list1)
#print(list1.sort(sport))


#2
list2 = ["maths", "religion", "CS" , "biology", "geography", "Irish"]
print(list2)
not_like = input("Which subject is least fav")
list2.remove(not_like)
print("new list is", list2)

#3
colour = ["white", "yellow" , "blue" , "red" , "green", "indigo" , "pink", "brown", "turquoise", "black"]
start = int(input("enter a starting number between 0 and 4"))
end = int(input("enter a ending number between 5 and 9"))
print(colour[start:end])


