from BasePizza import BasePizza
from ToppingsDecorator import ToppingsDecorator

class ExtraCheeseToppings(ToppingsDecorator):
    basePizza = BasePizza()    # Having has-a relationship also, therefore adding some additional features to base Class that is BasePizza
 
    def __init__(self, basePizza):
        self.basePizza = basePizza


    def cost(self):
        return self.basePizza.cost() + 50