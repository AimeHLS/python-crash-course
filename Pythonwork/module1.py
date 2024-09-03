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