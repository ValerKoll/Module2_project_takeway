from database_connection import DatabaseConnection
from resturant_repository import Resturant
from Order import Order

class TakeawayApp():
    __MENU_MAIN = 0
    __MENU_REST = 1
    def __init__(self):
        self.resturants_list = [Resturant(key, value) for key, value in Data.resturants_data.items()]
        self.max_rest_num = len(self.resturants_list)
        ###
        self.menu_level = self.__MENU_MAIN
        self.ordernumber = 0

    def run(self):
        ans_rest = input("\033cWELCOME. PRESS ANY KEYS TO CONTINUE (q to exit):  ")
        print("\033c")
        if ans_rest == 'q':
            return False
        while True:
            print(self.get_resturants())
            ans_rest = input("\033[0;39mSelect resturant (q to quit):  ")
            print('\033c')
            if ans_rest == 'q':
                break
            elif ans_rest.isdigit():
                ans_rest = int(ans_rest)
                if ans_rest > 0 and ans_rest <= self.max_rest_num:
                    resturant_object = self.resturants_list[ans_rest - 1]
                    new_order = Order(resturant_object)
                    print(new_order)
                    
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
        text_to_print = f"\n\033[1;33m{resturant_to_get.name}:"
        text_to_print += resturant_to_get.get_dishes()  # call rest.get_dishes
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

##connect to the DATABASE

app = TakeawayApp()
app.run()



from lib.artist_repository import ArtistRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()
print(connection.DATABASE_NAME)

# Seed with some seed data
connection.seed("seeds/music_library.sql")
#connection.seed("seeds/music_library_addtable.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)