'''
Imports (procedurally added as needed)
'''
import sys

'''
Convert two pieces of user-entered information to create a stability number

Equation: CGy-CPy/avg diameter=stability caliber
'''

cg_y = sys.argv[0]
cp_y = sys.argv[1]
avg_dia = sys.argv[2]

print((cg_y-cp_y)/avg_dia)
