from cxio.aspect_element import AspectElement
from cxio.cx_constants import CxConstants


class CxWriter(object):

    def __init__(self, f):
        self.__f = f
        self.__in_fragment = False
        self.__first = True
        self.__started = False
        self.__fragment_started = False
        self.__pre_meta_data = []
        self.__post_meta_data = []
        self.__aspect_element_counts = {}

    def add_pre_meta_data(self, pre_meta_data):
        if self.__started:
            raise IOError('already started')
        self.__pre_meta_data.extend(pre_meta_data)

    def add_post_meta_data(self, post_meta_data):
        self.__post_meta_data.extend(post_meta_data)

    def get_aspect_element_counts(self):
        return self.__aspect_element_counts

    def start(self):
        if self.__started:
            raise IOError('already started')
        self.__started = True
        self.__f.write('[')
        if len(self.__pre_meta_data) > 0:
            self.start_aspect_fragment(CxConstants.META_DATA)
            for e in self.__pre_meta_data:
                self.write_aspect_element(e)
            self.end_aspect_fragment()

    def end(self):
        if not self.__started:
            raise IOError('not started')
        if self.__fragment_started:
            raise IOError('fragment not ended')
        self.__f.write('\n')
        self.__f.write(']')

    def start_aspect_fragment(self, aspect_name):
        if not self.__started:
            raise IOError('not started')
        if self.__fragment_started:
            raise IOError('fragment already started')
        self.__fragment_started = True
        if self.__first:
            self.__first = False
        else:
            self.__f.write(', ')
        self.__f.write('\n')
        self.__f.write(' { ')
        self.__f.write('"')
        self.__f.write(aspect_name)
        self.__f.write('"')
        self.__f.write(':')
        self.__f.write(' ')
        self.__f.write('[')
        self.__f.write(' ')
        self.__f.write('\n')

    def end_aspect_fragment(self):
        if not self.__fragment_started:
            raise IOError('fragment not started')
        self.__fragment_started = False
        self.__f.write(' ')
        self.__f.write(']')
        self.__f.write('\n')
        self.__f.write(' }')
        self.__in_fragment = False

    def write_aspect_element(self, element):
        if not self.__fragment_started:
            raise IOError('fragment not started')
        if self.__in_fragment is True:
            self.__f.write(', ')
            self.__f.write('\n')
        self.__f.write('  ')
        self.__f.write(element.to_json())
        self.__in_fragment = True

