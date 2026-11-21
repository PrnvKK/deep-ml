def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    i, j = len(matrix), len(matrix[0])

    if mode == "column":
        res = []
        for col in range(j):
            total = 0
            for row in range(i):
                total += matrix[row][col]
            res.append(float(total/i))
    
    else:
        res = []
        for row in range(i):
            total = 0
            for col in range(j):
                total += matrix[row][col]
            res.append(float(total/j))
            
    return res