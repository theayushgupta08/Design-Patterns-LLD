from AllBasePizzas.MargerithaPizza import MargerithaPizza
from AllToppings.MushroomToppings import MushroomToppings
from AllToppings.ExtraCheeseToppings import ExtraCheeseToppings

if __name__=="__main__":
    myPizza = MushroomToppings(MargerithaPizza())
    print("Cost of your Pizza is: ", myPizza.cost())

    myPizza1 = MushroomToppings(ExtraCheeseToppings(MargerithaPizza()))
    print("Cost of your Pizza is: ", myPizza1.cost())