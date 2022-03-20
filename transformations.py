import numpy as np
import matplotlib.pyplot as graph


def transform(title, matrix, t_matrix, bounds):
    graph.title(title)
    graph.xlim(bounds[0], bounds[1])
    graph.ylim(bounds[0], bounds[1])

    # Multiply the two matrices
    result = np.dot(t_matrix, matrix)

    # Transpose to get (x,y) coordinates
    result = result.T
    matrix = matrix.T

    if (matrix.size == 2): # Single point (a,b)
        # Append the point [0,0] to produce a line from the origin to our point
        result = np.append(result, [[0, 0]], axis=0)
        matrix = np.append(matrix, [[0, 0]], axis=0)
    
    # Take the transpose to seperate x and y values
    matrix_x, matrix_y = matrix.T
    result_x, result_y = result.T

    # Add the x and y axes
    graph.axvline(x=0, c="black", linewidth = 1.5)
    graph.axhline(y=0, c="black", linewidth = 1.5)


    graph.plot(matrix_x, matrix_y, linewidth = 2, label = "Original")
    graph.plot(result_x, result_y, linewidth = 2, label = "Resultant", c="red")
    graph.fill(matrix_x, matrix_y, "c")
    graph.fill(result_x, result_y, "magenta")
    graph.grid()
    graph.legend()
    graph.show()


def x_reflection(matrix, bounds = [-8, 8]):
    reflection = np.array([
        [1, 0],
        [0, -1]
    ])
    transform("Reflection across x-axis", matrix, reflection, bounds)

def y_reflection(matrix, bounds = [-8, 8]):
    reflection = np.array([
        [-1, 0],
        [0, 1]
    ])
    transform("Reflection across y-axis", matrix, reflection, bounds)

def counterclockwise_90_rotation(matrix, bounds = [-8, 8]):
    rotation = np.array([
        [0, -1],
        [1, 0]
    ])
    transform("90 Degree Counterclockwise Rotation", matrix, rotation, bounds)

def x_expansion(matrix, factor, bounds = [-8, 8]):
    if (factor < 1): raise ValueError("For factor < 0 please use x_compression.")
    expansion = np.array([
        [factor, 0],
        [0, 1]
    ])
    transform("X-Expansion", matrix, expansion, bounds)

def x_compression(matrix, factor, bounds = [-8, 8]):
    if (factor > 1): raise ValueError("For factor > 0 please use x_expansion.")
    compression = np.array([
        [factor, 0],
        [0, 1]
    ])
    transform("X-Compression", matrix, compression, bounds)

def y_expansion(matrix, factor, bounds = [-8, 8]):
    if (factor < 1): raise ValueError("For factor < 0 please use y_compression.")
    expansion = np.array([
        [1, 0],
        [0, factor]
    ])
    transform("Y-Expansion", matrix, expansion, bounds)  

def y_compression(matrix, factor, bounds = [-8, 8]):
    if (factor > 1): raise ValueError("For factor > 0 please use y_expansion.")
    compression = np.array([
        [1, 0],
        [0, factor]
    ])
    transform("Y-Compression", matrix, compression, bounds)

def x_shear(matrix, factor, bounds = [-8, 8]):
    shear = np.array([
        [1, factor],
        [0, 1]
    ])
    transform("X-Shear", matrix, shear, bounds)

def scale(matrix, factor, bounds = [-8, 8]):
    scale = np.array([
        [factor, 0],
        [0, factor]
    ])
    transform("Scaled by a factor of: " + str(factor), matrix, scale, bounds)
