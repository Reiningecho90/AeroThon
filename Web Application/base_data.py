'''
Imports (procedurally added as needed)
'''
import pandas as pd


def get_rocket_data(rocket_data_list, test=True, rocket_name='Rocket 1'):
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
    data_check_key = {'Weight': 'Float (Decimal) in Grams',
                      'Length': 'Float (Decimal) in CM', 
                      'Maximum Diameter': 'Float (Decimal) in MM', 
                      'Stability Caliber': 'Float (Decimal) in CM',
                      'Center of Gravity X': 'Float (Decimal) in MM',
                      'Center of Gravity Y': 'Float (Decimal) in CM'}
    indicies = ['Weight', 'Length', 'Maximum Diameter', 'Stability Caliber', 'CG: X', 'CG: Y']
    rocket_data_df = pd.DataFrame(rocket_data_list, index=indicies, columns=[rocket_name])
    if test:
        print('\033[1;33mBeginning Test Check of Data\033[0m')
        process = 0
        for i in rocket_data_list:
            key = list(data_check_key.keys())[process]
            value = list(data_check_key.values())[process]
            if not isinstance(i, float):
                print(f'Value of {key} does not follow the format. Use: {value}.')
                process += 1
            else:
                print(f'{key} typecheck \033[0;32mpassed!\033[0m')
                process += 1
                continue
    else:
        print('No check')
    return rocket_data_df


def unit_test(base_data=True):
    '''
    Run certain unit tests for various functions
    '''
    if base_data:
        test_data = [430.0, 60.5, 6.1, 2.0, 20.2, 0.0]
        get_rocket_data(rocket_data_list=test_data, test=True, rocket_name='Rocket Test')


unit_test(base_data=True)
