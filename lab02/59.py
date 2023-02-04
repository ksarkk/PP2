thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict.update({"color": "green"})
print(thisdict)


thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["brand"]
print(thisdict)

thisdict.clear()
print(thisdict)

del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.