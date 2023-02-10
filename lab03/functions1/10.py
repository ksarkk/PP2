def uniqueList(myList) :
    myList1 = []
    for a in myList :
        if a not in myList1 :
            myList1.append(a)
    print(myList1)

string = input()
myList = string.split()
uniqueList(myList)