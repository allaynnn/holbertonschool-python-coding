#!/usr/bin/python3
"""
This module defines a class Square that represents a square.

A square has equal sides and this class encapsulates the size of the square
as a private attribute to ensure encapsulation and future control.
"""

class Square:
    """
    Represents a square with a private size attribute.

    The size of the square is stored privately to restrict direct access
    and modifications, enabling future validation and control.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance with a given size.

        Args:
            size (int): The size of one side of the square (no validation).
        """
        self.__size = size
