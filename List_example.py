a = []
# simplest list
print(a)
a = [1,2,3,19]
print(a)
a = [1,2,3,19, None, ["Bob","Jane", "Mary", [[], []]], True , 1000]
print(a)
print(len(a))

print(a[2])

a[2] = "Now I changed the list!"
print(a)
print(a[::-1])
# slice to only get: None, True!
print(a[1::2])
print(a[2::-2])

a1 = [1, 2, 3]
a2 = [4, 5, 6]
print(a1 + a2*3 + a1)
# You can add lists, multiply list by an integer
print(sort(a2+a1+a2))
for elem in a1+a2: #you can do a for to get items from the list
    print(elem)

