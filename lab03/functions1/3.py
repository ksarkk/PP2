def solve(numheads, numlegs):
    numRabbits = int((numlegs / 2) - numheads)
    numChickens = int(numheads - numRabbits)
    print("Number of Chickens :", numChickens)
    print("Number of Rabbits :", numRabbits)

solve(35, 94)