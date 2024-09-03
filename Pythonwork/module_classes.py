"""A set of classes used to represent gas and electric cars."""

class Car:
    """A class that can be used to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        # Nothing else happens here, except initializing attributes.
        self.make = make
        self.model = model
        self.year = year
        #SETTING A DEFAULT VALUE FOR AN ATTRIBUTE
        self.odometer_reading = 20
        self.tank_capacity = 65

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def fill_gas_tank(self):
        """Print a message that shows the capacity of car's tank."""
        print("This car runs on diesel and has"
              f" {self.tank_capacity} litres gas tank.")


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