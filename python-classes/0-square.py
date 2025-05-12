#!/usr/bin/python3
"""
This module defines the Square class which represents a square.

A square is a geometric shape with four equal sides. This class currently
defines a square by its size, stored as a private attribute.
"""

class Square:
    """
    This class defines a square by its size.

    The size attribute is private to ensure that the value is controlled
    internally. This will help prevent direct modification and allow future
    enhancements such as validation.
    """
    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of one side of the square (no type/value checks).
        """
        self.__size = size
