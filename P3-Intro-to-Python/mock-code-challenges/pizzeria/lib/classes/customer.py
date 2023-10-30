class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.pizzas = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 15):
            self._name = name
        else:
            raise Exception("Unacceptable name for customer")

    def access_current_orders(self, new_order=None):
        from classes.order import Order
        if new_order is not None and isinstance(new_order, Order):
            self.orders.append(new_order)
        return self.orders

    def access_current_pizzas(self, new_pizza=None):
        from classes.pizza import Pizza
        if new_pizza is not None and isinstance(new_pizza, Pizza) and (new_pizza not in self.pizzas):
            self.pizzas.append(new_pizza)
        return self.pizzas
