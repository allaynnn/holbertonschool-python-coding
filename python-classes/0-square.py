#!/usr/bin/python3
"""
This module defines a class Square that represents a square.

A square has equal sides, and this class uses a private attribute `__size` to store
the size of one side of the square. The size attribute is private to ensure
encapsulation and control over future updates or validations.
"""

class Square:
    """
    Represents a square.

    The size attribute is private, ensuring encapsulation and protecting 
    the square's internal state from direct access or modification. 
    Future enhancements or validations can be added for the size.
    """
    def __init__(self, size):
        """
        Initialize a new Square instance with a given size.

        Args:
            size (int): The size of one side of the square (no validation).
        """
        self.__size = size
