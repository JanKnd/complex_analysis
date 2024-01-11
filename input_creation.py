import numpy as np 
import math
import cmath

tau:float = 2*math.pi 


#---------------------------GENERAL CLARIFICATIONS:------------------------------------------------------------------------------------------------------
#radius = distance of numbers from the origin
#point_density = num of points / 1 unit of length around the diameter
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#creates inputs for complex function as circle of complex numbers around the origin
def create_inputs(radius: float,point_density: float) -> np.array:
    num_points = get_num_points(radius,point_density)
    angle_step = get_angle_step(num_points)
    angle = 0

    inputs = []
    for i in range(num_points):
        inputs.append(cmath.rect(radius,angle))
        angle += angle_step
        
    return(np.asarray(inputs))

def get_num_points(radius: float, point_density: float) -> int:
    circumference = tau*radius
    num_points = int(circumference*point_density)
    if num_points < 10:
        return(10)
    else:
        return(num_points)

def get_angle_step(num_points: int):
    return(tau / num_points)