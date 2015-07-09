triSize = input("what size triangle do you want?")
triSize = int(triSize)
for row in range(1,triSize + 1):
    for ok in range(row):
        print("*", end="")
    print()
