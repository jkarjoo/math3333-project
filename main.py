import numpy as np
from transformations import *

def runTransformations(matrix):
    x_reflection(matrix)
    y_reflection(matrix)
    counterclockwise_90_rotation(matrix)
    x_expansion(matrix, 2)
    x_compression(matrix, 0.5)
    y_expansion(matrix, 2)
    y_compression(matrix, 0.5)
    x_shear(matrix, 0.5)
    scale(matrix, 0.5)


def main():
    point = np.array([
        [2],
        [3]
    ])

    pentagon = np.array([
        [0, 2, 4, 4, 2, 0],
        [2, 4, 3, 0, -1, 2]
    ])

    square = np.array([
        [2, 2, 6, 6, 2],
        [0, 2, 2, 0, 0]
    ])

    triangle = np.array([
        [2, 4, 6, 2],
        [2, 4, 2, 2]
    ])


    runTransformations(point)
    runTransformations(pentagon)
    runTransformations(square)
    runTransformations(triangle)

main()