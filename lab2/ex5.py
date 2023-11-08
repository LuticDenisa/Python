# 0 sub diagonala
def zeros(mat):
    rows = len(mat)
    cols = len(mat[0])

    for i in range(rows):
        for j in range(cols):
            if i > j:
                mat[i][j] = 0

    return mat


ex = [
    [1, 4, 3],
    [2, 1, 6],
    [7, 6, 6]
]

result = zeros(ex)
for row in result:
    print(row)
