def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#
def my_function1(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function1(fruits)

#
def my_function2(x):
  return 5 * x

print(my_function2(3))
print(my_function2(5))
print(my_function2(9))

#
def myfunction3():
  pass

#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)