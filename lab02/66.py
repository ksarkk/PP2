def my_function():
  print("Hello from a function")

my_function()

#
def my_function1(fname):
  print(fname + " Refsnes")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

#
def my_function2(fname, lname):
  print(fname + " " + lname)

my_function2("Emil", "Refsnes")

#
def my_function3(*kids):
  print("The youngest child is " + kids[2])

my_function3("Emil", "Tobias", "Linus")

#
def my_function4(**kid):
  print("His last name is " + kid["lname"])

my_function4(fname = "Tobias", lname = "Refsnes")
