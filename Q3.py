
n = int(input())

if n%2 == 0:
    k = (n-1)*2 + 1
else:
    k = (n-1)*2

for i in range(0,n):

    print(" ")
    for j in range(1,k+1):

        if j-i<=i:
            print("*",end="")
        elif i+j >= k:
            print("*",end = "")
        else:
            print(" ",end = "")