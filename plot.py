import numpy as np
import cmath
import matplotlib.pyplot as plt

import function as f
import input_creation as ic

#ax = plt.figure().add_subplot(projection='3d')

def single_layer_plot(radius: float,point_density:float):
    complex_outputs = f.input_to_output(ic.create_inputs(radius,point_density))
    x = np.full(complex_outputs.size,radius,dtype=float)
    y = f.real_from_complex(complex_outputs)
    z = f.imag_from_complex(complex_outputs)
    
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(x,y,z)
    plt.show()

