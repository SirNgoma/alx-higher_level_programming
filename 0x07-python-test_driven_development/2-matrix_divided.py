#!/usr/bin/python3

"""
devides all element of a matrix. Example
   >>>  matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""
def matrix_divided(matrix, div):
    """
    returns new matrix:
    TypeError: matrix must be a matrix 
    TypeError: each row of the matrix must have the same size
    ZeroDivisionError: division by Zero
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    id div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)


    return new_matrix


if __name__ == '__main__':
    import doctest
    doctest.testmod()
