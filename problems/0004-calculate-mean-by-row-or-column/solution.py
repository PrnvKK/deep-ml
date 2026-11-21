import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "column":
        np_matrix = np.array(matrix)
        return np.mean(np_matrix, axis=0).tolist()
    else:
        np_matrix = np.array(matrix)
        return np.mean(np_matrix, axis=1).tolist()
