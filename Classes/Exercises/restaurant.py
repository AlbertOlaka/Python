class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of my restaurant is {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type} food.")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open till midnight.")

restaurant = Restaurant('Le Chateau', 'French cuisine')
restaurant.describe_restaurant()
restaurant.open_restaurant()

italian_restaurant = Restaurant('La Dolce Vita', 'Italian cuisine')
italian_restaurant.describe_restaurant()
italian_restaurant.open_restaurant()

spanish_restaurant = Restaurant('Boca Chica', 'Spanish cuisine')
spanish_restaurant.describe_restaurant()
spanish_restaurant.open_restaurant()