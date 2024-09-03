"""A set of classes that can be used to represent electric cars."""

from module1 import Car

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 300
            print(f"This car can go about {range} miles on a full charge.")
        print(f"This car can go about {range} miles on a full charge.")



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self,make, model, year, battery_size):
        #Calling attributes of parent class and if needed, adding new attributes
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # Calling in the initializations of parent class
        self.battery_size = battery_size
        self.battery = Battery(battery_size)

        # DEFINING ATTRIBUTES AND METHODS FOR THE CHILD CLASS
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars do not have gas tanks."""
        print("This car doesn't have a gas tank!")
