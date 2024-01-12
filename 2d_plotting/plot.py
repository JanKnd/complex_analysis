import numpy as np
import cmath
import matplotlib.pyplot as plt

import function as f
import input_creation as ic

ax = plt.figure().add_subplot(projection='3d')

def single_layer_figure(radius: float,point_density:float):
    complex_outputs = f.input_to_output(ic.create_inputs(radius,point_density))
    x = np.full(complex_outputs.size,radius,dtype=float)
    y = f.real_from_complex(complex_outputs)
    z = f.imag_from_complex(complex_outputs)    
    ax.plot(x,y,z, color="blue")


def plot_single_layer(radius: float, point_density:float):
    single_layer_figure(radius,point_density)
    plt.show()



def plot_multi_layer(start_radius:float, end_radius:float, layer_density:float, point_density:float):
    delta_radius = abs(end_radius-start_radius)
    num_layers = get_num_layers(delta_radius,layer_density)
    radius_step = get_radius_step(delta_radius, num_layers)
    curr_radius = start_radius
    for i in range(num_layers):
        single_layer_figure(curr_radius, point_density)
        curr_radius += radius_step
    plt.show()



def get_num_layers(delta_radius: float, layer_density:float) -> float:
    num_layers = int(delta_radius*layer_density)
    if layer_density < 1:
        return(1)
    else:
        return(num_layers)
    


def get_radius_step(delta_radius: float,num_layers:float) -> float:
    return(delta_radius/num_layers)


    