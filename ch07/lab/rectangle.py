class Rectangle:
    """This class represents a rectangle.

    It contains instance variables for the x and y coordinates of its
    upper left position, as well as its height and width. It has methods
    for setting and getting these attributes, and for computing its area
    and perimeter.
    """

    def __init__(self, x, y, h, w):
        """Initializes a new rectangle with the given x, y, h, and w values.

        If any of the x, y, h, or w values are less than 0, they are set to 0 by default.
        """
        # Set the instance variables to the given values, or to 0 if they are invalid
        self.x = x if x >= 0 else 0
        self.y = y if y >= 0 else 0
        self.height = h if h >= 0 else 0
        self.width = w if w >= 0 else 0

    def __str__(self):
        """Returns a string representation of the rectangle's x, y, width, and height."""
        return f"x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height}"



