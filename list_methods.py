a = [1,2,3]
a.append(27) #adds 1 item to the end
print(a)
b = ["James20"] * 4
a.extend(b) #adds one list at the end, same as a+b
print(a)

 # rpop removes by position
x = a.pop(3)
print(x)
print(a)

a.remove(3)
print(a)
while True:
     try:
         a.remove("james20")
        except ValueError:
         break
print(a)