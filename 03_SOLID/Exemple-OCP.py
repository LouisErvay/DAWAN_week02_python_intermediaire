"""Open-Closed Principle (OCP) : Le principe d'ouverture/fermeture stipule qu'un module (comme une classe, une fonction, etc.) 
doit être ouvert à l'extension mais fermé à la modification. 
En d'autres termes, un module doit être conçu de manière à pouvoir être facilement étendu sans modifier son code existant.
Source: https://www.cleancode.studio/python/design-patterns-in-python/python-open-closed-principle-design-pattern"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def calculate_area(shapes):
    return sum([shape.area() for shape in shapes])