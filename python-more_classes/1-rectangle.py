#!/usr/bin/python3

"""
- 'width' and 'height' must be integers.
- 'width' and 'height' must be greater than or equal to zero.

"""


class Rectangle:
    """
    A class to define a rectangle by its width and height.
    Provides property getters and setters with validation to ensure
    the values are integers and non-negative.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.
        Arguments:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
