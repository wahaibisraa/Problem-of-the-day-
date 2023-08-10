#Calculate cone volume

import math

def calculate_cone_volume(height, radius):
    if height <= 0 or radius <= 0:
        return "Height and radius must be positive values."
    
    volume = (1/3) * math.pi * radius**2 * height
    return volume


height = float(input("Enter the height of the cone: "))
radius = float(input("Enter the radius of the cone: "))

cone_volume = calculate_cone_volume(height, radius)
print(f"The volume of the cone is: {cone_volume:.2f}")
