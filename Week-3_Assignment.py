n_row= int(input())
n_col= int(input())
array_2d = [[0 for i in range(n_col)] for j in range(n_row)]

for i in range(n_row):
    for j in range(n_col):
        array_2d[i][j]= i*j

print(array_2d)
