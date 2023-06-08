#!/usr/bin/python3

"""Rotating a 2d matrix"""


def rotate_2d_matrix(matrix):
    """ Rotate the given matrix 90 degrees"""
    matrix_size = len(matrix[0])
    for x in range(matrix_size // 2):
        for y in range(x, matrix_size - x - 1):
            temp_var = matrix[x][y]
            matrix[x][y] = matrix[matrix_size - 1 - y][x]
            matrix[matrix_size - 1 - y][x] = matrix[matrix_size -
                                                    1 - x][matrix_size - 1 - y]
            matrix[matrix_size - 1 - x][matrix_size -
                                        1 - y] = matrix[y][matrix_size - 1 - x]
            matrix[y][matrix_size - 1 - x] = temp_var
