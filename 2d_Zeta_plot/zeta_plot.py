import matplotlib.pyplot as plt
import numpy as np
import cmath as c


# create data
def create_inputs(low_limit, high_limit):
    step_width = 0.01
    delta = high_limit - low_limit
    steps = int(delta / step_width)
    inputs = []
    for i in range(steps):
        inputs.append(0.5 + low_limit*1j)
        low_limit += step_width
    return np.asarray(inputs)


def zeta_function(z):
    z = 1/1**z + 1/2**z + 1/3**z + 1/4**z + 1/5**z
    return np.asarray(z)


def get_real_component(z):
    return z.real


def get_imaginary_component(z):
    return z.imag


# x = get_real_component(complex_numbers)
# y = get_imaginary_component(complex_numbers)
inputs = create_inputs(0,50)
print(inputs)
outputs = zeta_function(inputs)
print(outputs)
real_outputs = get_real_component(outputs)
imaginary_outputs = get_imaginary_component(outputs)
fig, ax = plt.subplots(figsize=(10,10))
ax.plot(real_outputs, imaginary_outputs)
ax.set(xlim=(-4, 4), xticks=np.arange(-4,4),
       ylim=(-4, 4), yticks=np.arange(-4,4))
plt.show()
