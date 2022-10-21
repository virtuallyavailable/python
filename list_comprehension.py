fruits = ["Apple","Banana","Pineapple","Pappaya"]
for x in fruits :
   print(x)

fruits = ["Apple","Banana","Pineapple","Pappaya"]
newlist = []
for x in fruits :
    if "p" in x :
        newlist.append(x)

print(newlist)      


languages = ["Spanish","Japanese","Turkish"]

newlist = [x for x in languages if x != "Spanish"]

print(newlist)

numbers = [x for x in range(50)]
print(numbers)

numbers = [x for x in range(50) if x < 20]

print(numbers)

languages = ["Spanish","Japanese","Turkish"]

newlist = [x.upper() for x in languages]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['Pineapple' for x in fruits]
print(newlist)






