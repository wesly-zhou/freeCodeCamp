# Mean-Variance-Standard Deviation Calculator

import mean_var_std
from unittest import main

example_list = [0,1,2,3,4,5,6,7,8]
calc_hashmap = mean_var_std.calculate(example_list)
print('First list contains the values along the y-axis, second list contains \
the values along the x-axis, third value is for the flattened list')
for key, value in calc_hashmap.items():
    print(f'{key}: {value[0]}, {value[1]}, {value[2]}')

# Run unit tests
# main(module='test_module', exit=False)