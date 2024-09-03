# IMPORTING MULTIPLE CLASSES IN A MODULE
from module_classes import Car, ElectricCar


my_mustang = Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())

my_cybertruck = ElectricCar("tesla", "cybertruck", 2020, 65)
print(my_cybertruck.get_descriptive_name())

# IMPORT THE ENTIRE MODULE
import module_classes


