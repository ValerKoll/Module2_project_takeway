class TakeawayApp():
    __MENU_MAIN = 0
    __MENU_REST = 1
    def __init__(self):
        self.resturants_list = [Resturant(key, value) for key, value in Data.resturants_data.items()]
        ###
        self.menu_level = self.__MENU_MAIN
        self.ordernumber = 0

    def run(self):
        ans_rest = input("\033cWELCOME. PRESS ANY KEYS TO CONTINUE (q to exit):  ")
        if ans_rest == 'q':
            return False
        while True:
            print('\033c')
            print(self.get_resturants())
            max_rest_num = len(app.resturants_list)
            ans_rest = input("\033[0;39mSelect resturant (q to quit):  ")
            if ans_rest == 'q':
                break
            elif ans_rest.isdigit():
                ans_rest = int(ans_rest)
                if ans_rest > 0 and ans_rest <= len(self.resturants_list):
                    print('\033c')
                    print(self.get_resturant_dishes(ans_rest - 1))
                    while True:
                        ans_order = input("\033[0;39mSelect dishes\n(press 'Q' to cancel order, 'C' to confirm):  ")
                        if ans_order == 'q':
                            break
                        elif ans_order == 'c':
                            print(app.confirm_order())
                            break
                        elif ans_rest.isdigit():
                            ans_order = int(ans_order)
                            print(app.selected_dish(ans_order-1))
        print("EXIT - thanks for using TKway App") 

    def get_resturants(self):
        text_to_print = "\nLIST OF RESTURANTS:\n"
        text_to_print += ''.join([f"\033[0;33m{index + 1}: {resturant.name}\n" for index, resturant in enumerate(self.resturants_list)])
        return text_to_print
    
    def get_resturant_dishes(self, resturant_to_get):
        text_to_print = f"\n\033[1;33m{resturant_to_get}:"
        text_to_print += self.resturants_list[resturant_to_get].get_dishes()  # call rest.get_dishes
        return text_to_print

    def selected_resturant(self, rest_selected):
        self.rest_selected_key = list(self.resturants_dict.keys())[rest_selected]
        self.order = Order(rest_selected)
        return self.get_resturant_dishes(self.rest_selected_key)
    
    def selected_dish(self, dish_to_add):
        self.order.add_to_order(
            list(self.resturants_dict[self.rest_selected_key].dishes_list)[dish_to_add].dish_name,
            list(self.resturants_dict[self.rest_selected_key].dishes_list)[dish_to_add].dish_price,
            list(self.resturants_dict[self.rest_selected_key].dishes_list)[dish_to_add].cooking_time
            )
        text_to_print = f"\n\033[1;32mORDER:"
        text_to_print += self.order.get_customer_order()
        text_to_print += f"\nTOTAL: {self.order.cost}"
        return text_to_print
    
    def confirm_order(self):
        self.ordernumber += 1
        preparation_time = self.order.order_confirmed()
        self.deliveryservice = DeliveryService(self.ordernumber, self.order)
        return f"ORDER CONFIRMED\n{self.deliveryservice.get_info()}"
        #self.deliveryservice.add_delivery(preparation_time)
        # cal del time
        # print confirmed and time
    
        
class Resturant():    
    def __init__(self, name, dishes_dict):
        self.name = name
        self.dishes_list = [Dish(key, value) for key, value in dishes_dict.items()] 
       
        
    def get_dishes(self):
        text_to_print = ""
        for item, dish in enumerate(self.dishes_list):
            text_to_print += f"\n\033[2;32m{item + 1}: {dish.dish_name} - Price: {dish.dish_price}"
        return text_to_print
    
class Dish():
    def __init__(self, dish_name, dish_dict):
        self.dish_name = dish_name
        self.dish_price = dish_dict['price']
        self.cooking_time = dish_dict['time']

class Customer():
    pass

class Order():
    def __init__(self, resturant_id):
        self.res_id = resturant_id
        self.order_list = []
        self.delivery_time = 0
        self.cost = 0
        self.counter = 0
        self.preparation_time = 0
    
    def add_to_order(self, dish, price, time):
        self.order_list.append(dish)
        self.cost += price
        self.counter += 1
        self.delivery_time += time
        self.preparation_time = self.delivery_time / self.counter
        
    def get_customer_order(self):
        text_to_print = ""
        for entry in self.order_list:
            text_to_print += f"\n\033[2;32m - {entry}"
        return text_to_print
    
    def order_confirmed(self):
        #calc_time        
        #store information in the customer hystory??
        pass

class DeliveryService():
    def __init__(self, order_number, order):
        self.preparation = order.preparation_time
    
    def get_info(self):
        return f"Delivery time: {self.preparation}\n"



class Data():
    resturants_data = {
        "Kung-Po Chinese":{
            'King prawn':{'price': 15, 'time': 20},
            'Noodle green':{'price': 21, 'time': 11},
            'Spicy rice':{'price': 8, 'time': 15},
            'Green prawn':{'price': 14, 'time': 10}
            },
        "Random Turkey":{
            'Chicken Kebab': {'price': 11, 'time': 25},
            'Beef green':{'price': 13, 'time': 23},
            'Orange Fires':{'price': 4, 'time': 8}
            },
        "Pizza Express Italian":{
            'Pizza roman': {'price': 10, 'time': 12},
            'Hell pizza':{'price': 27, 'time': 12},
            'Garlic bread':{'price': 10, 'time': 7}
            }
        }


## create takeaway app
app = TakeawayApp()
app.run()