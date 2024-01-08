samplearray = [
    [2,1,-1,2],
    [2,0,1,3],
    [1,-1,0,0],
]

max_rows = len(samplearray)
max_cols = len(samplearray[0])


current_col = 0

for r1 in range(max_rows-1):
    r2 = r1 + 1
    while r2 < max_rows:
        scalar = -1 * samplearray[r2][current_col] / samplearray[r1][current_col]
        for col in range(current_col, max_cols):
            samplearray[r2][col] = samplearray[r1][col]*scalar + samplearray[r2][col]
        r2 += 1
    current_col += 1
print(samplearray)