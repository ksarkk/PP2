import random
a = random.randint(1, 20)
count = 1

name = input("Hello! What is your name?" + "\n")

b = int(input("\n" + "Well, " + name + ", I am thinking of a number between 1 and 20." + "\n" + "Take a guess." + "\n"))

if(b == a) :
    print("\n" + "Good job, KBTU! You guessed my number in " + count + " guesses!")
else :
    while True :
        if(b > a) :
            b = int(input("\n" + "Your guess is too high." + "\n" + "Take a guess." + "\n"))
            count += 1
        elif(b < a) :
            b = int(input("\n" + "Your guess is too low." + "\n" + "Take a guess." + "\n"))
            count += 1
        else :
            print("\n" + "Good job, " + name + "! You guessed my number in " + str(count) + " guesses!")
            break

