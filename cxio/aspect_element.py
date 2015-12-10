class AspectElement(object):

    """ This is to represent one aspect element.
    Attributes:
        name  The name of the aspect
        data  The actual data of the aspect (a dictionary)
    """

    def __init__(self, name, data):
        """ Creates a new AspectElement.
        :param name: string
        :param data: dict
        """
        if name is None:
            raise AssertionError('aspect element name must not be none')
        if data is None:
            raise AssertionError('aspect element data must not be none')
        self.__name = name
        self.__data = data

    def get_name(self):
        """ Returns the name of the aspect element.
        :rtype: string
        """
        return self.__name

    def get_data(self):
        """ Returns the data of the aspect element.
        :rtype: dict
        """
        return self.__data

    def __str__(self):
        return str(self.__name) + ': ' + str(self.__data)


