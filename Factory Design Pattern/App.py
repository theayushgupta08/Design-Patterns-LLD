from ShapeFactory import ShapeFactory

if __name__=="__main__":
    factory = ShapeFactory()

    Shape1 = factory.getShape("circle")
    Shape2 = factory.getShape("rectangle")

    Shape1.draw()
    Shape2.draw()