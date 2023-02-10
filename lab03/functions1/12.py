def histogram(myList) :
    myList1 = []
    for i in range(0, len(myList)) :
        for j in range(0, myList[i]) :
            myList1.append("*")
        print("".join(myList1))
        myList1 = []

histogram([1,2,3,4,5,6,7])