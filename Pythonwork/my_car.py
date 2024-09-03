
from module_classes import Car
my_new_car = Car("audi", "a4", 2024)

print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# STORING MULTIPLE CLASSES IN A MODULE
# Multiple classes can be stored in a module, though they have to be related
# to each other in some way

