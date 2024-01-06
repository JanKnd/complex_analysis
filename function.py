#           |imaginary / z
#           |_____ real / y
#          /
#         /  radius / x
# f(x) {x ∈ R   ->   z(x)=x+f(x)i {x ∈ C

def function(z: complex) -> complex:
    #f(x) = x^2
    return(z+(z**2)*(0+1j))

def create_complex_outputs(inputs: tuple) -> tuple:
