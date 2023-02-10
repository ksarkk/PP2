def reverseString(myList) :
    print(" ".join(myList))


myString = input()
data = myString.split()
data.reverse()
reverseString(data)