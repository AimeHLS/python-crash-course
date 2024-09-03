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

    def describe_menu(self,menu):
        """Displaying restaurant's menu."""
        self.menu = menu

        print("\nOn tonight's menu, we have:")

        for item in menu:
            print("." + item.title())


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
            print("--> " + flavor.title())