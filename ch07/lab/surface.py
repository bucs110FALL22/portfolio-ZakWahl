from rectangle import Rectangle 
class Surface:
    """This class represents a rectangular surface.

    It contains an instance variable for a Rectangle object and a string
    representing the path to an image file. It has methods for setting and
    getting these attributes, and for drawing the image on the rectangle.
    """

    def __init__(self, filename, x, y, h, w):
        """Initializes a new surface with the given filename, x, y, h, and w values.

        The filename is saved to the self.image instance variable, and a new
        Rectangle object is created and stored in the self.rect instance variable.
        """
        # Save the filename to the image instance variable
        self.image = filename

        # Create a new rectangle with the given x, y, h, and w values
        self.rect = Rectangle(x, y, h, w)

    def getRect(self):
        """Returns the rectangle object for this surface."""
        return self.rect

    def draw(self):
        """Draws the image on the rectangle for this surface."""
        # Code to draw the image on the rectangle goes here