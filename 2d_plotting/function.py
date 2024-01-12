#           |imaginary / z
#           |_____ real / y
#          /
#         /  radius / x
# f(x) {x ∈ R   ->   z(x)=x+f(x)i {x ∈ C
import numpy as np
import cmath

def function(z: complex) -> complex:
    #f(x) = x^2
    return(z+(cmath.tan(z))*(0+1j))

def input_to_output(inputs: np.array) -> np.array:
    outputs = []
    for input in inputs:
        outputs.append(function(input))

    return(np.asarray(outputs))

def real_from_complex(complex_arr: np.array) -> np.array:
    real = []
    for num in complex_arr:
        real.append(num.real)
    return(np.asarray(real))

def imag_from_complex(complex_arr: np.array) -> np.array:
    imag = []
    for num in complex_arr:
        imag.append(num.imag)
    return(np.asarray(imag))
