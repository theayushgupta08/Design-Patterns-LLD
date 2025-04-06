'''
The Factory Design Pattern is a creational pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

Abstract Factory - The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes.

It is like grouping certain similar objects. Such as in below example we can group shape in 2 categories withoutEdge (conatins Circle) and withEdge (conatins Rectangle)

It is like Factory of Factories.

'''

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle!")

class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle!")


class ShapeFactory:
    def getShape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            return None 
        
if __name__=="__main__":
    factory = ShapeFactory()

    Shape1 = factory.getShape("circle")
    Shape2 = factory.getShape("rectangle")

    Shape1.draw()
    Shape2.draw()