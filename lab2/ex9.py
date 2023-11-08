# matrice in care nr sunt inaltimi; returnam pozitia unei pers care are in fata pe cnv mai inalt
def sad_spec(heights):
    sad_seats = []

    rows = len(heights)
    cols = len(heights[0])

    for i in range(1, rows):
        for j in range(cols):
            spec_height = heights[i][j]

            if heights[i - 1][j] > spec_height:
                sad_seats.append((i, j))

    return sad_seats


FIELD = [[1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 3],
        [6, 6, 7, 6, 7, 5]]

result = sad_spec(FIELD)
print(result)
