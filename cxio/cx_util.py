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
    def create_edges_aspect_element(edge_id, source_id, target_id, interaction):
        """
        :rtype: AspectElement
        """
        e = {'@id': edge_id,
             's': source_id,
             't': target_id,
             'i': interaction
             }
        return AspectElement(CxConstants.EDGES, e)

    @staticmethod
    def create_edge_attribute_aspect_element(edge_id, name, value):
        """
        :rtype: AspectElement
        """
        e = {'po': edge_id,
             'n': name,
             'v': value
             }
        return AspectElement(CxConstants.EDGE_ATTRIBUTES, e)

    @staticmethod
    def create_node_attribute_aspect_element(node_id, name, value, att_type=None):
        """
        :rtype: AspectElement
        """
        e = {'po': node_id,
             'n': name,
             'v': value
             }
        if att_type:
            e['t'] = att_type
        return AspectElement(CxConstants.NODE_ATTRIBUTES, e)

    @staticmethod
    def create_pre_metadata_element(aspect_name, consistency_group, version, last_update):
        """
        :rtype: Element
        """
        e = {'name': aspect_name,
             'consistencyGroup': consistency_group,
             'version': version,
             'lastUpdate': last_update
             }
        return Element('metaData', e)

    @staticmethod
    def create_post_metadata_element(aspect_name, id_counter):
        """
        :rtype: Element
        """
        e = {'name': aspect_name,
             'idCounter': id_counter,
             }
        return Element('metaData', e)

    @staticmethod
    def create_number_verification_element():
        """ Convenience method to create a number verification element
        :rtype: Element
        """
        e = [dict(longNumber=CxConstants.NUMBER_VERIFICATION_VALUE)]
        return Element(CxConstants.NUMBER_VERIFICATION, e)

    @staticmethod
    def create_ndex_citation_aspect_element(citation_id, citation_type, title, contributors, identifier, description):
        """
        :rtype: AspectElement
        """
        e = {'@id': citation_id,
             'dc:title': title,
             'dc:contributor': contributors,
             'dc:identifier': identifier,
             'dc:type': citation_type,
             'dc:description': description,
             'attributes': []
             }
        return AspectElement('citations', e)

    @staticmethod
    def create_ndex_support_aspect_element(support_id, cx_citation_id, text):
        """
        :rtype: AspectElement
        """
        e = {'@id': support_id,
             'citation': cx_citation_id,
             'text': text,
             'attributes': []
             }
        return AspectElement('supports', e)

    @staticmethod
    def create_ndex_function_term_aspect_element(function_term):
        """
        :rtype: AspectElement
        """
        e = {'function_term': function_term}
        return AspectElement('functionTerms', e)

    @staticmethod
    def create_ndex_node_citation_aspect_element(node_id, citation_id):
        """
        :rtype: AspectElement
        """
        e = {'citations': [citation_id],
             'po': [node_id]
             }
        return AspectElement('nodeCitations', e)

    @staticmethod
    def create_ndex_node_support_aspect_element(node_id, support_id):
        """
        :rtype: AspectElement
        """
        e = {'supports': [support_id],
             'po': [node_id]
             }
        return AspectElement('nodeSupports', e)

    @staticmethod
    def create_ndex_edge_support_aspect_element(edge_id, support_id):
        """
        :rtype: AspectElement
        """
        e = {'supports': [support_id],
             'po': [edge_id]
             }
        return AspectElement('edgeSupports', e)

    @staticmethod
    def create_ndex_context_element(contexts):
        """
        :rtype: Element
        """
        return Element('@context', contexts)

