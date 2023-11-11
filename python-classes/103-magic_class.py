#!/usr/bin/python3
"""Module for MagicClass."""


class MagicClass:
    """Replicates the given Python bytecode."""

    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass.

        Args:
            radius (int, float): The radius of the circle.
        """
        self.__radius = 0

        if type(radius) not in [int, float]:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Compute the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * 3.14159265359

    def circumference(self):
        """Compute the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * 3.14159265359 * self.__radius


if __name__ == "__main__":
    mc = MagicClass(5)
    print(mc.area())
    print(mc.circumference())
