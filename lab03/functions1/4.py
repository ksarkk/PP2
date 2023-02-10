def filterPrime(myList) :
    for i in range(len(myList) - 1) :
        if myList[i] == 1 :
            continue
        elif myList[i] == 2 :
            print(2)
        else :
            for x in range(2, myList[i]) :
                if myList[i] % x == 0 :
                    break
                elif x == myList[i] - 1 :
                    print(myList[i])
            

myList = [1, 3, 2, 5, 8, 6, 89, 55, 64]

filterPrime(myList)