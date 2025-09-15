items = ["apple","mango","banana","kiwi"]
print(items)
print(items[0])
print(items[1:3])
items.append("orange")
print(items)
if "apple" in items:
    print("apple exist")
else:
    print("apple doesnt exist")
i = 1
for x in items:
    print(f"{i}){x}")
    i=i+1



fruit = input("Enter the fruit : ")
if fruit in items:
   print("Fruit exist")
else:
    items.append(fruit)
    print(items)




