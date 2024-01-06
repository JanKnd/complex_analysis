import numpy as np 
import math
import cmath

tau:float = 2*math.pi 

#creates np.array of complex numbers as inputs for complex function
#density = of points 1 unit of length along the circumference (higher -> more points)
def create_2d_inputs(radius : float, density: float) -> tuple:
    num_points:int = get_num_of_points(radius, density)
    
    try:
        angle_step:float = tau / num_points
    except:
        angle_step: float = tau / 1

    curr_angle = 0.0
    two_d_inputs = []
    for i in range(num_points):
        two_d_inputs.append(cmath.rect(radius,curr_angle))
        curr_angle += angle_step
    return(two_d_inputs)

def get_num_of_points(radius: float, density: float) -> int:
    circumference:float = tau*radius**2
    num_points = int(circumference*density)
    return(num_points)


#creates np.array of np.array's of complex numbers as inputs for complex function
def create_3d_inputs(start_radius: float, end_radius: float,point_density : float, layer_density: float) -> tuple:
    delta_radius:float = abs(end_radius-start_radius)
    num_of_slices: int = get_num_of_slices(delta_radius,layer_density)
    radius_step:float = delta_radius/num_of_slices
    three_d_inputs = []
    curr_radius: float = 0.0    
    for i in range(num_of_slices):
        three_d_inputs.append(create_2d_inputs(curr_radius,point_density))
        curr_radius += radius_step
    return(three_d_inputs)

def get_num_of_slices(delta_radius, layer_density: float) -> int:
    delta_radius
    num_slices = int(delta_radius*layer_density)
    return(num_slices)
