#!/usr/bin/python3
"""matrix_divided divides a matrix by parameter: div"""


def matrix_divided(matrix, div):
    """
    * <matrix> must be a list of lists of integers or floats
    * Each row of <matrix> must be the same size
    * <div> must be a number (integer or float)
    * <div> cannot be 0
    * All elements of <matrix> should be divided by <div>
    * Returns a new matrix containing the results
    """
    # None checks
    if not matrix:
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

    # Verify that list is matrix
    if not all(isinstance(ele, list) for ele in matrix):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

    # Verify that the matrix contains integers or floats
    # Verify that matrix row lengths are equal
    row_len = len(matrix[0])
    for row in range(len(matrix)):
        if row_len != len(matrix[row]):
            raise TypeError
            ("Each row of the matrix must have the same size")
        for element in range(len(matrix[row])):
            if not isinstance(matrix[row][element], (int, float)):
                raise TypeError
                ("matrix must be a matrix (list of lists) of integers/floats")

    # Verify that div is a number (integer/float)
    if isinstance(div, (int, float)):
        # Verify that div is not 0
        if div == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")

    # Store division results in new matrix rounded to 2 decimal places
    new_matrix = []
    for row in matrix:
        row = [number / div for number in row]
        new_row = [round(number, 2) for number in row]
        new_matrix.append(new_row)

    return new_matrix
