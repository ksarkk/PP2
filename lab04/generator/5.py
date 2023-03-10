def anti_seq(n) :
    while n >= 0 :
        yield n
        n -= 1

my_num = int(input())
for x in anti_seq(my_num) :
    print(x)