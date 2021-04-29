#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Function that computes the square value of all integers
    # in a matrix
    # Initial matrix should not be modified
    # Returns a new matrix
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
