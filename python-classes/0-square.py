#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
"""

class Square:
    """
    This class defines a square by its size.
    
    The size is a private attribute to enforce encapsulation and data protection.
    """
    def __init__(self, size):
        """
        Initialize a new Square instance with a given size.

        Args:
            size (int): The size of the square (no validation).
        """
        self.__size = size

