def even_gen(n) :
    a = 0
    while(a <= n) :
        yield a
        a += 2

my_num = int(input('Enter an integer number : '))

for x in even_gen(my_num) :
    print(x, end=", ")