'''
Imports (procedurally added as needed)
'''

import sys
import math

'''
Mass Element Add script to create a new mass object, for inside the airframe.

List Formatting: 
[
element mass,
element shape (Sphere, Rectangle, Triangular Prism, Pyramid, Cylinder, Cone),
element diameter in cm,
element height in cm,
element length in cm,
element width in cm,
x location in cm,
y location in cm,
center of gravity x location in cm,
center of gravity y location in cm,
rocket total mass
]
'''

mass = sys.argv[0]
shape = sys.argv[1]
diameter = sys.argv[2]
height = sys.argv[3]
length = sys.argv[4]
width = sys.argv[5]
location_x = sys.argv[6]
location_y = sys.argv[7]
cg_x = sys.argv[8]
cg_y = sys.argv[9]
rocket_mass = sys.argv[10]


shape_data = {}
if shape == 'Sphere':
    shape_data['volume'] = ((4/3)*math.pi)*((diameter/2)**3)
    shape_data['density'] = mass/shape_data['volume']
    shape_data['newcgy'] = ((cg_y+rocket_mass)+(location_y+mass))/rocket_mass
    shape_data['newcgx'] = ((cg_x+rocket_mass)+(location_x+mass))/rocket_mass
elif shape == 'Rectangle':
    shape_data['volume'] = length*width*height
    shape_data['density'] = mass/shape_data['volume']
    shape_data['newcgy'] = ((cg_y+rocket_mass)+(location_y+mass))/rocket_mass
    shape_data['mewcgx'] = ((cg_x+rocket_mass)+(location_x+mass))/rocket_mass
elif shape == 'Triangular Prism':
    shape_data['volume'] = (1/2)*height*length*width
    shape_data['density'] = mass/shape_data['volume']
    shape_data['newcgy'] = ((cg_y+rocket_mass)+(location_y+mass))/rocket_mass
    shape_data['newcgx'] = ((cg_x+rocket_mass)+(location_x+mass))/rocket_mass
elif shape == 'Pyramid':
    shape_data['volume'] = (length*width*height)/3
    shape_data['density'] = mass/shape_data['volume']
    shape_data['newcgy'] = ((cg_y+rocket_mass)+(location_y+mass))/rocket_mass
    shape_data['newcgx'] = ((cg_x+rocket_mass)+(location_x+mass))/rocket_mass
elif shape == 'Cylinder':
    shape_data['volume'] = math.pi*((diameter/2)**2)*height
    shape_data['density'] = mass/shape_data['volume']
    shape_data['newcgy'] = ((cg_y+rocket_mass)+(location_y+mass))/rocket_mass
    shape_data['newcgx'] = ((cg_x+rocket_mass)+(location_x+mass))/rocket_mass
elif shape == 'Cone':
    shape_data['volume'] = math.pi*((diameter/2)**2)*(height/3)
    shape_data['density'] = mass/shape_data['volume']
    shape_data['newcgy'] = ((cg_y+rocket_mass)+(location_y+mass))/rocket_mass
    shape_data['newcgx'] = ((cg_x+rocket_mass)+(location_x+mass))/rocket_mass

for i in shape_data.items():
    print(i.value())
