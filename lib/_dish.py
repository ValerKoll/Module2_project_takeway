class Dish():
    def __init__(self, dish_name, dish_dict):
        self.dish_name = dish_name
        self.dish_price = dish_dict['price']
        self.cooking_time = dish_dict['time']