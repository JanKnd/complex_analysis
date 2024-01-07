#           |imaginary / z
#           |_____ real / y
#          /
#         /  radius / x
# f(x) {x ∈ R   ->   z(x)=x+f(x)i {x ∈ C
import numpy as np

def function(z: complex) -> complex:
    #f(x) = x^2
    return(z+(z**2)*(0+1j))

# def singel_layer_output(inputs: tuple) -> tuple:
#     outputs = []
#     for i in inputs:
#         outputs.append(function(inputs[i]))
#     return(tuple(outputs))

def real_from_complex(input:np.array) -> np.array:
    real_part_whole = [[]]
    real_part_sub = []
    for layer in range(input.size):
        real_part_sub = []
        for point in range(input[layer].size):
            real_part_sub.append(input[layer][point].real)
        real_part_sub = np.asarray(real_part_sub)
        real_part_whole.append(real_part_sub)
    return(np.asarray(real_part_whole, dtype= "object"))

def imag_from_complex(input:np.array) -> np.array:
    real_part_whole = [[]]
    real_part_sub = []
    for layer in range(input.size):
        real_part_sub = []
        for point in range(input[layer].size):
            real_part_sub.append(input[layer][point].imag)
        real_part_sub = np.asarray(real_part_sub)
        real_part_whole.append(real_part_sub)
    return(np.asarray(real_part_whole, dtype="object"))
