#!/usr/bin/python3
"""Module for Square class."""


class Square:
    """Defines a square by size."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size (int, float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int, float): The size of the square.

        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal in area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square is less than another in area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square is less than or equal to another in area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square is greater than another in area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square is greater than or equal to another in area."""
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
