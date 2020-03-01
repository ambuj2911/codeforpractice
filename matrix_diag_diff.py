

def foo(n,matrix):
    sum_left = 0
    sum_right = 0

    for i in range(n):
        sum_left = sum_left + matrix[i][i]
        sum_right = sum_right + matrix[i][n-1-i]

    if sum_right<sum_left:
        return sum_left-sum_right
    else:
        return sum_right-sum_left



n = int(input())
matrix = []

for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input()))
    matrix.append(b)
print(matrix)

print(foo(n,matrix))