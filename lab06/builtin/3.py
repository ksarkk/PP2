my_string = 'aboba'
last_char = len(my_string) - 1
my_bool = True

for x in my_string :
    if x != my_string[last_char] :
        my_bool = False
    last_char -= 1

if my_bool :
    print("Palindrome!")
else :
    print("Not Palindrome!")