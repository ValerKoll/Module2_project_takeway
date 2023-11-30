class DeliveryService():
    def __init__(self, order_number, order):
        self.preparation = order.preparation_time
    
    def get_info(self):
        return f"Delivery time: {self.preparation}\n"