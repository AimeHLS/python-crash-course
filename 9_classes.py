#What to expect:
# Write classes and create instances of those classes

# Specify the kind of information that can be stored in instances, and define
# actions that can be taken with these instances.

# Write classes that extend the functionality of existing classes, when
# similar classes share common functionality, more can be done with less code

# Store classes in modules and import classes written by other programmers in
# my own program files.

# Learn about object-oriented programming so that I can see the world as a
# programmer does ((:exciting:))...understand the code: line by line but also
# bigger concepts behind it...train me to think logically so that I can be able
# to write a code that addresses almost any problem I encounter.

# Make life easier, enabling collaboration with other programmers by writing
# code based on the same kind of logic...accomplish more.


class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit (self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        #ACCESSING ATTRIBUTES INSIDE THE CLASS:
        #self.attribute (bcse self stands for and instance)

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")



#1 MAKING AN INSTANCE FROM A CLASS:
# instance = Class("parameter1", "parameter2")

my_dog = Dog("Willie", 6)

#2 ACCESSING ATTRIBUTES OUTSIDE THE CLASS:
# instance name.attribute

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

#To access attributes of an instance, dot notation is used: my_dog.name

#  When defining methods within a class, we use 'self' to access attributes
# and methods of that instance.

# However, when we are outside the class and want to access the attributes
# of an instance, we use the 'instance name' (my_dog in this case) to access
# those attributes.

# CALLING METHODS
#instance.method()

my_dog.sit()
my_dog.roll_over()

# TRYING IT MYSELF

class Restaurant:
    """An attempt best restaurants in the city."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nIn my experience, one of the best restaurant in Tianjin is"
              f"{self.restaurant_name} and they cook {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open right now.")

restaurant = Restaurant("Blue Frog", "Western")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("Anda Rusi","Arabic")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant("Turka", "Turkish")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()


# print("\nIn my experience, one of the best restaurant in Tianjin is"
# f"{restaurant.restaurant_name} and they cook {restaurant.cuisine_type}")
# print("In my experience, the best restaurant in Tianjin is"
# f"{restaurant.restaurant_name} and they cook {restaurant.cuisine_type}")

class Users:
    """An attempt to know and welcome new users."""
    def __init__(self,first_name, last_name,user_name, age,email  ):
        """Initialize users' basic attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.age = age
        self.email = email
        #self.email = f"{self.first_name}{self.last_name}@example.com"


    def describe_user(self):
        """Describing user based on user info."""
        print(f"\n{self.user_name}:"
              f"\n\tFirst name {self.first_name}"
              f"\n\t Last name:{self.last_name}"
              f"\n\t Age:{self.age}"
              f"\n\t Email:{self.email}")
        # print(f"\n\t Email:{self.email}")

    def greet_user(self):
        """A simple greeting and welcome message to the user."""
        print(f"\nHello {self.first_name}! we are happy to have you here.")

user_0 = Users("Amanda", "Bomb", "Sunshine250", 25, "amanda@python.com")
user_0.describe_user()
user_0.greet_user()

user_1 = Users("Curtis", "Jackson", "50cent", 40, "curtis@python.com")
user_1.describe_user()
user_1.greet_user()

user_2 = Users("Sean", "Carter", "Jayz", 45, "seancarter@python.com")
user_2.describe_user()
user_2.greet_user()

# WORKING WITH CLASSES AND INSTANCES

# Once a class is defined, a big chunk of time is spent working with instances
#created from a class. one of the first tasks is to modify attributes associated
#with particular instance.

class Car:
    """A simple attempt to represent a car."""
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


my_new_car = Car("Tesla", "cybertruck", "2023")
print()
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# MODIFYING ATTRIBUTE VALUES

#1 Modifying Attribute's Value Directly
# The simplest way is to access the attribute directly through an instance.

print()
my_new_car.odometer_reading = 23
#Using a default attribute, we access the attribute by: instance.attribute
my_new_car.read_odometer()

#2 Modifying an Attribute's Value Through a Method.

class Odometer(Car):
    """Add logic to the previous read_odometer method."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
           self.odometer_reading = mileage
           #mileage is the argument that will be passed as new odometer reading
        else:
            print("\nYou cannot roll back an odometer!")

        print(f"This car has {self.odometer_reading} miles on it.")
        # updated_odometer_message = f"This car has {self.odometer_reading} miles on it."
        # return updated_odometer_message

#3 Incrementing an Attribute's Value Through a Method

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_new_car = Odometer("Tesla", "Cybertruck", "2024")
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)

print()
my_used_car = Odometer("Toyota", "Landcruiser", "2018")
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
my_used_car.fill_gas_tank()

# TRYING IT MYSELF

#1 RESTAURANT

class Restaurant:
    """Attempting to describe best restaurants in the city."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 300

    def describe_restaurant(self):
        print("\nIn my experience, one of the best restaurant in Tianjin is "
              f"{self.restaurant_name} and they cook {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open right now.")


    def set_number_served(self, number):
        """Telling the number of clients served by restaurant."""
        self.number_served = number
        print(f"{self.restaurant_name} has served {self.number_served} clients.")

    def increment_number_served(self,total_number):
        """Add up the number of clients served by the restaurant."""
        self.number_served += total_number
        print(f"And up to now {self.restaurant_name} has served"
              f"{self.number_served} clients")

restaurant = Restaurant("Blue Frog", "Western")
restaurant.describe_restaurant()

# restaurant.number_served = 200
# print(f"{restaurant.restaurant_name} has served {restaurant.number_served} clients.")
restaurant.open_restaurant()

restaurant.set_number_served(300)
restaurant.increment_number_served(100)

#2 LOGIN ATTEMPTS

class Users:
    """An attempt to know and welcome new users."""
    def __init__(self,first_name, last_name,user_name, age,email):
        """Initialize users' basic attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.age = age
        self.email = email
        self.login_attempts = 0
        #self.email = f"{self.first_name}{self.last_name}@example.com"


    def describe_user(self):
        """Describing user based on user info."""
        print(f"\n{self.user_name}:"
              f"\n\tFirst name {self.first_name}"
              f"\n\t Last name:{self.last_name}"
              f"\n\t Age:{self.age}"
              f"\n\t Email:{self.email}")
        # print(f"\n\t Email:{self.email}")

    def greet_user(self):
        """A simple greeting and welcome message to the user."""
        print(f"\nHello {self.first_name}! we are happy to have you here.")

    def increment_login_attempts(self, attempts):
        """Tell how many times the user has tried to login"""
        self.login_attempts += attempts
        print(f"You have attempted to login {self.login_attempts} times")


user_0 = Users("Amanda", "Bomb", "Sunshine250", 25, "amanda@python.com")
user_0.increment_login_attempts(0)

#  INHERITANCE

# The __init_() method for a child class

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self,make, model, year, battery_size):
        #Calling attributes of parent class and if needed, adding new attributes
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # Calling in the initialization of parent calss
        self.battery_size = battery_size

        # DEFINING ATTRIBUTES AND METHODS FOR THE CHILD CLASS
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars do not have gas tanks."""
        print("This car doesn't have a gas tank!")

print()
my_leaf = ElectricCar("nissan", "leaf", 2024, 40)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()

# INSTANCES AS ATTRIBUTES

# Also known as composition this approach is used to clean up the code
# by moving some methods and attributes to another class and
# using that class as an attribute to the previous class.

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

    def __init__(self,make, model, year, battery_size=75):
        #Calling attributes of parent class
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) # Calling methods of parent class.
        self.battery = Battery(battery_size)
        # Setting a default attribute to the previous class to connect both classes.

    def fill_gas_tank(self):
        """Electric cars do not have gas tanks."""
        print("This car doesn't have a gas tank!")

print()
my_tesla = ElectricCar("tesla", "cybertruck", 2024, 65)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()

# Change the attributes directly, since class battery only has one attribute

my_BMW_i4 = ElectricCar("bmw", "i4", "2022", 40)
print()
print(my_BMW_i4.get_descriptive_name())
my_BMW_i4.battery.get_range()

# MODELING REAL-WORLD OBJECTS

#IMPORTING CLASSES



