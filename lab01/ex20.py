#Strings are arrays

a = "Hello, World!"
print(a[1])

#Loop through string

for x in "banana":
  print(x)

#size of string 

b = "Hello, World!"
print(len(b))

#check string

txt = "The best things in life are free!"
print("free" in txt)

#check with if

txt1 = "The best things in life are free!"
if "free" in txt1:
  print("Yes, 'free' is present.")

#check if NOT

txt2 = "The best things in life are free!"
print("expensive" not in txt2)

#check if not whit if

txt3 = "The best things in life are free!"
if "expensive" not in txt3:
  print("No, 'expensive' is NOT present.")

