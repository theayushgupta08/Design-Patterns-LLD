class BasePizza:
    def cost(self):
        pass 


class MargerithaPizza(BasePizza):
    def cost(self):
        return 100
    
class VegDelightPizza(BasePizza):
    def cost(self):
        return 150 
    

class ToppingsDecorator(BasePizza):    # Having is-a relationship
    pass

class ExtraCheeseToppings(ToppingsDecorator):
    basePizza = BasePizza()    # Having has-a relationship also, therefore adding some additional features to base Class that is BasePizza
 
    def __init__(self, basePizza):
        self.basePizza = basePizza


    def cost(self):
        return self.basePizza.cost() + 50
    
class MushroomToppings(ToppingsDecorator):
    basePizza = BasePizza()

    def __init__(self, basePizza):
        self.basePizza = basePizza


    def cost(self):
        return self.basePizza.cost() + 10
    

if __name__=="__main__":
    myPizza = MushroomToppings(MargerithaPizza())
    print("Cost of your Pizza is: ", myPizza.cost())

    myPizza1 = MushroomToppings(ExtraCheeseToppings(MargerithaPizza()))
    print("Cost of your Pizza is: ", myPizza1.cost())

