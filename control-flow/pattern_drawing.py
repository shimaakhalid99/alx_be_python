size = int(input("Enter the size of the pattern:"))
i = 0
while i<=size-1:
    for j in range(size):
        print("*",end="")
    print()
    i +=1