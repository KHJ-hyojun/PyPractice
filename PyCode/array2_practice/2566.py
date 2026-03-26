Max = 0
max_row = 0
max_col = 0
matrix = []
for i in range(9):
    matrix.append(list(map(int,input().split())))



for row in range(9):
    for col in range(9):
        if matrix[row][col] >= Max:
            Max = matrix[row][col]
            max_row = row
            max_col = col
print(Max)
print(max_row + 1, max_col + 1)