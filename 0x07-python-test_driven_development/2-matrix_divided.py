#!/usr/bin/python3

"""
    Function that divide all elements in the matrix
"""


def matrix_divided(matrix, div):
    """
    Args:
        The matrix and the divisor
    Raises:
        TypeError:
            If isn't a matrix
            If the elements of the matrix aren't lists
            If the matrix's row have differents sizes
            If the divisor is not a number
        ZeroDivisionError:
            If the divisor is zero
    Return:
        A new matrix divided
    """
    new_matrix = [x[:] for x in matrix]
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(new_matrix)):

        if len(new_matrix[i]) != len(new_matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(new_matrix[i], list) or len(new_matrix[i]) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        for j in range(len(new_matrix[i])):

            if not isinstance(new_matrix[i][j], (int, float)):
                raise TypeError(
                    "matrix must be a matrix " +
                    "(list of lists) of integers/floats")

            new_matrix[i][j] = round(matrix[i][j] / div, 2)
    return new_matrix
