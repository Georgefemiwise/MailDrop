# from django.test import TestCase

import time
CURRENT_YEAR = time.strftime('%Y')
# # Create your tests here.
def get_index( program:str, index:int ): 
    r"micro function for getting the right formated index number"
    
    programAbbrv = '07' #ARRAY_OF_PROGRAMS[program]
    department  = "ict" if program != 'hnd' else '000'
    
    if program != 'hnd':
        address = f"{programAbbrv}/{department}/{CURRENT_YEAR[2:]}/{index:03}" 
        return address
    
    else:
        address = f"{programAbbrv}{CURRENT_YEAR[2:]}{index:06}"
        return address
        
print(get_index('hnd', 5))
