from cxio.element import Element
from cxio.aspect_element import AspectElement
from cxio.cx_constants import CxConstants


class ElementMaker(object):
    """ Static methods for creating (aspect) element instances.
    """

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
    def create_cartesian_layout_element(node_id, view_id, x, y, z=None):
        """
        :rtype: AspectElement
        """
        e = {'node': node_id,
             'x': x,
             'y': y
             }
        if view_id:
            e['view'] = view_id
        if z:
            e['z'] = z
        return AspectElement(CxConstants.CARTESIAN_LAYOUT, e)

    @staticmethod
    def create_network_attributes_aspect_element(sub_network_id, name, value, data_type=None):
        """
        :rtype: AspectElement
        """
        e = {'n': name,
             'v': str(value)
             }
        if data_type:
            if data_type not in CxConstants.SINGLE_ATTRIBUTE_TYPES:
                raise IOError('illegal data type for network attribute "' + name + '": ' + data_type)
            if data_type != CxConstants.DATA_TYPE_STRING:
                e['d'] = data_type
        if sub_network_id:
            e['s'] = sub_network_id
        return AspectElement(CxConstants.NETWORK_ATTRIBUTES, e)

    @staticmethod
    def create_network_list_attributes_aspect_element(sub_network_id, name, values, data_type):
        """
        :rtype: AspectElement
        """
        if data_type not in CxConstants.LIST_ATTRIBUTE_TYPES:
            raise IOError('illegal data type for list network attribute "' + name + '": ' + data_type)
        e = {'n': name,
             'v': values,
             'd': data_type
             }
        if sub_network_id:
            e['s'] = sub_network_id
        return AspectElement(CxConstants.NETWORK_ATTRIBUTES, e)

    @staticmethod
    def create_edge_attributes_aspect_element(sub_network_id, edge_id, name, value, data_type=None):
        """
        :rtype: AspectElement
        """
        e = {'po': edge_id,
             'n': name,
             'v': str(value)
             }
        if data_type:
            if data_type not in CxConstants.SINGLE_ATTRIBUTE_TYPES:
                raise IOError('illegal data type for edge attribute "' + name + '": ' + data_type)
            if data_type != CxConstants.DATA_TYPE_STRING:
                e['d'] = data_type
        if sub_network_id:
            e['s'] = sub_network_id
        return AspectElement(CxConstants.EDGE_ATTRIBUTES, e)

    @staticmethod
    def create_edge_list_attributes_aspect_element(sub_network_id, edge_id, name, values, data_type):
        """
        :rtype: AspectElement
        """
        if data_type not in CxConstants.LIST_ATTRIBUTE_TYPES:
            raise IOError('illegal data type for list edge attribute "' + name + '": ' + data_type)
        e = {'po': edge_id,
             'n': name,
             'v': values,
             'd': data_type
             }
        if sub_network_id:
            e['s'] = sub_network_id
        return AspectElement(CxConstants.EDGE_ATTRIBUTES, e)

    @staticmethod
    def create_node_attributes_aspect_element(sub_network_id, node_id, name, value, data_type=None):
        """
        :rtype: AspectElement
        """
        e = {'po': node_id,
             'n': name,
             'v': str(value)
             }
        if data_type:
            if data_type not in CxConstants.SINGLE_ATTRIBUTE_TYPES:
                raise IOError('illegal data type for node attribute "' + name + '": ' + data_type)
            if data_type != CxConstants.DATA_TYPE_STRING:
                e['d'] = data_type
        if sub_network_id:
            e['s'] = sub_network_id
        return AspectElement(CxConstants.NODE_ATTRIBUTES, e)

    @staticmethod
    def create_node_list_attributes_aspect_element(sub_network_id, node_id, name, values, data_type):
        """
        :rtype: AspectElement
        """
        if data_type not in CxConstants.LIST_ATTRIBUTE_TYPES:
            raise IOError('illegal data type for list node attribute "' + name + '": ' + data_type)
        e = {'po': node_id,
             'n': name,
             'v': values,
             'd': data_type
             }
        if sub_network_id:
            e['s'] = sub_network_id
        return AspectElement(CxConstants.NODE_ATTRIBUTES, e)

    @staticmethod
    def create_pre_metadata_element(aspect_name, consistency_group, version, last_update, properties, id_counter):
        """
        :rtype: Element
        """
        e = {'name': aspect_name,
             'consistencyGroup': consistency_group,
             'version': str(version),
             'lastUpdate': last_update,
             'properties': properties,
             'idCounter': id_counter
             }
        return Element(CxConstants.META_DATA, e)

    @staticmethod
    def create_post_metadata_element(aspect_name, id_counter):
        """
        :rtype: Element
        """
        e = {'name': aspect_name,
             'idCounter': id_counter,
             }
        return Element(CxConstants.META_DATA, e)

    @staticmethod
    def create_number_verification_element():
        """ Convenience method to create a number verification element
        :rtype: Element
        """
        e = [dict(longNumber=CxConstants.NUMBER_VERIFICATION_VALUE)]
        return Element(CxConstants.NUMBER_VERIFICATION, e)

    @staticmethod
    def create_status_element(success=True, error_msg='' ):
        """ Convenience method to create a status element
        :rtype: Element
        """
        e = [{'error': error_msg,
              'success': success,
              }]
        return Element(CxConstants.STATUS, e)

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
    def create_ndex_edge_citation_aspect_element(edge_id, citation_id):
        """
        :rtype: AspectElement
        """
        e = {'citations': [citation_id],
             'po': [edge_id]
             }
        return AspectElement('edgeCitations', e)

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

