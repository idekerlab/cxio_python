class Element(object):

    """ This is to represent one (non-aspect) element of a CX document.
    For example, it is used to represent meta data and number-verification elements.
    Attributes:
        name  The name of the element
        data  The actual data of the element (a dictionary)
    """
    def __init__(self, name, data):
        if name is None:
            raise AssertionError('element name must not be none')
        if data is None:
            raise AssertionError('element data must not be none')
        self.__name = name
        self.__data = data

    def get_name(self):
        return self.__name

    def get_data(self):
        return self.__data

    def __str__(self):
        return str(self.__name) + ': ' + str(self.__data)
