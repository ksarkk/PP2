def uniqueAndReverseList(myList) :
    myList1 = []
    for a in myList :
        if a not in myList1 :
            myList1.append(a)
    myList1.reverse()
    print(", ".join(myList1))

def isPalindrome(myString) :
    myList = list(myString) 
    j = len(myList) - 1
    for i in range(0, len(myList)) : 
        if(myList[i] != myList[j]) :
            print("Not Palindrome")
            break
        j -= 1
    if(j == -1) :
        print("Palindrome") 

string = input()
myList = string.split()
isPalindrome(myList)
uniqueAndReverseList(myList)
