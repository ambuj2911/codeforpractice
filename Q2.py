
n = int(input())
sum = 0
for i in range(1,n+1):

    if i %2 == 0:
        sum = sum+1
        print(sum, end="")
        print(" ",end = "")
        sum = sum+1
        print(sum)
    else:
        sum = sum+1
        print(sum)