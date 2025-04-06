

from ShapesTypes.Circle import Circle
from ShapesTypes.Rectangle import Rectangle


class ShapeFactory:
    def getShape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            return None 