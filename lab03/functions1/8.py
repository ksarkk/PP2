def spyGame(nums) :
    a = True
    count = 0
    for i in range(0, len(nums)) :
        if(nums[i] == 0) :
            count += 1
            for j in range(i + 1, len(nums)) :
                if(nums[j] == 0) :
                    count += 1
                    for k in range(j + 1, len(nums)) :
                        if(nums[k] == 7) :
                            count += 1
                            a = False
                            break
                    break
            break
    if(a == True) :
        print("False")
    elif(count == 3) :
        print("True")

spyGame([1,2,4,0,0,7,5]) #true
spyGame([1,0,2,4,0,5,7]) #true
spyGame([1,7,2,0,4,5,0]) #false