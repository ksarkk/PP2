def div_by_three_four(n) :
    a = 12
    while(a <= n) :
        if a % 4 == 0 and a % 3 == 0 :
            yield a
        a += 1

my_num = int(input('Enter an integer number : '))
for x in div_by_three_four(my_num) :
    print(x)