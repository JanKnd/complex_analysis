import matplotlib.pyplot as plt
import numpy as np
import cmath
import math
from matplotlib import cm
from matplotlib.ticker import LinearLocator


# f(x) {x ∈ R   ->   z(x)=x+f(x)i {x ∈ C
def zeta_funtion(z: complex, degree_of_percition: int):
    output: complex = 0
    n = 1
    for i in range(degree_of_percition):
        output += 1 / (cmath.exp(z * math.log(n, 10)))
        n += 1
    return (output)


def complex_function(z: complex):
    return (1 / 1 ** z) + (1 / 2 ** z) + (1 / 3 ** z) + (1 / 4 ** z) + (1 / 5 ** z) + (1 / 6 ** z)


X_real = np.arange(-40, 40, 0.01)
Y_imag = np.arange(-2, 2, 0.01)

X, Y = np.meshgrid(X_real, Y_imag)

assert Y.shape == X.shape
matrix_shape = X.shape

xf = X.flat
yf = Y.flat

x_comp_real = np.ndarray(np.shape(xf), dtype=complex)
y_comp_imag = np.ndarray(np.shape(yf), dtype=complex)

assert np.shape(xf) == np.shape(yf), "plane must be square"
flat_len = np.shape(xf)[0]

# converting real and imag part to complex number datatype
for i in range(flat_len):
    x_comp_real[i] = complex(xf[i] + 0j)
    y_comp_imag[i] = complex(0 + yf[i] * 1j)

# adding real and imag part
xy_comp = np.add(x_comp_real, y_comp_imag)

# applying function
# xy_comp_res = np.tan(xy_comp)
xy_comp_res = np.ndarray(xy_comp.shape, dtype=complex)
for i in range(flat_len):
    xy_comp_res[i] = zeta_funtion(xy_comp[i], 5)
    # complex_function(xy_comp[i])

# z coordinates = abs val of complex number
xy_abs_val = np.abs(xy_comp_res)

# color mapping var
xy_angle = np.ndarray(flat_len)
for i in range(flat_len):
    xy_angle[i] = cmath.phase(xy_comp_res[i])

# initializing arrs for real and imag results
x_real_res = np.ndarray(flat_len)
y_imag_res = np.ndarray(flat_len)

# reshaping to matrix
xy_abs_val, xy_angle = np.reshape(xy_abs_val, matrix_shape), np.reshape(xy_angle, matrix_shape)

# plotting
norm = plt.Normalize(vmin=-np.pi, vmax=np.pi)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

surf = ax.plot_surface(X, Y, xy_abs_val, facecolors=plt.cm.gist_rainbow(norm(xy_angle)),
                       linewidth=0, antialiased=True)
ax.set_xlabel('real')
ax.set_ylabel('imaginary')
ax.set_zlabel('absolute value')
ax.set_zlim(0, 6)

m = cm.ScalarMappable(cmap=plt.cm.gist_rainbow, norm=norm)
plt.colorbar(m)

plt.show()
