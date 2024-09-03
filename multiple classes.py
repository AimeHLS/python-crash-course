

class Car:
    """Represent aspects of a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def fill_gas_tank(self):
        """Gas tank filling method."""
        print("This car's gas tank is now full.")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75, manufacturer="Generic Co.Ltd"):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
        self.manufacturer = manufacturer

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery manufactured by "
              f"{self.manufacturer}.")

    def upgrade_battery(self):
        """A method for upgrading electric car's battery."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
            #Hasn't been able to solve this.


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 300  # Default range for battery_size=75
        print(f"This car can go about {range} miles on a full charge.")




class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(

                self, make, model, year, battery_size=75,
                 battery_manufacturer="Generic Co.Ltd."

                 ):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery(battery_size, battery_manufacturer)


    def fill_gas_tank(self):
        """Electric cars do not have gas tanks."""
        print("This car doesn't have a gas tank!")

# Creating instances
my_leaf = ElectricCar("nissan", "leaf", 2024, 40)
print(f"\n{my_leaf.get_descriptive_name()}")
my_leaf.battery.describe_battery()
# I haven't understood this yet
my_leaf.fill_gas_tank()
my_leaf.battery.get_range()

my_tesla = ElectricCar("tesla", "cybertruck", 2024, 65)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()

my_BMW_i4 = ElectricCar("bmw", "i4", 2022)
print(my_BMW_i4.get_descriptive_name())
my_BMW_i4.battery.describe_battery()
my_BMW_i4.battery.get_range()

tesla_model3 = ElectricCar("tesla", "model 3", 2020)
print(tesla_model3.get_descriptive_name())


#Display the initial range
print("Initial Range: ")
tesla_model3.battery.get_range()

#Upgrade the battery and show the range:
tesla_model3.battery.upgrade_battery()
print("Upgraded Range:")
tesla_model3.battery.get_range()

# TRY IT MYSELF

#1  Ice Cream Stand

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

class IceCreamStand(Restaurant):
    """Icecream stand a section of restaurant."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initialize attributes of parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def dispaly_flavors(self):
        """A display of available icecream flavors"""

        print(f"\nThese are icecream flavors available now:")
        for flavor in self.flavors:
            print("--> " + flavor)

yum_Ice = IceCreamStand(
    "blue frog",
    "western",
    ("Vanilla", "Chocolate", "strawberry")
    )
yum_Ice.dispaly_flavors()

#2 Admin, a special kind of user

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
        """A simple greetingwel/come message to the user."""
        print(f"\nHello {self.first_name}! we are happy to have you here.")

    def increment_login_attempts(self, attempts):
        """Tell how many times the user has tried to login"""
        self.login_attempts += attempts
        print(f"You have attempted to login {self.login_attempts} times")


class Privileges:
    """Indicate admin's privileges among users."""

    def __init__(self,privilege):
        """Initialize attribute"""
        self.privileges = privilege

    def show_privileges(self):
        """Indicating privileges enjoyed by admin"""

        print("\nAs an admin, you can do the following things:")
        for priv in self.privileges:
            print("." + priv.title())



class Admin(Users):
    """"Describing an admin as a special case for users class"""

    def __init__(self,first_name, last_name,user_name, age,email, privilege):
        """
        Initializing attributes for parent class.
        Adding new attributes for child class.
        """
        super(). __init__(first_name, last_name, user_name, age, email)
        self.privileges = Privileges(privilege)
        # Composition

    # def show_privileges(self): moved upwards
    #     """Indicating privileges enjoyed by admin"""
    #     print("\nAs an admin, you can do the following things:")
    #     for privilege in self.privileges:
    #         print("." + privilege.title())





smith = Admin(

    "smith",
    "jordan",
    "smjo",
    21,
    "sm@ecip@com",
    ("ban user","add post", "delete post")

    )
smith. privileges.show_privileges()

# class Student:
#     def __init__(self, name, student_ID, grade):
#         self.name = name
#         self.student_ID = student_ID
#         self.grade = grade

# class Student_management:
#     """An attempt to establish student management system."""

#     def __init__(self):
#         self.students = []

#     def add_new_student(self, name, student_ID, grade):
#         student = Student(name,student_ID, grade)
#         self.students.append(student)

#     def display_student_info(self):
#         """Displaying information about the student."""
#         print(f"{student.name}")
#         print(f"{student.student_ID}")
#         for grade in self.grades:
#             print(grade)

#     def average_grade(self):
#         """Calculating average score of every student"""
#         total_grade = 0
#         for student in self.students:
#             total_grade += student.grade
#             average_grade = total_grade / len(self.students)
#             print(f"Average Grade: {average_grade}")


# newst = Student_management()
# newst.add_new_student("Alice", 1, 78)
# newst.add_new_student("Sam", 1, 89)
# newst.add_new_student("Prince", 1, 90)

# newst.display_student_info()

# newst.average_grade()