#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers
    Args:
        matrix: num
    """
    for i in matrix:
        print(" ".join("{:d}".format(j)for j in i))
        
