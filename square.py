squareSize = input("what size square do you want?")
squareSize = int(squareSize)
for row in range(1,squareSize + 1):
    for ok in range(squareSize):
        print("*", end="")
    print()
