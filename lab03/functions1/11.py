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

isPalindrome(string)