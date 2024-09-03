from printing_functions import print_models as pm
from printing_functions import show_completed_models as sm

unprinted_designs = ["pink panther", "kungfu panda", "spiderman"]
completed_models =[]

pm(unprinted_designs, completed_models)
sm(completed_models)
#The reason why the parameters are used as lists,
#they are a list


import printing_functions

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models (completed_models)


import printing_functions as pf

pf.print_models
pf.show_completed_models


# IMPORTS

#1 import module_name(module_name is the file which contains the function)
import printing_functions

printing_functions.build_me_car(
            "jeep",
            "wrangler",
            "suitable for off grid")


#2 from module_name import function_name
from printing_functions import build_me_car

build_me_car("Toyota", "tundra", "black", "offgrid tyres", "offgrid suspension")


#3 from module_name import function_name as fn

from printing_functions import build_me_car as bmc

bmc("nissan", "path finder", "grey", "chargeable hybrid")


#4 import module_name as mn
import printing_functions as pf

pf.build_me_car("mitsubishi", "pajero", "suv", "huge horse power", "offgrid car")


#5 from module_name import*
from printing_functions import*

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

unprinted_designs = ["ironman", "batman", "the hulk"]
completed_models = []


build_me_car("ford", "everest", "dark grey")



