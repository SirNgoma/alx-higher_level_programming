#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computres squre value of all int of matrix.
    Args:
        matrix: to be used
    """
    res_matrix =
    [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            res_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
