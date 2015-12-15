import re
import ijson
from ijson import ObjectBuilder
from cxio.aspect_element import AspectElement
from cxio.element import Element
from cxio.cx_constants import CxConstants


class CxReader(object):

    """ This is to read CX data from a input stream (a file-like object).
    This reader reads a CX formatted stream in a iterative manner via method
    "aspect_elements()" which behaves like an iterator.
    Example:
        cx_reader = CxReader(in_stream)
        for e in cx_reader.aspect_elements():
            print(e)
    Additionally (mostly for testing purposes), this reader also
    provides method "parse_as_dictionary()" which returns all aspect elements
    as one (large) dictionary.
    """

    __ITEM_NAME_ITEM_RE = re.compile('item\.(\w+)\.item')

    def __init__(self, in_stream):
        """ Creates a new CxReader for reading from "in_stream".
        :param in_stream: object
                          A file-like object to read from
        """
        if in_stream is None:
            raise AssertionError('input stream must not be none')
        self.__parser = ijson.parse(in_stream)
        self.__pre_meta_data = []
        self.__post_meta_data = []
        self.__aspect_element_counts = {}
        self.__aspect_names = set()
        self.__first_element = None
        self.__number_verification = None
        self.__status = None
        for e in self.aspect_elements():
            if e is not None:
                self.__first_element = e
                break

    def aspect_elements(self):
        """ This method is used to actually read aspect elements.
        It returns a iterator (which in turn returns AspectElement objects)
        and is to be used in a loop construct.
        Example:
        for e in cx_reader.aspect_elements():
            print(e)
        """
        if self.__first_element is not None:
            my_first_element = self.__first_element
            self.__first_element = None
            yield my_first_element
        for e in self.__aspect_elements():
            yield e

    def get_aspect_element_counts(self):
        """ Returns a dictionary containing the counts of
        AspectElements read in.
        :rtype: dict
        """
        return self.__aspect_element_counts

    def get_pre_meta_data(self):
        """ Returns the pre-metadata.
        Can be called as soon as a CxReader has been created.
        :rtype: list of Element
        """
        return self.__pre_meta_data

    def get_post_meta_data(self):
        """ Returns the post-metadata.
        To be called once a stream has been completely read in.
        :rtype: list of Element
        """
        return self.__post_meta_data

    def get_number_verification(self):
        """ Returns the number verification element.
        :rtype: Element
        """
        return self.__number_verification

    def get_error_msg(self):
        """ Returns error of the status element.
        To be called once a stream has been completely read in.
        :rtype: String
        """
        return self.__status.get_data()['error']

    def get_is_success(self):
        """ Returns success of the status element.
        To be called once a stream has been completely read in.
        :rtype: Boolean
        """
        return self.__status.get_data()['success']

    def parse_as_dictionary(self):
        """ Convenience method to return all aspect elements
        as one (large) dictionary. Not recommended for real-world
        applications.
        :rtype: dict
        """
        dic = {}
        for e in self.aspect_elements():
            name = e.get_name()
            if name not in dic:
                dic[name] = []
            dic[name].append(e)
        return dic

    def __aspect_elements(self):
        current_name = None
        builder = None
        saw_aspect_element = False
        for prefix, event, value in self.__parser:
            if event == 'start_map':
                m = self.__ITEM_NAME_ITEM_RE.fullmatch(prefix)
                if m is not None:
                    current_name = m.group(1)
                    builder = ObjectBuilder()
            if builder is not None and current_name is not None:
                builder.event(event, value)
                if event == 'end_map':
                    if prefix == 'item.%s.item' % current_name:
                        val = builder.value
                        builder = None
                        if current_name == CxConstants.NUMBER_VERIFICATION:
                            self.__number_verification = Element(current_name, val)
                        elif current_name == CxConstants.STATUS:
                            self.__status = Element(current_name, val)
                        elif current_name == CxConstants.META_DATA:
                            if saw_aspect_element:
                                self.__post_meta_data.append(Element(current_name, val))
                            else:
                                self.__pre_meta_data.append(Element(current_name, val))
                                #yield None
                        else:
                            saw_aspect_element = True
                            if current_name not in self.__aspect_element_counts:
                                self.__aspect_element_counts[current_name] = 1
                            else:
                                self.__aspect_element_counts[current_name] += 1
                            yield AspectElement(current_name, val)
        raise StopIteration()
