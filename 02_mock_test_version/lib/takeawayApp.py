class TakeawayApp():    
    resturants_list = []
    
    def __init__(self):
        pass
    
    def add(self, dish_entry):
        self.resturants_list.append(dish_entry)
        
    def get_dishes(self):
        return self.resturants_list