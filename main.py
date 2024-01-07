#regular modules:
import numpy as np 
import matplotlib.pyplot as plt
import cmath

#file modules:
import input_creation as ic
import function as f

start_radius = 0.0
end_radius = 1.0
delta_radius = abs(start_radius-end_radius)
point_density = 10.0
layer_density = 10.0
num_slices = ic.get_num_of_slices(delta_radius,layer_density)
radius_step = delta_radius/num_slices



radii = ic.get_radii(start_radius,num_slices,radius_step)
inputs = ic.create_3d_inputs(start_radius,end_radius,point_density,layer_density)
ax = plt.figure().add_subplot(projection='3d')
for i in range(inputs.size):
    x = np.zeros(inputs[i].size)
    x.fill(radii[i])
    ax.scatter(x,f.real_from_complex(inputs)[i],f.imag_from_complex(inputs)[i]) 
    
    plt.show()
print(inputs)

