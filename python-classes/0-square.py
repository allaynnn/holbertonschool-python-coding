#!/usr/bin/python3
"""
This module defines the Square class.

The Square class represents a geometric square shape by storing its size
as a private instance attribute. This design supports encapsulation, and
future enhancements such as input validation or area computation.
"""

class Square:
    """
    Represents a square.

    The size attribute is private to enforce encapsulation and protect the
    internal state. This approach ensures the square’s size can be managed
    more safely and consistently in future updates.
    """
    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of one side of the square.
        """
        self.__size = size

