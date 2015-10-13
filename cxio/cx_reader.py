import ijson
import re
from ijson import ObjectBuilder
from cxio.aspect_element import AspectElement
from cxio.cx_constants import CxConstants


class CxReader(object):
    __ITEM_NAME_ITEM_RE = re.compile('item\.(\w+)\.item')

    def __init__(self, in_stream):
        if in_stream is None:
            raise AssertionError('input stream must not be none')
        self.__parser = ijson.parse(in_stream)
        self.__pre_meta_data = []
        self.__post_meta_data = []
        self.__aspect_element_counts = {}
        self.__aspect_names = set()
        self.__first_element = None
        for e in self.aspect_elements():
            if e is not None:
                self.__first_element = e
                break

    def get_aspect_element_counts(self):
        return self.__aspect_element_counts

    def aspect_elements(self):
        if self.__first_element is not None:
            my_first_element = self.__first_element
            self.__first_element = None
            yield my_first_element
        for e in self.__aspect_elements():
            yield e

    def parse_as_dictionary(self):
        dic = {}
        for e in self.aspect_elements():
            name = e.get_name()
            if name not in dic:
                dic[name] = []
            dic[name].append(e)
        return dic

    def get_pre_meta_data(self):
        return self.__pre_meta_data

    def get_post_meta_data(self):
        return self.__post_meta_data

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
                        if current_name == CxConstants.META_DATA:
                            if saw_aspect_element:
                                self.__post_meta_data.append(AspectElement(current_name, val))
                            else:
                                self.__pre_meta_data.append(AspectElement(current_name, val))
                                yield None
                        else:
                            saw_aspect_element = True
                            if current_name not in self.__aspect_element_counts:
                                self.__aspect_element_counts[current_name] = 1
                            else:
                                self.__aspect_element_counts[current_name] += 1
                            yield AspectElement(current_name, val)
        raise StopIteration()
