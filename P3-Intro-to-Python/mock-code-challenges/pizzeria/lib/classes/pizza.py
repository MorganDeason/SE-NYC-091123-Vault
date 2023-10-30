class Pizza:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.customers = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("'Pizza.name' already exists!")

    def access_current_orders(self, new_order=None):
        from classes.order import Order
        if new_order is not None and isinstance(new_order, Order):
            self.orders.append(new_order)
        return self.orders
        

    def access_current_customers(self, new_customer=None):
        from classes.customer import Customer
        if isinstance(new_customer, Customer) and (new_customer not in self.customers):
            self.customers.append(new_customer)
        return self.customers

    def calculate_total_number_of_orders(self):
        pass

    def calculate_average_price_across_all_orders(self):
        pass
