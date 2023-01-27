def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function :

y = "awesome"

def myfunc():
  global y
  y = "fantastic"

myfunc()

print("Python is " + y)