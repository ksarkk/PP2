def has33(nums) :
    a = True
    for i in range(0, len(nums) - 1) :
        if(nums[i] == nums[i + 1]) :
            if(nums[i] == 3) :
                a = False
                print("True")
                break
    if(a == True) :
        print("False") 

has33([1, 3, 3])
has33([1, 3, 1, 3])
has33([3, 1, 3]) 