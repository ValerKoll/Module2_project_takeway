class Order():
    def __init__(self, resturant_object):
        self.resturnat_selected = resturant_object.name
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
    
    def __repr__(self):
        text_to_print = ""
        for entry in self.resturnat_selected:
            text_to_print += f"\n\033[2;32m - {entry}"
        return text_to_print    
    
    def get_customer_order(self):
        text_to_print = ""
        for entry in self.order_list:
            text_to_print += f"\n\033[2;32m - {entry}"
        return text_to_print
    
    def order_confirmed(self):
        #calc_time        
        #store information in the customer hystory??
        pass