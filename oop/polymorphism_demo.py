import math

class Shape:
    """Base class for all shapes."""

    def area(self):
        """Method to be overridden in derived classes."""
        raise NotImplementedError("The area() method must be overridden in subclasses")


class Rectangle(Shape):
    """Rectangle shape derived from Shape."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape derived from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of a circle."""
        return math.pi * (self.radius ** 2)
