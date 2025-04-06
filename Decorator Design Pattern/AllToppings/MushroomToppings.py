from BasePizza import BasePizza
from ToppingsDecorator import ToppingsDecorator

class MushroomToppings(ToppingsDecorator):
    basePizza = BasePizza()

    def __init__(self, basePizza):
        self.basePizza = basePizza


    def cost(self):
        return self.basePizza.cost() + 10