class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.served = 0

    def describe_restaurant(self):
        print(f"The name of my restaurant is {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open till midnight.")

    def number_served(self):
        """Print a statement of the number of people served in this restaurant"""
        print(f"This restaurant has served {self.served} number of people.")

    def set_number_served(self, people):
        """Set the number of people served a the given value"""
        self.served = people

    def increment_number_served(self, day):
        """Add the given amount to the number fo people served."""
        self.served += day

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavours):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def describe_flavour(self):
        """Print a statement describing the ice cream flavour."""
        for flavour in self.flavours:
            print(f"This ice cream is {flavour}")
            
restaurant = Restaurant('Le Chateau', 'French cuisine')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(250)
restaurant.number_served()

restaurant.increment_number_served(100)
restaurant.number_served()

restaurant_1 = IceCreamStand('Le Chateau', 'French cuisine', ['vanilla', 'strawberry', 'chocolate'])
restaurant_1.describe_restaurant()
restaurant_1.describe_flavour()


# italian_restaurant = Restaurant('La Dolce Vita', 'Italian cuisine')
# italian_restaurant.describe_restaurant()
# italian_restaurant.open_restaurant()

# spanish_restaurant = Restaurant('Boca Chica', 'Spanish cuisine')
# spanish_restaurant.describe_restaurant()
# spanish_restaurant.open_restaurant()