a = ("Python", "Html", "Java")
b = list(a)
b[1] = "C++"
a = tuple(b)
print(a)

a = ("apple", "banana", "cherry")
b = list(a)
b.append("orange")
a = tuple(b)
print(a)

colours = ("purple", "brown", "orange")
y = list(colours)
y.remove("orange")
colours = tuple(y)
print(colours)

colours = ("purple", "brown", "orange")
del colours
print(colours)

colours = ("Red", "Blue", "Green")
(apple,kiwi,mango) = colours

print(apple)
print(kiwi)
print(mango)


