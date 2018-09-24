"""The doggy module."""



class Dog(object):
    """The class representing all dogs."""

    def __init__(self, name):
        """Constructor for dog objects."""
        self.name = name

    def bark(self):
        """Make some noise."""
        print("Bow-wow-how.")


fido = Dog("Fido the wonder dog")


print(fido.name)


fido.bark()

