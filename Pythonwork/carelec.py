from module2 import ElectricCar
from module1 import Car
print("My cars")
nissan = ElectricCar("nissan", "leaf", 2012, 40)
print(nissan.get_descriptive_name())

print()
truck = Car("ford", "raptor", "2019")
print(truck.get_descriptive_name())

# USING ALIASES

# Aliases on classes
print()
from module_classes import ElectricCar as EC
tesla = EC("tesla", "model x", 2023, 65)
print(tesla.get_descriptive_name())
tesla.battery.get_range()

#2 Aliases on the whole module
import module2 as ec