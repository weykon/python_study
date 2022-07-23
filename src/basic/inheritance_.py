# class A:
# class B(A):
# Inheritance

class Vehicle:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def get_Name(self):
        return self.__name


class Bike(Vehicle):

    def __init__(self, name, color, model):

        super().__init__(name, color)       # call parent class
        self.__model = model

    def get_details(self):
        return self.get_Name() + self.__model + " in " + self.getColor() + " color"


b_obj = Bike("Cziar", "red", "TK720")
print(b_obj.get_details())
print(b_obj.get_Name())
