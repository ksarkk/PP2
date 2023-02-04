car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

if "model" in car:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change


x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change