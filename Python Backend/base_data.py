'''
Imports (procedurally added as needed)
'''
import sys
import pandas as pd

'''
Convert data from user entered list to DataFrame so pandas can handle it easier

List Formatting:
[
weight (grams: float), 
length (cm: float), 
maximum diameter (mm: float), 
stability caliber (float),
center of gravity x (x coordinate: mm float),
center of gravity y (y coordinate: cm float)
]

ex: [430.0, 60.5, 6.1, 2.0, 20.2, 0.0]

List will come from the user, some data like CG coords. and stab. cal. will be functions
'''

weight = float(sys.argv[1])
length = float(sys.argv[2])
max_dia = float(sys.argv[3])
stab_cal = float(sys.argv[4])
cg_x = float(sys.argv[5])
cg_y = float(sys.argv[6])
test = str(sys.argv[7])
rocket_name = str(sys.argv[8])
rocket_data_list = [weight, length, max_dia, stab_cal, cg_x, cg_y]

data_check_key = {'Weight': 'Float (Decimal) in Grams',
                    'Length': 'Float (Decimal) in CM', 
                    'Maximum Diameter': 'Float (Decimal) in MM', 
                    'Stability Caliber': 'Float (Decimal) in CM',
                    'Center of Gravity X': 'Float (Decimal) in MM',
                    'Center of Gravity Y': 'Float (Decimal) in CM'}
indicies = ['Weight', 'Length', 'Maximum Diameter', 'Stability Caliber', 'CG: X', 'CG: Y']
rocket_data_df = pd.DataFrame(rocket_data_list, index=indicies, columns=[rocket_name])
type_check_cond = True
if test == "True":
    print('Beginning Test Check of Data')
    process = 0
    
    for i in rocket_data_list:
        key = list(data_check_key.keys())[process]
        value = list(data_check_key.values())[process]
        if not isinstance(i, float):
            process += 1
            type_check_cond = False
        else:
            process += 1
            continue
else:
    print('No check')

print(type_check_cond)
