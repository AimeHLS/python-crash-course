# FIRST APPROACH: module_name.function_name()
import pizza
pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(13,"olives","bacon","mushrooms", "extra cheese")

# SECOND APPROACH
# Importing Specific Functions: from module_name import function_0,
# function_1,function_2

from pizza import make_pizza

make_pizza(14, "pepperoni")
make_pizza(13,"olives","bacon","mushrooms", "extra cheese")

# THIRD APPROACH
# Using as to Give a Function an Alias
# Incase the function being imported might
# conflict with an existing name in the program

from pizza import make_pizza as mg

mg(16, "pepperoni")
mg(13,"olives","bacon","mushrooms", "extra cheese")
#from module_name import function_name as fn

# FOURTH APPROACH
#Using as to Give a Module an Alias

import pizza as p
p.make_pizza(15, "pepperoni")
p.make_pizza(13,"olives","bacon","mushrooms", "extra cheese")
#import module_name as mn

#FIFTH APPROACH
# Importing All Functions in a Module
# Use asterisk(*)

from pizza import*
make_pizza(15, "pepperoni")
make_pizza(13,"olives","bacon","mushrooms", "extra cheese")
#from module_name import*

# STYLING FUNCTIONS
def function_name(
            parameter_0, parameter_1, parameter_2,
            parameter_3, parameter_4, parameter_5,):
    "How to make sure function parameters do not exceed 79 characters per line"
    # Press ENTer after opening paranthesis, press TAB key twice
    # Separate more than one function by two blank lines
    # All import statements should be written at the beginning of the file.
    # unles you use comment at the beginning of the file to describe
    # the overall program