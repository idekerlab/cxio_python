class AspectElement(object):

    def __init__(self, name, data):
        if name is None:
            raise AssertionError('aspect element name must not be none')
        if data is None:
            raise AssertionError('aspect element data must not be none')
        self.__name = name
        self.__data = data

    def get_name(self):
        return self.__name

    def get_data(self):
        return self.__data

    def __str__(self):
        return str(self.__name) + ': ' + str(self.__data)


