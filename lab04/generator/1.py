def square_gen(n) :
    a = 0
    while(a <= n) :
        yield a ** 2
        a += 1

my_num = int(input('Enter an integer number : '))

for x in square_gen(my_num) :
    print(x)