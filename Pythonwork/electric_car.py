from module_classes import ElectricCar

my_tesla = ElectricCar("tesla", "model x",  2023, 65)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# Now I understand my_tesla.battery helps to switch up to Battery class
my_tesla.battery.get_range()