from Dish import Dish

class Resturant():    
    def __init__(self, name, dishes_dict):
        self.name = name
        self.dishes_list = [Dish(key, value) for key, value in dishes_dict.items()] 
       
        
    def get_dishes(self):
        text_to_print = ""
        for item, dish in enumerate(self.dishes_list):
            text_to_print += f"\n\033[2;32m{item + 1}: {dish.dish_name} - Price: {dish.dish_price}"
        return text_to_print