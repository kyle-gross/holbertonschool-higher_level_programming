#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Prints a matrix of integers
    for i in range(len(matrix)):
        for ii in range(len(matrix[i])):
            print("{:d}".format(matrix[i][ii]), end="")
            if ii < (len(matrix[i]) - 1):
                print(" ", end = "")
        print()
