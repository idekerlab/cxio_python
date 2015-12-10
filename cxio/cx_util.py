from cxio.element import Element
from cxio.aspect_element import AspectElement
from cxio.cx_constants import CxConstants


class CxUtil(object):
    """ Static utility and convenience methods.
    """

    @staticmethod
    def write_aspect_fragment(cx_writer, aspect_elements):
        """ Convenience method to write a list of aspect elements ("aspect fragment").
        :param cx_writer: CxWriter
            A CxWriter ready to write aspect elements.
        :param aspect_elements: list
            The list of AspectElement (of the same category) to be written out.
        """
        if len(aspect_elements) > 0:
            name = aspect_elements[0].get_name()
            cx_writer.start_aspect_fragment(name)
            for aspect_element in aspect_elements:
                if not name == aspect_element.get_name():
                    raise ValueError('"' + str(name) + '" different from "' + str(aspect_element.get_name() + '"'))
                cx_writer.write_aspect_element(aspect_element)
            cx_writer.end_aspect_fragment()

    @staticmethod
    def create_nodes_aspect_element(node_id, node_name=None, node_represents=None):
        """ Convenience method to create a nodes aspect element
        :rtype: AspectElement
        """
        if node_name is None and node_represents is None:
            e = {'@id': node_id}
        elif node_represents is None:
            e = {'@id': node_id, 'n': node_name}
        else:
            e = {'@id': node_id, 'n': node_name, 'r': node_represents}
        return AspectElement(CxConstants.NODES, e)


    @staticmethod
    def create_number_verification_element():
        """ Convenience method to create a number verification element
        :rtype: Element
        """
        e = [dict(longNumber=CxConstants.NUMBER_VERIFICATION_VALUE)]
        return Element(CxConstants.NUMBER_VERIFICATION, e)
