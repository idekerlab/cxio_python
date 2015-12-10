import json
import decimal
import collections
from cxio.cx_constants import CxConstants
from cxio.cx_util import CxUtil


class CxWriter(object):

    """ This is to write CX data to a output stream.
    """

    def __init__(self, out):
        """ Creates a new CxWriter for writing to "out".
        :param out: object
                    A file-like object to write to
        """
        if out is None:
            raise AssertionError('output stream must not be none')
        self.__out = out
        self.__pre_meta_data = []
        self.__post_meta_data = []
        self.__aspect_element_counts = {}
        self.__started = False
        self.__ended = False
        self.__fragment_started = False
        self.__first = True
        self.__in_fragment = False

    def add_pre_meta_data(self, pre_meta_data):
        """ To add pre meta data, to be written prior to the aspect elements.
        :param pre_meta_data: list
                              A list of Elements representing pre-meta data
        """
        if pre_meta_data is None:
            raise AssertionError('pre meta data must not be none')
        if self.__ended:
            raise IOError('already ended')
        if self.__started:
            raise IOError('already started')
        self.__add_meta_data(self.__pre_meta_data, pre_meta_data)

    def add_post_meta_data(self, post_meta_data):
        """ To add post meta data, to be written after the aspect elements.
        :param post_meta_data: list
                               A list of Elements representing post-meta data
        """
        if post_meta_data is None:
            raise AssertionError('post meta data must not be none')
        if self.__ended:
            raise IOError('already ended')
        self.__add_meta_data(self.__post_meta_data, post_meta_data)

    def start(self):
        if self.__ended:
            raise IOError('already ended')
        if self.__started:
            raise IOError('already started')
        self.__started = True
        self.__out.write('[')
        self.__write_number_verification_element()
        if len(self.__pre_meta_data) > 0:
            self.__write_meta_data(self.__pre_meta_data)

    def end(self):
        if self.__ended:
            raise IOError('already ended')
        if not self.__started:
            raise IOError('not started')
        if self.__fragment_started:
            raise IOError('fragment not ended')
        if len(self.__post_meta_data) > 0:
            self.__write_meta_data(self.__post_meta_data)
        self.__ended = True
        self.__started = False
        self.__out.write('\n')
        self.__out.write(']')

    def start_aspect_fragment(self, aspect_name):
        if aspect_name is None:
            raise AssertionError('aspect name data must not be none')
        if self.__ended:
            raise IOError('already ended')
        if not self.__started:
            raise IOError('not started')
        if self.__fragment_started:
            raise IOError('fragment already started')
        self.__fragment_started = True
        if self.__first:
            self.__first = False
        else:
            self.__out.write(', ')
        self.__out.write('\n')
        self.__out.write(' { ')
        self.__out.write('"')
        self.__out.write(aspect_name)
        self.__out.write('"')
        self.__out.write(':')
        self.__out.write(' ')
        self.__out.write('[')
        self.__out.write(' ')
        self.__out.write('\n')

    def end_aspect_fragment(self):
        if self.__ended:
            raise IOError('already ended')
        if not self.__fragment_started:
            raise IOError('fragment not started')
        self.__fragment_started = False
        self.__out.write(' ')
        self.__out.write(']')
        self.__out.write('\n')
        self.__out.write(' }')
        self.__in_fragment = False

    def write_aspect_element(self, element):
        if self.__ended:
            raise IOError('already ended')
        if not self.__fragment_started:
            raise IOError('fragment not started')
        if self.__in_fragment is True:
            self.__out.write(', ')
            self.__out.write('\n')
        self.__out.write('  ')
        self.__out.write(self.__aspect_element_to_json(element))
        self.__in_fragment = True
        my_name = element.get_name()
        if my_name not in self.__aspect_element_counts:
            self.__aspect_element_counts[my_name] = 1
        else:
            self.__aspect_element_counts[my_name] += 1

    def __write_number_verification_element(self):
        e = CxUtil.create_number_verification_element()
        self.__out.write('\n')
        self.__out.write(' { ')
        self.__out.write('"')
        self.__out.write(e.get_name())
        self.__out.write('"')
        self.__out.write(':')
        self.__out.write(' ')
        self.__out.write(self.__aspect_element_to_json(e))
        self.__out.write(' },')

    def __write_meta_data(self, meta_data):
        self.start_aspect_fragment(CxConstants.META_DATA)
        for e in meta_data:
            self.write_aspect_element(e)
        self.end_aspect_fragment()

    def get_aspect_element_counts(self):
        return self.__aspect_element_counts

    @staticmethod
    def __aspect_element_to_json(aspect_element):
        return json.dumps(aspect_element.get_data(), cls=DecimalEncoder)

    @staticmethod
    def __add_meta_data(meta_data, add_me):
        if isinstance(add_me, collections.Iterable):
            meta_data.extend(add_me)
        else:
            meta_data.append(add_me)


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


