thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #remove returns error if such an item doesnt exist
print(thisset)

thisset.discard("banana") #discard wont return error
print(thisset)


x = thisset.pop()
print(x)
print(thisset)


thisset.clear()
print(thisset)

del thisset
print(thisset)