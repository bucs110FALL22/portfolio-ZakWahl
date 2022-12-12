import string

class StringUtility:
    """This class provides utility methods for working with strings.

    It contains an instance variable for a string, and has methods for
    manipulating and querying the string. The original string is never
    modified, and all methods return new strings.
    """

    def __init__(self, string):
        """Initializes a new StringUtility with the given string.

        The string is saved to the self.string instance variable.
        """
        
        self.string = string

    def __str__(self):
        """Returns the string itself, not changed."""
        return self.string

    def vowels(self):
        """Counts the number of vowels in the string.

        If there are 5 or more vowels in the string, the word 'many' is returned
        instead of the actual count. """
        count = sum(1 for char in self.string if char in 'aeiouAEIOU')

        
        if count >= 5:
            return 'many'

        return str(count)

    def bothEnds(self):
        """Returns a string made of the first 2 and last 2 chars of the original string.

        If the string is less than or equal to 2 characters long, then an empty string
        is returned instead. """
        if len(self.string) <= 2:
            return ""


        return self.string[:2] + self.string[-2:]

    def fixStart(self):
        """Returns a string where the first character have been changed to '*'.

        The first character itself is not changed. If the string is 1 character or
        less, it is returned unchanged.
        """
        
        if len(self.string) <= 1:
            return self.string

        
        return self.string[0] + self.string[1:].replace(self.string[0], '*')

    def asciiSum(self):
        """Returns the sum of the ASCII values of everything in the string."""
        
        ascii_sum = 0

        
        for char in self.string:
            ascii_sum += ord(char)

        
        return ascii_sum

    def cipher(self):
      """Returns an encoded string. """
      #def cipher(self):
      upper = 65
      lower = 97
      alpha = 26
      list = ""

      for j in self.string:
        if j == " ":
          list = list+j
        elif j.isupper():
          list = list+chr((ord(j)+len(self.string)-upper)%alpha+upper)
        else:
          list = list+chr((ord(j)+len(self.string)-lower)%alpha+lower)
      return list