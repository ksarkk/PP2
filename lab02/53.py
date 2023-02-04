thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

print("banana" in thisset)

#Adding the items 
thisset.add("orange")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)